#coding:utf-8

from flask import Flask, render_template, request, redirect, url_for
from src.data.data import School_data, MyData
import json
from src.login.User_model import User_data
from tour_guide_system.src.algorithm import Dijkstra, CountAllPath, KMP_in, Kruskal

app = Flask(__name__)

User = User_data()

# 获得景点信息的通用函数
def get_spots():
    spots_data = []
    for point in MyData.spots:
        if point.flag:
            spots_data.append([point.name, point.id])
    return spots_data

# check登陆信息
def Check_login(ip):
    return User.is_login(ip)

# 主页
@app.route('/')
def index():
    return render_template('index.html', spots = MyData.spots.values())

# 展示页面
@app.route('/spot/<i>')
def spot(i):
    data = {}
    data['name'] = MyData.spots[i].name
    data['disc'] = MyData.spots[i].disc
    data['func'] = MyData.spots[i].func
    data['id'] = MyData.spots[i].id
    return render_template('spot.html',data = data)

# 名称搜索页面
@app.route('/name_search', methods = ['POST'])
def name_search():
    i = MyData.locate(request.form['name'])
    if(i==1):
        return render_template('warning.html',info=u'没有结果 !', back='index')
    return redirect(url_for('spot', i=i))
    
# 功能搜索页面
@app.route('/func_search', methods = ['POST'])
def func_search():
    func = request.form['func']
    data = []
    for each in MyData.spots.values():
        if KMP_in(each.func.decode(), func):
            data.append([each.name, str(each.id)])
    return render_template('func_result.html', data = data, func = func)
    
# 路径搜索页面
@app.route('/path_search', methods = ['POST'])
def path_search():
    i, j = request.form['i'], request.form['j']
    Min_path = Dijkstra(MyData.spots, i, j, MyData.get_dist)
    All_paths = CountAllPath(MyData.spots, i, j)
    return render_template('paths.html', spots = MyData.spots, Min_path = Min_path, All_paths = All_paths, i=i, j=j)
        
# 网线铺设页面
@app.route('/net_work')
def net_work():
    result = Kruskal(MyData.spots)
    lenth = 0
    for each in result:
        lenth += each[0]
    return render_template('net_work.html', paths = result, spots = MyData.spots, lenth = lenth)
        
# 管理员登陆界面
@app.route('/admin_login', methods = ['POST', 'GET'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.form['username'] == 'bjfu' and request.form['password'] == 'bjfu':
            User.login(request.remote_addr)
            return redirect(url_for('admin_list'))
        return render_template('warning.html', info = u'账号或密码错误！', back = 'admin_login')

# 关于页面
@app.route('/info')
def info():
    return '<h1>:-)</h1>'

####----------后台-----------####
@app.route('/admin/list')
def admin_list():
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    spots_data = MyData.spots.values()
    return render_template('admin_list.html', spots = spots_data)
    
@app.route('/admin/add_spot', methods = ['GET', 'POST'])
def admin_add_spot():
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    if request.method == 'GET':
        return render_template('add_spot.html')
    else:
        spot_data = {}
        spot_data['name'] = request.form['name']
        spot_data['disc'] = request.form['disc']
        spot_data['func'] = request.form['func']
        p_id = MyData.add_a_spot(spot_data)
        if p_id == -1:
            return render_template('warning.html', info = u'此地点已经存在！', back = 'admin_list')
        try:
            f = request.files['pic']
            f.save(u'./tour_guide_system/static/{}.png'.format(spot_data['name']))
        except:
            pass
        return render_template('warning.html', info = u'添加成功！', back = 'admin_list')

@app.route('/admin/adjust_spot/<i>', methods = ['GET', 'POST'])
def admin_adjust_spot(i):
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    if request.method == 'GET':
        data = {}
        data['name'] = MyData.spots[i].name
        data['disc'] = MyData.spots[i].disc
        data['func'] = ''
        data['func'] += MyData.spots[i].func
        data['id'] = MyData.spots[i].id
        return render_template('adjust_spot.html', old_data = data)
    else:
        spot_data = {}
        spot_data['name'] = request.form['name']
        spot_data['disc'] = request.form['disc']
        spot_data['func'] = request.form['func']
        spot_data['id'] = i
        MyData.modify_a_spot(spot_data)
        try:
            f = request.files['pic']
            f.save(u'./tour_guide_system/static/{}.png'.format(spot_data['name']))
        except:
            pass
        return render_template('warning.html', info = u'修改成功！', back = 'admin_list')

@app.route('/admin/delete_spot/<i>')
def admin_delete_spot(i):
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    data = {}
    data['id'] = i
    MyData.delete_a_spot(data)
    return render_template('warning.html', info = u'删除成功！', back = 'admin_list')

@app.route('/admin/add_paths', methods = ['POST'])
def admin_add_paths():
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    try:
        data = {}
        data['id_0'], data['id_1'] = request.form['spot1'], request.form['spot2']
        data['dist'] = int(request.form['dist'])
        if data['id_0'] == data['id_1']:
            raise KeyboardInterrupt
        print MyData.add_a_path(data)
        return render_template('warning.html', info = u'添加成功！', back = 'admin_list')
    except:
       return render_template('warning.html', info = u'添加失败，请检查输入格式', back = 'admin_list')

@app.route('/admin/delet_path/<i>-<j>')
def admin_delete_path(i, j):
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    data = {}
    data['id_0'], data['id_1'] = i, j
    MyData.delete_a_path(data)
    return render_template('warning.html', info = u'删除成功！', back = 'admin_list')
