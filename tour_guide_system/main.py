#coding:utf-8

from flask import Flask, render_template, request
from src.data.school_data import School_data, Data
import json
from flask_login import UserMixin
from src.login.User_model import User_data

app = Flask(__name__)

User = User_data()

# check登陆信息
def Check_login(ip):
    return User.is_login(ip)

# 主页
@app.route('/')
def index():
    return render_template('index.html')

# 展示页面
@app.route('/spot/<i>')
def spot(i):
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)

# 名称搜索页面
@app.route('/name_search', methods = ['POST'])
def name_search():
    name = request.form['name']
    for each in Data.points:
        if not each.flag:
            continue
        if each.name == name:
            i = each.id
            break
    else:
        return render_template('warning.html',info=u'没有结果 !', back='index')
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    data['func'] = Data.points[i].function
    return render_template('spot.html',data = data)
    
# 功能搜索页面
@app.route('/func_search', methods = ['POST'])
def func_search():
    func = request.form['func']
    data = []
    for each in Data.points:
        if not each.flag:
            continue
        if func in each.function:
            data.append([each.name, str(each.id)])
    return render_template('func_result.html', data = data, func = func)
    
# 路径搜索页面
@app.route('/path_search')
def path_search(i):
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
        
# 网线铺设页面
@app.route('/net_work')
def net_work():
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
        
# 管理员登陆界面
@app.route('/admin_login', methods = ['POST', 'GET'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.form['username'] == 'bjfu' and request.form['password'] == 'ilovebjfu':
            User.login(request.remote_addr)
            return render_template('warning.html', info = u'登陆成功！', back = 'admin_login')
        return render_template('warning.html', info = u'账号或密码错误！', back = 'admin_login')

# 关于页面
@app.route('/info')
def info():
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)

####----------后台-----------####
@app.route('/admin/list')
def admin_list():
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    pass

@app.route('/admin/spot/<i>')
def admin_spot(i):
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    pass
    
@app.route('/admin/paths')
def admin_paths():
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    pass

@app.route('/admin/path/<i>-<j>')
def admin_path(i, j):
    if not Check_login(request.remote_addr):
        return render_template('warning.html', info = u'请登陆管理员账号之后再操作！', back = 'admin_login')
    pass