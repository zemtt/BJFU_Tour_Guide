# coding:utf-8
from data import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

a = School_data()
data_1 = {
    'name':u'图书馆',
    'disc':u'图书馆，是搜集、整理、收藏图书资料以供人阅览、参考的机构，早在公元前3000年就出现了图书馆，图书馆有保存人类文化遗产、开发信息资源、参与社会教育等职能。据《在辞典中出现的“图书馆”》说，“图书馆”一词最初在日本的文献中出现是1877年的事；而最早在我国文献中出现，当推《教育世界》第62期中所刊出的一篇《拟设简便图书馆说》，时为1894年。',
    'func':u'学习、借书、咖啡'
}
data_2 = {
    'name':u'教学楼',
    'disc':u'图书馆，是搜集、整理、收藏图书资料以供人阅览、参考的机构，早在公元前3000年就出现了图书馆，图书馆有保存人类文化遗产、开发信息资源、参与社会教育等职能。据《在辞典中出现的“图书馆”》说，“图书馆”一词最初在日本的文献中出现是1877年的事；而最早在我国文献中出现，当推《教育世界》第62期中所刊出的一篇《拟设简便图书馆说》，时为1894年。',
    'func':u'学习、借书、咖啡'
}
data_3 = {
    'name':u'宿舍',
    'disc':u'图书馆，是搜集、整理、收藏图书资料以供人阅览、参考的机构，早在公元前3000年就出现了图书馆，图书馆有保存人类文化遗产、开发信息资源、参与社会教育等职能。据《在辞典中出现的“图书馆”》说，“图书馆”一词最初在日本的文献中出现是1877年的事；而最早在我国文献中出现，当推《教育世界》第62期中所刊出的一篇《拟设简便图书馆说》，时为1894年。',
    'func':u'学习、借书、咖啡'
}
data_4 = {
    'name':u'食堂',
    'disc':u'图书馆，是搜集、整理、收藏图书资料以供人阅览、参考的机构，早在公元前3000年就出现了图书馆，图书馆有保存人类文化遗产、开发信息资源、参与社会教育等职能。据《在辞典中出现的“图书馆”》说，“图书馆”一词最初在日本的文献中出现是1877年的事；而最早在我国文献中出现，当推《教育世界》第62期中所刊出的一篇《拟设简便图书馆说》，时为1894年。',
    'func':u'学习、借书、咖啡'
}
a.add_a_spot(data_1)
a.add_a_spot(data_2)
a.add_a_spot(data_3)
a.add_a_spot(data_4)
id_a, id_b, id_c, id_d = (
    a.locate(data_1['name']),
    a.locate(data_2['name']),
    a.locate(data_3['name']),
    a.locate(data_4['name'])
)
a.add_a_path(
    {
        'id_0':id_a,
        'id_1':id_b,
        'dist':100
    }
)
a.add_a_path(
    {
        'id_0':id_c,
        'id_1':id_d,
        'dist':200
    }
)
a.dump()