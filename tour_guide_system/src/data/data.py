# coding:utf-8
import random
ERROR = 1
OK = 0

# 生成长度为16的随机id
def make_a_id():
    seed, id_str = '0123456789abcdef', ''
    for each in random.sample(seed,16):
        id_str += each
    return id_str

class School_data(object):
    def __init__(self):
        self.spots = {}
    
    def dump(self):
        """
        功能：将文件保存为map.txt
        """
        spots_text, paths_text = '', ''

        spot_count, path_count = 0, 0
        for spot in self.spots.values():
            spots_text += spot.name+'\n'+spot.disc+'\n'+spot.func+'\n'
            for obj_id in spot.paths:
                paths_text += spot.name+' '+self.spots[obj_id].name+' '+str(spot.paths[obj_id])+'\n'
                self.spots[obj_id].paths.pop(spot.id)
                path_count += 1
            spot_count += 1
        with open('map.txt', 'w') as f:
            f.write(str(spot_count)+' '+str(path_count)+'\n')
            f.write(spots_text + paths_text)
    
    def locate(self, name):
        for spot in self.spots.values():
            if spot.name == name:
                return spot.id
        return ERROR

    def load(self):
        with open('map.txt','r') as f:
            text = f.readlines()
        spot_count, path_count = (int(each) for each in text[0].split(' '))
        line_count = 1
        for i in range(spot_count):
            data = {}
            data['name'] = text[line_count][:-1]
            data['disc'] = text[line_count+1][:-1]
            data['func'] = text[line_count+2][:-1]
            self.add_a_spot(data)
            line_count += 3
        for i in range(path_count):
            data = {}
            name_0, name_1, lenth = text[line_count][:-1].split(' ')
            lenth = int(lenth)
            data['id_0'], data['id_1'] = self.locate(name_0), self.locate(name_1)
            data['dist'] = lenth
            self.add_a_path(data)
            line_count+=1

    def add_a_spot(self, data):
        """
        参数：
        data：需要新添加的景点的数据。
        返回值：
        ERROR：添加失败，此名称景点已经存在
        OK：添加成功
        """
        for spot in self.spots.values():
            if data['name'] == spot.name:
                return ERROR
        spot = Spot_data()
        spot.set(data)
        self.spots[spot.id] = spot
        return OK
    
    def modify_a_spot(self, data):
        """
        参数：
        data：需要修改的景点的数据。
        返回值：
        ERROR：修改失败
        OK：添加成功
        """
        if data['id'] not in self.spots:
            return ERROR
        spot = self.spots[data['id']]
        spot.set(data)
        return OK
    
    def delete_a_spot(self, data):
        """
        参数：
        data：需要删除的景点的数据。
        """
        self.spots.pop(data['id'])    
    
    def add_a_path(self, data):
        """
        参数：
        data：需要添加的路径的数据。
        ERROR：添加失败，id不正确
        OK：添加成功
        """
        try:
            spot_0, spot_1 = self.spots[data['id_0']], self.spots[data['id_1']]
            spot_1.paths[data['id_0']] = data['dist']
            spot_0.paths[data['id_1']] = data['dist']
            return OK
        except:
            return ERROR
    
    def delete_a_path(self, data):
        """
        参数：
        data：需要添加的路径的数据。
        ERROR：添加失败，id不正确
        OK：添加成功
        """
        try:
            spot_0, spot_1 = self.spots[data['id_0']], self.spots[data['id_1']]
            spot_1.paths.pop(data['id_0'])
            spot_0.paths.pop(data['id_1'])
            return OK
        except:
            return ERROR

class Spot_data(object):
    def __init__(self):
        self.id = make_a_id()
        self.name = ''
        self.func = ''
        self.disc = ''
        self.paths = {}
    
    def set(self, data):
        self.name = data['name']
        self.disc = data['disc']
        self.func = data['func']

MyData = School_data()
MyData.load()