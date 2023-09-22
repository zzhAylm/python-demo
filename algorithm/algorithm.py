import unittest
# 实现邻接表
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    # 从这个顶点添加一个连接到另一个
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # 修改str
    def __str__(self):
        return str(self.id) + 'connectedTo' + str(
            [x.id for x in self.connectedTo])

    # 返回邻接表中的所有的项点
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    # 返回从这个顶点到作为参数顶点的边的权重
    def getweight(self, nbr):
        return self.connectedTo[nbr]



class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    # 增加顶点
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # 返回某个顶点的信息
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # 判断顶点是否在邻接表中
    def __contains__(self, n):
        return n in self.vertList

    # 增加边
    def addEdge(self, f, t, const=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], const)

    # 获取所有顶点
    def getVertices(self):
        return self.vertList.keys()

    # 使用迭代器返回所有的邻接表信息
    def __iter__(self):
        return iter(self.vertList.values())


from algorithm import Graph

if __name__ == '__main__':
    # 添加顶点
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    var = g.vertList
    print(var)
    # 添加边和权重
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    # 打印所有的边
    for v in g:
        # 获取所有顶点
        for w in v.getConnections():
            # 打印
            print("( %s , %s , %s)" % (v.getId(), w.getId(), v.getweight(w)))