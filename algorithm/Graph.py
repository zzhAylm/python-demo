
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