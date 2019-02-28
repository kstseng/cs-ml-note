##
## List of Lists Representation
##
'''
example
myTree = ['a',           # root
    ['b',                # left subtree
        ['d', [], []],   # left subtree of 'b'
        ['e', [], []]],  # right subtree of 'b'
    ['c',                # right subtree
        ['f', [], []],   # left subtree of 'f'
        []]              # 'f' doesn't have right subtree
]
'''
'''
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
'''

##
## Nodes and References
##
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

def main():
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())    

main()
