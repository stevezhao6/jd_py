import sys

def prim_mst(graph,vertexs):
    ulist = []
    ulist.append(vertexs[0])    # 集合U
    tree_list = []  # 最小生成树
    closest = []    # closest[i]表示生成树集合中与点i最近的点的编号
    lowcost = []    # lowcost[i]表示生成树集合中与点i最近的点构成的边最小权值,-1表示i已经在生成树集合中

    lowcost.append(-1)
    closest.append(0)
    n = len(vertexs)
    for i in range(1,n): #初始化closest数组和lowcost数组
        lowcost.append(graph[0][i])
        closest.append(0)
    sum = 0
    for _ in range(1,n): # n-1次贪心选择
        minid = 0 # 记录V-U中顶点最近的U中的顶点编号
        min = sys.maxsize
        for j in range(1,n):  # 寻找每次插入生成树的权值最小lowcost
            if(lowcost[j]!=-1 and lowcost[j]<min):
                 minid = j
                 min = lowcost[j]
        ulist.append(vertexs[minid])
        tree_list.append([vertexs[closest[minid]],vertexs[minid],lowcost[minid]])
        sum+=min
        lowcost[minid] = -1
        for j in range(1,n):  # 更新插入结点后lowcost数组和closest数组值
            if(lowcost[j] != -1 and lowcost[j] > graph[minid][j]):
                lowcost[j] = graph[minid][j]
                closest[j] = minid
    return sum,tree_list

if __name__=='__main__':
    graph = [[0, 54, 32, 7, 50, 60], [54, 0, 21, 58, 76, 69], [32, 21, 0, 35, 67, 66],
              [7, 58, 35, 0, 50, 62], [50, 76, 67, 50, 0, 14], [60, 69, 66, 62, 14, 0]]
    vertex = ['A','B','C','D','E','F']
    sum,tree_list = prim_mst(graph,vertex)
    for edge in tree_list:
        print(edge[0]+"--"+edge[1]+"   权:"+str(edge[2]))
print("树的耗费：",sum)
