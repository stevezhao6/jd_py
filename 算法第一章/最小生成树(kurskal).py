def kruskal(edge_list,vertex):
    vertex_num = len(vertex)
    edge_num = len(edge_list)
    tree_mst = []
    if vertex_num <= 0 or edge_num < vertex_num - 1:
        return tree_mst
    edge_list.sort(key=lambda a:a[2])  # 按照边权由小到大排序
    group = [[i] for i in range(1,vertex_num+1)]    # 初始化,将图G的顶点看成n个孤立分支

    for edge in edge_list:
        for i in range(len(group)):
            if edge[0] in group[i]:
                m = i
            if edge[1] in group[i]:
                n = i
        if m != n:
            tree_mst.append(edge)
            group[m] = group[m] + group[n]
            group.remove(group[n])
    return tree_mst


if __name__ == "__main__":

    edge_list = [[1,2,6],[1,3,1],[1,4,5],[2,3,5],[2,5,3],[3,4,5],[3,6,4],[3,5,6],[4,6,2],[5,6,6]]
    vertex =[1,2,3,4,5,6]
    tree_mst =  kruskal(edge_list,vertex)
    for edge in tree_mst:
        print(edge)