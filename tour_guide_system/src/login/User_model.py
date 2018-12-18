# coding:utf-8
import time

class User_data(object):
    def __init__(self):
        self.login_ip = ''
        self.login_time = 0
    
    def login(self, ip):
        self.login_ip = ip
        self.login_time = time.time()
    
    def is_login(self, ip):
        if ip == '127.0.0.1':
            return True
        if ip == self.login_ip and time.time() - self.login_time < 3600:
            self.login_time = time.time()
            return True
        return False