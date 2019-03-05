# Trees

樹的基本介紹與操作

- [簡介 Introduction](#introduction)
- [名稱與定義 Vocabulary and Definition](#vocabulary-and-definition)
- [樹的定義 Tree Definition](#tree-definition)
  - [節點與邊 Node and Edge](#node-and-edge)
  - [遞迴定義 Recursive Definition](#recursive-definition)
- [樹的表示式 Representation](#representation)
  - [列表表示式 List of Lists Representation](#list-of-lists-representation)
  - [節點表示式 Nodes and References](#nodes-and-references)
- 樹的應用
  - [剖析樹 Parse Tree](#parse-tree)
  - [樹的遍歷 Tree Traversals](#tree-traversals)

## Introduction

**Tree (樹)** 是用來描述具有**階層結構 (Hierarchical Structure)**的問題。

應用：文件系統 (File System)、網站架構 (`head`, `body`, ...)

## Vocabulary and Definition

最根本特徵：**在樹的結構裡，只有一個 root ( 樹根 )，並且不存在 cycle**。

- 基本結構
  - 節點 Node：
    - 樹的`基本結構`。
    - 可記載一些附加訊息。
  - 邊 Edge：
    - 樹的另一個`基本結構`。當節點之間以邊連結，代表他們之間存在關係。
    - 每個節點除了根以外，恰好從另一個節點以`傳入邊`連接，並可以具有多個`輸出邊`。
- 節點種類
  - 根 Root
    - 唯一**沒有** `輸入邊`的節點。
  - 子節點 (子嗣) Children, Descendant
    - 具有相同`輸入邊`的節點的集合，並且這些`輸入邊`屬於該節點的`輸出邊`，那這個`節點的集合`稱為該節點的`子節點`。
  - 父節點 Parent
    - 對子節點的輸入邊而言是輸出邊的節點。
    - **parent** —> **child**: 被指向者為 `child`，指向者為 `parent`。
  - 兄弟 Siblings
    - 同一個父節點的這些節點，彼此稱為兄弟節點。
  - 祖先 Ancestor
    - 以某一個節點，能夠以「尋找 parent 」的方式所能找到的節點，稱為該節點的祖先。
  - 葉節點 Leaf Node
    - 沒有子節點的節點
- 其他描述
  - 路徑 Path
    - 由`邊`連接`節點`的有序列表
  - 子樹 Subtree
    - 由父節點和該節點的所有後代組合的一組節點與邊。
  - 層數 Level
    - 從根節點到該點所經過的分之數目。
    - 定義：`根節點`的層數為 `0`。
  - 節點的高度 Height of Node
    - 此 Node 與最長路徑之後代 leaf node 的 edge 數
  - 樹的高度 Height of Tree
    - 樹中任何節點的最大層數。

## Tree Definition

### Node and Edge 

由一組節點和一組邊所組成。

定義：

- 樹的一個節點被指定為根節點。
- 除了根節點外，每個節點 `n` 通過一個其他節點 `p` 的邊連接。其中 `p` 稱為 `n` 的父節點。
- 從根節點遍歷到每個節點的路徑唯一。

![](http://interactivepython.org/runestone/static/pythonds/_images/treedef1.png)

### Recursive Definition

樹是由一個根節點和零個或多個子樹所組成。每個子樹也是一棵樹。 此為一個遞迴式的定義 (recursive definition of a tree)。

![](http://interactivepython.org/runestone/static/pythonds/_images/TreeDefRecursive.png)

## Representation

### List of Lists Representation

利用 `python` 的 `list` 來表示 **Tree**。

[Code](https://github.com/kstseng/dsa-ml-tool-note/tree/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/TreesAndTreeAlgorithm/trees_representation.py)

##### 範例

![](http://interactivepython.org/runestone/static/pythonds/_images/smalltree.png)

```python
myTree = ['a',           # root
    ['b',                # left subtree
        ['d', [], []],   # left subtree of 'b'
        ['e', [], []]],  # right subtree of 'b'
    ['c',                # right subtree
        ['f', [], []],   # left subtree of 'f'
        []]              # 'f' doesn't have right subtree
]
```

##### 實作

```python
def BinaryTree(r):
    # 節點、左子樹、右子樹
    return [r, [], []]

def insertLeft(root, newBranch):
    """
    """
    t = root.pop(1)
    if len(t) > 1:
        ## 原本的左節點不為空的列表
        ## 則以 newBranch 為根節點，並把本來的子節點接在 newBranch 的左子葉
        root.insert(1, [newBranch, t, []])
    else:
        ## 原本不存在左節點
        root.insert(1, [newBranch, [], []])

def insertRight(root, newBranch):
    """
    """
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]
```

### Nodes and References

使用節點的方式定義樹。

```python
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None
    
    def insertLeft(self, newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            ## 嫁接
            ## 把 newNode 做成樹
            t = BinaryTree(newNode)
            ## 把原先的左子樹接到 t 上
            t.leftchild = self.leftchild
            ## 把原先的左子樹替換成新接好的 t
            self.leftchild = t
        
    def insertRight(self, newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t
    
    def getRightChild(self):
        return self.rightchild
    
    def getLeftChild(self):
        return self.leftchild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
```

## Parse Tree

剖析樹可以用於表示句子或是數學表達式。

[Code](https://github.com/kstseng/dsa-ml-tool-note/tree/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/TreesAndTreeAlgorithm/tree_parse_tree.py)

- 句子組成

![](http://interactivepython.org/runestone/static/pythonds/_images/nlParse.png)

- 數學表達式：樹的層次結構可以容易了解整個表達式的求值順序。

![](http://interactivepython.org/runestone/static/pythonds/_images/meParse.png)

以下講針對數學表達式進行介紹：

- 如果從數學表達式建構剖析樹
- 如何評估儲存在剖析樹中的表達式
- 如何從剖析樹恢復原始數學表達式

##### 步驟

1. 能針對一串運算式，建立樹狀結構。
2. 能對於樹狀結構，遞迴的計算，然後得到最終結果。

##### 程式

```python
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    """
    fpexp = "( ( 10 + 5 ) * 3 )"
    pt = buildParseTree(fpexp)

    """
    fplist = fpexp.split()
    ## 用來儲存父節點
    ## parent stack
    pStack = Stack()
    ## 因為 Class() 是傳址 (reference type) 
    ## 所以 eTree 和 currentTree 會是同一個 address
    ## 因此對 currentTree 所做的操作，會同樣影響 eTree！
    ##
    ## 附註：int, ... 是傳值 (value type)
    eTree = BinaryTree('')
    ## pStack: 紀錄父節點
    pStack.push(eTree)
    ## 傳址 (reference type)
    currentTree = eTree

    operator = ["+", "-", "*", "/"]
    not_numbers = operator + ['(', ')']
    for i in fplist:
        if i == "(":
            ## 插入左子樹，並將 current 移到左子樹
            ## 此時 eTree 亦同樣插入左子樹
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in not_numbers:
            ## 如果是數字
            ## 則把該節點的值設定為 i
            ## 並利用 pStack 退回到該節點的父節點
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in operator:
            ## 如果是運算子
            ## 則設定該節點為運算子後
            ## 插入右子樹
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":
            ## 如果是 ")"
            ## 再往上退到該節點的父節點
            currentTree = pStack.pop()
        else:
            raise ValueError
    
    return eTree

def evaluate(parseTree):
    """
    用遞迴去取出值
    """
    opers = {
        '+': operator.add, 
        '-': operator.sub, 
        '*': operator.mul, 
        '/': operator.truediv
    }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        ## 若左子樹與右子樹都存在
        ## 則先找出 operator
        ## 再針對左子樹和右子樹，遞迴得呼叫 evaluate
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        ## Base Case!
        ## 直到某個節點的左子樹或右子樹任一不存在
        ## （以此範例而言，對於一個節點而言，左子與右子只會同時存在，或同時不存在）
        ## 代表已經到 leaf node，也就是數字
        ## 則直接回傳該數字
        return parseTree.getRootVal()
```

## Tree Traversals

訪問樹的三種方式（**根**的順序）

- 前序 preorder：

  - 順序：`根節點` —> `左子樹` —> `右子樹`

  - 應用：某些情境下提供正確的遍歷路徑。例：書本章節

    ![](http://interactivepython.org/runestone/static/pythonds/_images/booktree.png)

- 中序 inorder：

  - 順序：`左子樹` —> `根節點` —> `右子樹`
  - 應用：印出剖析樹

- 後序 postorder：

  - 順序：`左子樹` —> `右子樹` —> `根節點`
  - 應用：計算剖析樹

```python
def preorder(tree):
    """
    前序：
    根節點 —> 左子樹 —> 右子樹
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    """
    後序：
    左子樹 —> 右子樹 —> 根節點
    """
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def postordereval(tree):
    """
    """
    opers = {
        '+': operator.add, 
        '-': operator.sub, 
        '*': operator.mul, 
        '/': operator.truediv
    }
    if tree:
        ## 先取得左子樹與右子樹的結果
        res_l = postordereval(tree.getLeftChild())
        res_r = postordereval(tree.getRightChild())
        if res_l and res_r:
            ## 若左與右皆存在（不為 None）
            ## 則進行運算
            return opers[tree.getRootVal()](res_l, res_r)
        else:
            ## 若左與右至少一個存在（以此 case 為皆不存在）
            ## 則回傳 root value
            return tree.getRootVal()

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    """
    利用中序印出計算式（包含括號）
    左子樹 —> 根節點 —> 右子樹
    """
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal
```