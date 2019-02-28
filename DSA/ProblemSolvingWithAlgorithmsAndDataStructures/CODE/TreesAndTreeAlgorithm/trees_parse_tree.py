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

def main():
    fpexp = "( ( 10 + 5 ) * 3 )"
    pt = buildParseTree(fpexp)
    print('{} = {}'.format(fpexp, evaluate(pt)))
    print('result: '.format(postordereval(pt)))
    print(inorder(pt))
    print(printexp(pt))

main()
