# coding:utf-8

def KMP():
    """
    KMP算法，串模式匹配实现根据景点功能查询
    """
    pass

def Kruskal():
    """
    实现最小生成树构造
    """
    pass

def CountAllPath(points, start, end):
    result = []
    paths = [start]
    dists = 0

    # 递归函数
    def count_next_step():
        if paths[-1] == end:
            result.append(list(paths))
        next_list = points[paths[-1]].paths
        for spot in next_list:
            if spot not in paths:
                paths.append(spot)
                count_next_step()
                paths.pop()

    count_next_step()
    return result