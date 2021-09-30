import sys

# 迪科斯切
def dijkstra(start_point, graph):
    MAX = sys.maxsize
    n = len(graph)
    # 初始化各项数据，把dist[start]初始化为0，其他为无穷大
    dist = [99999999 for _ in range(n)]  # 路径长度
    pre = [-1 for _ in range(n)]  # 前驱pre
    s = [False for _ in range(n)]  # 集合S
    dist[start_point] = 0
    for i in range(n):
        minLength = MAX
        minVertex = -1
        for j in range(n):  # 线性时间找最小
            if not s[j] and dist[j] < minLength:
                minLength = dist[j]
                minVertex = j

        s[minVertex] = True
        # 从这个顶点出发，遍历与它相邻的顶点的边，计算特殊路径长度,更新dist和pre
        for edge in graph[minVertex]:
            if not s[edge[0]] and minLength + edge[1] < dist[edge[0]]:
                dist[edge[0]] = minLength + edge[1]
                pre[edge[0]] = minVertex
    return dist, pre


if __name__ == "__main__":

    data = [[1, 0, 8], [1, 2, 5], [1, 3, 10], [1, 6, 9], [2, 0, 1], [0, 6, 2], [3, 6, 5], [3, 4, 8], [0, 5, 4],
            [5, 6, 7], [5, 3, 8],
            [5, 4, 5]]  # 边集合（顶点，顶点，边权）
    n = 7  # 图的顶点数n\n"
    graph = [[] for _ in range(n)]  # 图的邻接表
    # 根据输入的图构建图的邻接表
    for edge in data:
        graph[edge[0]].append([edge[1], edge[2]])
        graph[edge[1]].append([edge[0], edge[2]])
    dist, pre = dijkstra(1, graph)
    print("dist=", dist)
    print("pre=", pre)
