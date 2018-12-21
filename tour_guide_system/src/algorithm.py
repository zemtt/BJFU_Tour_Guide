# coding:utf-8

def KMP_in(str_1, str_2):
    """
    功能：
    用KMP算法，串模式匹配实现根据景点功能查询
    """
    def kmp_match(s, p):
        m, n, cur = len(s), len(p), 0
        next_ = next_list(p)
        while cur<=m-n:
            for i in range(n):
                if s[i+cur]!=p[i]:
                    cur += max(i - next_[i-1], 1)
                    break
            else:
                return True
        return False
    
    def next_list(p):
        prefix, postfix, ret = set(), set(), [0]
        for i in range(1,len(p)):
            prefix.add(p[:i])
            postfix = {p[j:i+1] for j in range(1,i+1)}
            ret.append(len((prefix and postfix or {''}).pop()))
        return ret
    
    return kmp_match(str_1, str_2)

def Kruskal(spots):
    """
    功能：
    用克鲁斯卡尔实现最小生成树构造，其中Edge_set用堆排序
    返回值：
    一个List包含最小生成树的所有边
    """

    Edges_set, result = [], []
    rest_spots = spots.keys()
    for spot in spots.keys():
        rest_spots.remove(spot)
        for path in spots[spot].paths:
            if path in rest_spots:
                Edges_set.append([spots[spot].paths[path], spot, path])
    Edges_set = Heap_sort(Edges_set)
    Vexset = { spots.keys()[i]:i for i in range(len(spots.keys())) }

    for edge in Edges_set:
        vex_1, vex_2 = Vexset[edge[1]], Vexset[edge[2]]
        if vex_1 == vex_2:
            continue
        result.append(edge)
        for each in Vexset:
            if Vexset[each] == vex_1:
                Vexset[each] = vex_2
    
    return result

def Heap_sort(edges):
    def Creat_a_heap():
        for i in range((len(edges)-1)/2, 0, -1):
            Heap_adjust(i, len(edges)-1)
    
    def Heap_adjust(s, m):
        rc = edges[s]
        j = 2*s
        while(j<m):
            if(j<m and edges[j][0]<edges[j+1][0]):
                j+=1
            if(rc[0]>edges[j][0]):
                break
            edges[s] = edges[j]
            s = j
            j*=2
        edges[s] = rc
    
    edges = [[0,0,0]]+edges
    Creat_a_heap()
    for i in range(len(edges)-1, 1, -1):
        edges[1], edges[i] = edges[i], edges[1]
        Heap_adjust(1,i-1)
    if edges[1][0] > edges[2][0]:
        edges[1], edges[2] = edges[2], edges[1]
    return edges[1:]

# 迪杰斯特拉查找最短路径
def Dijkstra(spots, start, end, get_dist):
    """
    功能：
    用深迪杰斯特拉法，算出起点与终点之间的最短路径

    参数：
    spots：School_data类里面的spots成员，数据类型为dict
    start：路径起点的id
    end：结束路径的id
    get_dist：School_data之中的函数，用于获取两点之间的距离

    返回值：
    一个List，第一个元素为路径总长度，第二个元素为路径经过的节点
    """
    path_dict = {}
    # 地图信息初始化
    rest_spots = spots.keys()
    rest_spots.remove(start)
    for spot in rest_spots:
        path_dict[spot] = [get_dist(start, spot), [start, spot]]

    # while循环
    while(rest_spots):
        min_dis, min_path, min_spot = None, None, None
        for spot in rest_spots:
            if not min_dis or path_dict[spot][0] < min_dis:
                min_spot, min_dis, min_path = spot, path_dict[spot][0],  path_dict[spot][1]
        rest_spots.remove(min_spot)
        if min_spot == end:
            break
        for spot in rest_spots:
            new_dist = get_dist(min_path[-1], spot) + min_dis
            if new_dist  >= path_dict[spot][0]:
                continue
            path_dict[spot] = [new_dist, min_path + [spot]]
            
    return path_dict[end]

# 所有路径的查找
def CountAllPath(spots, start, end):
    """
    功能：
    用深度优先法，使用栈来存储当前路径，来实现所有路径的计算

    参数：
    spots：School_data类里面的spots成员，数据类型为dict
    start：路径起点的id
    end：结束路径的id

    返回值：
    一个包含从start到end的所有路径的List，其中每一个路径信息包含两个元
    素，1、路径经过的所有节点 2、路径的总长度
    """
    result = []
    paths = [start]

    # 递归函数
    def count_next_step(dist):
        if paths[-1] == end:
            result.append([list(paths), dist])
        next_list = spots[paths[-1]].paths
        for spot in next_list:
            if spot not in paths:
                paths.append(spot)
                count_next_step(dist + next_list[spot])
                paths.pop()

    count_next_step(0)
    return result