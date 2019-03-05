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
                
