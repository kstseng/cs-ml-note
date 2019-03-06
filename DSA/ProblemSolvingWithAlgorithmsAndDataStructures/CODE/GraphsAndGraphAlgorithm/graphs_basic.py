class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        newVertext = Vertex(key)
        self.vertList[key] = newVertext
        return newVertext
    
    def getVertext(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
        
    def __contains__(self, key):
        return key in self.vertList
    
    def addEdge(self, f, t, cost=0):
        """
        f: from which vertext
        t: to which vertext
        """
        if f not in self.vertList:
            ## 不需要回傳的新 vertex
            _ = self.addVertex(f)
        if t not in self.vertList:
            _ = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight=cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

def main():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print('Graph\'s vertext')
    print(g.vertList)
    g.addEdge(0, 1, 5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print('({}, {})'.format(v.getId(), w.getId()))

main()