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

