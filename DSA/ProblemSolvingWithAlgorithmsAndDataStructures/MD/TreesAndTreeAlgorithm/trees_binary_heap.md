# Binary Heaps

- [Binary Heaps 簡介](#binary-heaps-introduction)
- [Binary Heaps 操作](#binary-heaps-operations)
- [Binary Heaps 實作](#binaryiheaps-implementation)

## Binary Heaps Introduction

先前利用列表進行排序和實現 `Stack` 中，**插入列表**是 `O(n)`，排序列表是 `O(nlong)`。而若使用一個經典方法是實作一個 `priority queue using binary heap`，讓 `enqueue` 和 `dequeue` 上是 `O(logn)`。

在實作上有兩種 `Binary Heaps`，以下會使用 `min heap`。

1. `min heap`：最小的 key 在最前面。
2. `max heap`：最大的 key 在最前面。

## Binary Heaps Operations

- `BinaryHeap()`: 建立新的 binary heap
- `insert(k)`: 增加一個新項
- `findMin()`: 返回具有最小 `key` 的項
- `delMin()`: 刪除最小 key 的項
- `isEmpty()`: 檢查 binary heap 是否為空
- `size()`: binary heap 的項數
- `buildHeap(list)`: 從 key list 建立一個新的 `heap`

## Binary Heaps Implementation

### 結構屬性

為了保持對數性能 (logarithmic performance)，必須保持樹的平衡，因此將使用完整二元樹。

#### 完整二元樹 (Complete Binary Tree)：

- 每個層都有其所有的節點，除了最底層。

- 因為 Complete，因此可使用一個 `list` 來表示。而不用 `Lists of list representation`或是 `Node and Reference`。

  - 若父節點的位置在 `p`，則其左子節點位在 `2p`，右子節點位在 `2p + 1`。

     ![](http://interactivepython.org/runestone/static/pythonds/_images/heapOrder.png)

  - 排序屬性：

    - 對於父節點中，每個子節點的 `key` **小於等於**父節點中的 `key`。

#### 實作

筆記：如何在 `insert` 和 `delMin` 中持續保持 `Binary Tree` 順序屬性。注意 `percUp` 和 `percDown` 兩個 method。

```python
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self, i):
        """
        從「下」到「上」檢查第 i 個元素是否符合「順序」結構
        """
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                ## 如果 leaf 的 key 大於其 parent 的 key
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i // 2

    def insert(self, k):
        """
        先加上值後，再檢查階層架構是否被破壞
        """
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
    
    def percDown(self, i):
        """
        從「上」到「下」檢查第 i 個元素是否符合「順序」結構
        
        附註：
            與 percUp 不同的是，若要交換時，
            先找出 child 中最小 key 的 index，
            再與 root 的 key 交換。
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
             
    def minChild(self, i):
        """
        回傳 "child" 中 key 比較小的那個 index
        """
        if i * 2 + 1 > self.currentSize:
            ## 當只有左子樹，直接回傳左子樹
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def delMin(self):
        """
        移除最小的值
        1. 先紀錄最小的值，且與最後一項交換，以方便 pop
        2. pop 最後一項，並檢查階層性
        """
        ## 先記錄最後一項
        rootval = self.heapList[1]
        ## 與最後一項交換
        self.heapList[1] = self.heapList[self.currentSize]
        ## 使用 pop
        self.heapList.pop()
        ## 記得更新 currentSize
        #self.currentSize = len(self.heapList)
        self.currentSize -= 1
        ## 從上到小檢查階層關係
        self.percDown(1)
        return rootval

    def buildHeap(self, alist):
        """
        對一個沒排序的 list 轉存成 Binary Heap

        步驟：
            1. 先直接存成 binary heap
            2. 再由最底層開始檢查，依序往上修正階層關係
        
        確保最小的節點一直往上走
        """
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        i = len(alist) // 2
        ## 從最底層開始依序檢查
        ## 確保最小節點能持續往上走
        while (i > 0):
            self.percDown(i)
            i -= 1

def main():
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])
```
