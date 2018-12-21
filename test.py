# coding:utf-8
from tour_guide_system.src.data.data import *
from tour_guide_system.src.algorithm import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

id_s = MyData.locate('宿舍')
id_e = MyData.locate('教学楼')
result = CountAllPath(MyData.spots, id_s, id_e)
for each in result:
    for each_p in each:
        print MyData.spots[each_p].name.decode(),
    print