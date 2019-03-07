# Binary Search Trees

- [二元搜尋樹的簡介](#binary-search-tree-introduction)
- [二元搜尋樹的操作](#binary-search-tree-operations)
- [二元搜尋樹的實現](#binary-search-tree-implementation)
- [二元搜尋樹的分析](#binary-search-tree-analysis)

## Binary Search Tree Introduction

利用二元搜索樹中，利用**左子樹**的 `key` 小於**父節點**的 `key`，且**右子樹**的 key 大於**父節點**的 `key`來搜尋。這稱為 **BST 屬性**。

![](http://interactivepython.org/runestone/static/pythonds/_images/simpleBST.png)

## Binary Search Tree Operations

- `Map()`: 創建一個新的 `map`
- `put(key, val)`: 對 `map` 新增一個 `key-value pair`，如果該 `key` 已經存在，則以新值取代舊值。
- get(key)`: 傳回該 `key` 所對應的 value`，若不存在則傳為 `None`。
- `del`: 使用 `del map[key]`從 `map`刪除此 `key-value pair`。
- `len()`: 返回儲存在 `map` 中的 `key-value pair` 數量。
- `in`: 若給定的 `key` 在 `map`中，則返回 `True`。 

## Binary Search Tree Implementation

使用 `Node and Reference` 的表示方式來實現 BST。

將實現部分分成兩個 `Class`，一個是 `BinarySearchTree`，另一個是 `TreeNode`。

### 筆記

1. `findSuccessor`: 此處使用 `inorder successor`。亦即以 **inorder** 的順序進行 traversal 來尋找下一個 node。而某 `node ` 的 **Successor** 的位置有兩種可能。

   1. 若 Current Node 存在 Right Child，則 Current Node 下一個順序的 Node 是以 Current Node 的 Right Child 為 root，其 subtree 中最左的 Node。（也就是選擇大於 Current Node 中最小的 Node）。

   2. 若Current Node沒有 Right Child，則 Current Node 之下一個順序的 Node 是「以 Left Child 的身份尋找到的 ancestor」。（因為順著右節點往上找，都會是找到）

      1. 以 `H` 為例，沒有 right child，則往上找。
      2. 找到 `E`，但 `H` 是 `E` 的右子樹，因此在往上找。
      3. 找到 `B`，但 `E` 是 `B` 的右子樹，因此在往上找。
      4. 找到 `A`，此時 `B` 是 `A` 的左子樹，結束尋找。

      ![](https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Tree%20series/BinaryTree_fig/Traversal/f22.png?raw=true)

[圖片來源](http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html)

### 程式

```python
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        ## 存在 parent 且其 parent 的左子樹等於自身
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        ## 沒有 parent node
        return not self.parent
    
    def isLeaf(self):
        ## 沒有 child node
        return not (self.leftChild or self.rightChild)
    
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            ## 'self.leftChild = lc' 只是指派 self 的 leftChild
            ## 而 lc 的 parent 還沒有指派清楚
            ## 因此要多一步把 'lc' 的 parent 指向自己
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
 
class BinarySearchTree:
    ## 此 class 目的在提供 reference 指向 root (TreeNode)
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        ## 迭代器，用以尋遍整個 list
        return self.root.__iter__()
       
    def put(self, key, val):
        """
        """
        if self.root:
            ## 如果存在 root
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    
    def _put(self, key, val, currentNode):
        """
        """
        if key < currentNode.key:
            ## 往左邊走
            if currentNode.hasLeftChild():
                ## 往下遞移
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            ## 往右邊走
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)
    
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self, key, currentNode):
        """
        """
        if not currentNode:
            ## 節點不存在
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            ## 往左找
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            ## 往右找
            return self._get(key, currentNode.rightChild)
        else:
            ## 不可能發生
            pass
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __contain__(self, key):
        """
        重新改變了 'in' 操作
        """
        #if self._get(key, self.root):
        if self.get(key):
            return True
        else:
            return False
        
    def delete(self, key):
        """
        1. 只有 root 且 key 是要刪除的
        2. 只有 root 但 key 不是要刪除的
        3. general case
        """
        if self.size > 1:
            nodeToRemove = self.get(key)
            if nodeToRemove:
                ## 如果找到要移除的 node
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not found')
        elif self.size == 1:
            if self.root.key == key:
                self.root = None
                self.size -= 1
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, key not found')

    def __detitem__(self, key):
        self.delete(key)
    
    def remove(self, currentNode):
        """
        三個 case
        1. 要刪除的是 leaf
        """
        if currentNode.isLeaf():
            ## 如果是 leaf，直接取代為 None
            if currentNode == currentNode.parent.leftChild:
                ## 如果要刪除的 node 是左子葉
                currentNode.parent.leftChild = None
            else:
                ## 如果要刪除的 node 是右子葉
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            ## has one child
            if currentNode.hasLeftChild:
                if currentNode.isLeftChild():
                    ## current 是左子
                    ##
                    ## 把 current 的 parent 的左子，指向 current 的左子
                    currentNode.parent.leftChild = currentNode.leftChild
                    ## 把 current 的左子的 parent，指向 current 的 parent
                    currentNode.leftChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    ## current 是右子
                    ##
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    ## 是 root
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild)
            else: # current has rightChild
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)

    def findSuccessor(self):
        """
        ## inorder successor: 按照 inorder 順序找下一個
        """
        succ = None
        if self.hasRightChild():
            ## 有右子樹，則要找的是右子樹的最小 key
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    ## 若 current node 沒有 right child
                    ## 則 current node 的下一個順序是
                    ## 「以 left child 的身份尋找到的 ancestor」
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
    
    def findMin(self):
        """
        因為二元搜尋樹的設計
        所以最小值就是一直往左子樹找
        """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        """
        """
        if self.isLeaf():
            ## 如果是 leaf，直接取代為 None
            if self.isLeftChild():
                ## 如果是左子葉
                self.parent.leftChild = None
            else:
                ## 如果是右子葉
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    def __iter__(self):
        """
        中序
        """
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

def main():
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"

    print(mytree[6])
    print(mytree[2])    
```

## Binary Search Tree Analysis

以 `put` 方法為例，效能取決於 **Binary Tree 的高度**，也就是 `root` 和`最深 leaf` 的邊的數量。

若按照隨機分配新增 `key`，樹的高度會落在 $$log_{2}n$$。因為假設是隨機分佈 `key`，則會有一半小於 `root`，一半大於 `root`。而第 `d` 層（深度為 `d`）的節點數量是 $$2^d$$。

$$n = 2^0 + 2^1 + ... + 2^d = 2^{d+1}-1$$

$$d = O(log_2{n})$$

其他操作像是 `get`、`in` 和 `del` 同樣受到樹高影響。

且最壞狀況是，`put` 的複雜度是 `O(n)`。如下：

![](http://interactivepython.org/runestone/static/pythonds/_images/skewedTree.png)



#### 參考資料

- [Binary Tree: Traversal (尋訪)](http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html): 很精彩的介紹