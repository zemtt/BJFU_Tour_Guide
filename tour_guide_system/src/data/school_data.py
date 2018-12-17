# coding:utf-8
from pickle import dump, load
#import copy_reg

class School_data(object):
    def __init__(self):
        self.point_map = [
            [-1 for i in range(100)]
            for j in range(100)
        ]
        self.points = [School_spot(i) for i in range(100)]

    def save(self):
        with open('./tour_guide_system/src/data/school.dat', 'wb') as f:
            dump(self, f)

    # 添加一个景点
    def add_a_point(self, data):
        for point in self.points:
            if point.flag and point.name == data['name']:
                return -1
        for point in self.points:
            if point.flag:
                continue
            point.name, point.discription, point.function =  (
                data['name'],
                data['disc'],
                data['func']
            )
            point.flag = True
            self.save()
            return point.id
    
    # 修改一个景点
    def modify_a_point(self, data):
        point = self.points[data['id_']]
        point.name, point.discription, point.function =  (
            data['name'],
            data['disc'],
            data['function']
        )
        self.save()
    
    # 删除一个景点
    def delete_a_point(self, data):
        # 删除点信息
        point = self.points[data['id_']]
        point.flag = False
        # 删除边信息
        for i in range(100):
            self.point_map[i][data['id_']], self.point_map[data['id_']][i] = 0, 0
        self.save()

    # 查找一个景点
    def find_a_point_by_name(self, name):
        for point in self.points:
            if not point.flag:
                continue
            if point.name == name:
                return point.id
        return -1
    
    # 添加一条路径
    def add_a_path(self, data):
        id_0, id_1 = data['0'], data['1']
        self.point_map[id_0][id_1], self.point_map[id_1][id_0] = data['dist'], data['dist']
        self.save()
    
    # 删除一条路径
    def delete_a_path(self, data):
        id_0, id_1 = data['0'], data['1']
        self.point_map[id_0][id_1], self.point_map[id_1][id_0] = -1, -1
        self.save()

    def make_a_new_dat_file(self):
        self.add_a_point(
            {
                'name':u'图书馆',
                'disc':u'图书馆，是搜集、整理、收藏图书资料以供人阅览、参考的机构，早在公元前3000年就出现了图书馆，图书馆有保存人类文化遗产、开发信息资源、参与社会教育等职能。据《在辞典中出现的“图书馆”》说，“图书馆”一词最初在日本的文献中出现是1877年的事；而最早在我国文献中出现，当推《教育世界》第62期中所刊出的一篇《拟设简便图书馆说》，时为1894年。',
                'func':['学习', '借书', '咖啡']
            }
        )
        self.save()

class School_spot(object):
    def __init__(self,id_):
        self.id = id_
        self.name = ''
        self.function = []
        self.discription = ''
        self.flag = False

a = School_data()
#a.make_a_new_dat_file()
with open('./tour_guide_system/src/data/school.dat', 'rb') as f:
    Data = load(f)