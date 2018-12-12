#coding:utf-8

from flask import Flask, render_template, request
from src.data.school_data import School_data, Data
import json

app = Flask(__name__)

# 主页
@app.route('/')
def index():
    return render_template('index.html')

# 展示页面
@app.route('/spot/<i>')
def item(i):
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
        if each.name == name:
            i = each.id
    else:
        return render_template('warning.html',info=u'没有结果 !', back='#')
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
    
# 功能搜索页面
@app.route('/func_search')
def func_search(i):
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
    
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
def net_work(i):
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
        
# 管理员登陆界面
@app.route('/admin_login')
def admin_login(i):
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
            
# 关于页面
@app.route('/info')
def info(i):
    i = int(i)
    data = {}
    data['name'] = Data.points[i].name
    data['disc'] = Data.points[i].discription
    return render_template('spot.html',data = data)
    