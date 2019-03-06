# Graphs

- [詞彙與定義 (Vocabulary and Definitions)](#vocabulary-and-definitions)
- [圖的抽象數據類型 (The Graph Abstract Data Type)](#the-graph-abstract-data-type)
- [圖的表示 (Representations)](#graph-representations)
  - [Adjacency Matrix](#adjacency-matrix)
  - [Adjacency List](#adjacency-list)
- [圖的實現 (Graph Implementation)](#graph-implementation)

## Vocabulary and Definitions

### Terms

- 頂點 (Vertex)
  - 圖的基本組成之一。可以給頂點一個名稱 `key`。
  - 頂點可帶有其他訊息，稱這額外帶入的訊息為 `payload`。
- 邊 (Edge)
  - 圖的基本組成之一。當邊連接兩個頂點，表明他們之間存在關係
  - 邊可以是單向或是雙向。若圖中都是單向，則稱為有向圖（**directed graph**, or a **digraph**）。
- 權重 (Weight)
  - 邊可以加上權重。代表從一頂點到另一頂點的成本（`cost`）。
- 路徑 (Path)
  - 由邊所組成的頂點序列。
- 循環 (Cycle)
  - 在有向圖中，同一個頂點開始和結束的路徑。例如下圖的路徑（`V5`, `V2`, `V3`, `V5`）便是一個循環。
  - 沒有循環的圖稱為非循環圖（**acyclic graph**），一個**沒有循環**的**有向圖**，稱為 **directed acyclic graph (DAG)**。若問題可以被表示成 `DAG`，則可以解決幾個重要的問題。

### Define Graph

有了上述的定義，便可以定義**圖**。

`G = (V, E)`

- `G`：圖
- `V`：一組頂點
- `E`：一組邊
  - 每個邊由一個 `tuple` (`v`, `w`) 組成，其中 `v`, `w` 皆屬於 `V`。

##### 範例

`V = {V0, V1, V2, V3, V4, V5}`

`E = {(v0, v1, 5), (v1, v2, v4), (v2, v3, 9), (v3, v4, 7), (v4, v0, 1), (v0,v5,2),(v5,v4,8),(v3,v5,3),(v5,v2,1)}`

![](http://interactivepython.org/runestone/static/pythonds/_images/digraph.png)

## The Graph Abstract Data Type

- `Graph()`: 建立一個空的圖
- `addVertext(vert)`: 向此圖新增一個頂點的實體。
- `addEdge(fromVert, toVert)`: 對兩個頂點新增一個新的有向邊。
- `addEdge(fromVert, toVert, weight)`: 對兩個頂點新增一個新的有向權重邊。
- `getVertext(vertKey)`: 在圖中找到名為 `vertKey` 的頂點。
- `getVertices()`: 回傳圖中所有頂點的列表。
- `in`: 當執行 `vertext in graph`，若 `vertext` 在圖中，則回傳 `True`，否則 `False`。

## Graph Representations

### Adjacency Matrix

每一行和每一列表示圖中的頂點，而儲存在第 `v` 行和第 `w` 列的數值便代表是否存在從 `頂點 v` 到 `頂點 w` 的邊。

- 優點：簡單易懂。
- 缺點：當矩陣稀疏時，此種儲存方法效率很差。
- 適用情境：當`邊`的數量很大時。

![](http://interactivepython.org/runestone/static/pythonds/_images/adjMat.png)

### Adjacency List

用一個 `List` 儲存所有頂點。而每一項使用字典儲存該頂點與其他頂點之邊的權重。

- 優點：
  - 可有效地表示稀疏的圖
  - 允許直接透過頂點找到相鄰的頂點。

![](https://facert.gitbooks.io/python-data-structure-cn/7.%E5%9B%BE%E5%92%8C%E5%9B%BE%E7%9A%84%E7%AE%97%E6%B3%95/7.5.%E9%82%BB%E6%8E%A5%E8%A1%A8/assets/7.5.%E9%82%BB%E6%8E%A5%E8%A1%A8.figure4.png)

## Graph Implementation

建立兩個 `Class` 實作：

- 一個是 `Vertex`：用來表示每個頂點
- 另一個是 `Graph`：用來表示所儲存頂點的列表

```python
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
```