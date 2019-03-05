# AVL Tree

## 前情提要

若樹非常不平衡，則 Binary Search Tree 的操作，如 `get` 或 `put` 會讓複雜度變高（$$O(log_2n)$$ to $$O(n)$$)。因此將介紹一種特殊的二元搜索樹，它會自動確保樹保持平衡。此類型的樹稱為 **AVL 樹** (以發明人命名)。

## Outline

- [平衡因子的定義 (The Definition of Balance Factor)](#the-definition-of-balance-factor)
- [AVL Tree 複雜度 (AVL Tree Performance)](#avl-tree-performance) 
- [AVL Tree 實作 (AVL Tree Implementation)](#avl-tree-implementation)

## The Definition of Balance Factor 

為了實現 AVL 樹，需要追蹤每個節點的**平衡因子** (`Balance Factor`)，方式則是透過查看每個節點的左右子樹的高度。定義上，將節點的平衡因子定義為左子樹的高度和右子樹的高度之差。

```shell
balanceFactor = height(leftSubTree) − height(rightSubTree)
```

若 `balanceFactor` 大於 0，則樹是左重 (`left heavy`)； `balanceFactor` 小於 0，則樹是右重 (`right heavy`)。 `balanceFactor` 等於 0，則樹是完美平衡 (`perfectly in balance`)。

如果 `balanceFactor` 是 `-1`, `0`, `1`，則定義此樹平衡。若在這範圍之外，則需要執行程序使之平衡。

![](http://interactivepython.org/runestone/static/pythonds/_images/unbalanced.png)

## AVL Tree Performance

在平衡條件下 (`Balance Factor` 為 `-1`, `0`, `1`)，舉左重樹為例，最壞的狀況如下，分別考慮高度為 `0`, `1`, `2`, `3` 的樹。

![](http://interactivepython.org/runestone/static/pythonds/_images/worstAVL.png)

對於節點的數量可歸納如下

1. `N1`, 高度為 `0`: `1` 個節點
2. `N2`, 高度為 `1`: `1 + 1 = 2` 個節點
3. `N3`, 高度為 `2`: `1 + 1 + 2 = 4` 個節點
4. `N4`, 高度為 `3`: `1 + 2 + 4 = 7` 個節點

因此可歸納在高度為 `h` 下的節點數量為 `N_h = 1 + N_(h-1) + N_(h-2)`。並藉由費波那契數列，可將原式改寫： `N_h = F_(h+2) - 1, h >= 1`。再藉由近似（黃金比例），可以得到下式：
$$
N_h=\frac{\phi^{h+2}}{\sqrt{5}}-1
$$
再經過重新排列跟推導後，可得
$$
h=1.44logN_h
$$
從推導得知，AVL 樹的高度等於樹中`節點數目 (資料數)`的**對數的常數倍**。因此其搜尋複雜度為 `O(logN)`。

**小結**：保持樹的平衡（Binary Search Tree --> AVL Tree）可以對效率有很大的改進

## AVL Tree Implementation

#### 重點

- [更新平衡因子](#update-balance)
- [樹的旋轉](#rotate)
- [旋轉前的確認](#check-before-rotate)

##### Update Balance

在新加入一個 Node （`put`）時，需要改變 Node 以及其 parent 的 Balance Factor。如果再更新 parent 的 Balance Factor 後，其 Balance Factor 不為 0，便需要再往上更新 Balance Factor。 不用往上更新的情況為：

1. 原先為 1（`left heavy`），然後添加右子樹 -> parent balanceFactor = 0
2. 或是原先為 -1（`right heavy`），然後添加左子樹 -> parent balanceFactor = 0

上述兩個狀況，都不會改變此 subtree 的高度。因此無需向上更新。

##### Rotate

分為左旋轉和右旋轉。

- 左旋轉

  ![](http://interactivepython.org/runestone/static/pythonds/_images/simpleunbalanced.png)

- 右旋轉

  ![](http://interactivepython.org/runestone/static/pythonds/_images/rightrotate1.png)

##### Check before Rotate

在旋轉時，會碰到一些狀況導致旋轉出現問題。

如碰到以下狀況，需要左旋轉

![](http://interactivepython.org/runestone/static/pythonds/_images/hardunbalanced.png)

左旋轉後如下

![](http://interactivepython.org/runestone/static/pythonds/_images/badrotate.png)

又會需要右旋轉，回到初始狀態，導致旋轉不會結束。因此在旋轉前要先確認此問題。

如以上例子，此樹需要左旋轉，先確認右子樹是否為 `right heavy`，若不是的話，要先對右子樹進行右旋轉。接著才對整棵樹進行左旋轉。

![](http://interactivepython.org/runestone/static/pythonds/_images/rotatelr.png)

#### 程式

相比於 `Binary Search Tree`，需要新增和修改的函數。

```python
def _put(self, key, val, currentNode):
    """
    和 BTS 的 _put 幾乎相同，只差在新增 Node 後，要 updateBalance
    """
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key, val, currentNode.leftChild)
        else:
            currentNode.leftChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.leftChild)
    else: # key > currentNode
        if currentNode.hasRightChild():
            self._put(key, val, currentNode.rightChild)
        else:
            currentNode.rightChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.rightChild)

def updateBalance(self, node):
    """
    """
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        ## 先檢查該 node 是否夠平衡
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
            node.parent.balanceFactor += 1
        elif node.isRightChild():
            node.parent.balanceFactor -= 1
        
        if node.parent.balanceFactor != 0:
            ## 若父節點的 balance factor 不為零
            ## 則持續往上(往 root) updateBalance
            ##
            ## 不用 update 的情況為
            ## 1. 原先為 1，然後添加右子樹 -> parent balanceFactor = 0
            ## 2. 或是原先為 -1，然後添加左子樹 -> parent balanceFactor = 0
            ## 上述兩情況都不會改變更上層的狀態。也因此不用更新
            self.updateBalance(node.parent)


    def rotateLeft(self, rotRoot):
        """
        左旋轉
        rotRoot: A
        newRoot: B

        Original:
          A
           \
            B
           / \
          C   D
        
        Rotate:
          B
         / \
        A   D
         \
          C
        """
        newRoot = rotRoot.rightChild
        ## 先把 newRoot 的 left child 關係處理好
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        ## 把 newRoot 的 parent 關係處理好
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        ## 重新連接彼此關係
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        ## 經由推導而來
        rotRoot.balanceFactor += 1
        newRoot.balanceFactor += 1
    
    def rotateRight(self, rotRoot):
        """
        右旋轉

        Original:
             A
            / 
           B
          / \
         C   D
        
        Rotate:
          B
         / \
        C   A
            /
           D
        """
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor -= 1
        newRoot.balanceFactor -= 1


    def rebalance(self, node):
        """
        EX: 若樹長得如下，需要進行左旋轉

        A
         \
          C
         /
        B

        但執行左旋轉後會變這樣

          C
         /
        A
         \
          B

        若再右旋轉，會再回到初始狀況。

        因此在旋轉之前要先判斷。
        """
        if node.balanceFactor < 0:
            ## 需要左旋轉
            if node.rightChild.balanceFactor > 0:
                ## 若右子樹是 left heavy
                ## 要先對右子樹右旋轉
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            ## 需要右旋轉
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node):
            else:
                self.rotateRight(node):
```