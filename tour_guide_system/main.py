#coding:utf-8

from flask import Flask, render_template, request
app = Flask(__name__)

# 主页
@app.route('/search')
@app.route('/')
def index():
    return render_template('index.html')