# coding:utf-8
from tour_guide_system.src.data.data import *
from tour_guide_system.src.algorithm import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

id_s = MyData.locate('主楼')
id_e = MyData.locate('图书馆')
print MyData.spots[id_s].paths
result = CountAllPath(MyData.spots, id_s, id_e)
for each in result:
    for each_p in each[0]:
        print MyData.spots[each_p].name.decode(),
    print each[1]

result = Dijkstra(MyData.spots, id_s, id_e, MyData.get_dist)
for each in result[1]:
    print MyData.spots[each].name.decode(),
print result[0]
print
lenth = 0
result = Kruskal(MyData.spots)
for each in result:
    lenth += each[0]
    print MyData.spots[each[1]].name.decode(), MyData.spots[each[2]].name.decode(), each[0]

print lenth