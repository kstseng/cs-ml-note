# Recursion

## Outline
* [遞歸三定律](#the-three-laws-of-recursion)
* [暖身小範例](#simple-problem)
 * [計算整數列表和](#calculating-the-sum-of-a-list-of-numbers)
 * [整數轉換為任意進位字串符](#converting-an-integer-to-a-string-in-any-base)
* [遞迴視覺化 - 烏龜](#recursion_visualization)
 * [螺旋](#draw-sprial)
 * [樹](#tree)
* [Sierpinski Triangle](#sierpinski-triangle)

## The Three Laws of Recursion

1. 遞迴算法必須要有基本情況。(A recursive algorithm must have a base case.)
2. 遞迴算法必須改變其狀態，並向基本情況靠近。(A recursive algorithm must change its state and move toward the base case.)
3. 遞迴算法必須以遞迴方式呼叫自身。(A recursive algorithm must call itself, recursively.)

## Simple Problem

#### Calculating the Sum of a List of Numbers
計算整數列表之和

[Github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/Recursion/recursion_sum_of_list.py)

* `For loop`

```python
def listsumLoop(numList):
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    
    return total
```

* `Recursion`

```
listsum(numList) = first(numList) + rest(numList)
```

```python
def listsumRecursion(numList):
    """ 
    """
    if len(numList) == 1:
        ## base case (函數的「例外條款」)
        return numList[0]
    else:
        total = numList[0] + listsumRecursion(numList[1:])

    return total
```


### Converting an Integer to a String in Any Base
整數轉換為任意進位字串符

[Github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/Recursion/recursion_converting_int_to_str.py)

* 遞迴

```python
def toStr(n, base):
    """
    範例：

    n = 769;  base = 10
    769 / 10 = 76 ... 9
    76  / 10 = 7  ... 6
    7   < 10      ==> 7

    ==> '769'

    """
    convertString = "0123456789ABCEDF"
    if n < base:
        ## base case
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
```

* 利用 Stack 存取

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def toStrStack(n, base):
    """
    """
    rStack = Stack()

    convertString = "0123456789ABCEDF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    
    return res
```

### Recursion Visualization

先不要執行，去想想看會怎麼畫。

[Github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/Recursion/recursion_turtle.py)

#### Draw Sprial

```python
import turtle

def drawSprial(myTurtle, lineLen):
    """
    """
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(45)
        drawSprial(myTurtle, lineLen - 5)

## run
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

drawSprial(myTurtle, 100)
myWin.exitonclick()

```

#### Tree

思考方式：從 base case 往回想。

* `branchLen <= 5`: 長度不足 `5`：停留原地。
* `前一次呼叫`：
 * 往前走 `branchLen`
 * 右轉 20 度並停留原地
 * 左轉 40 度停留原地，
 * 退回起始點


```python
import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        ## 先右轉 20 度
        t.right(20)
        tree(branchLen - 15, t)
        ## 再左轉 40 度
        t.left(40)
        tree(branchLen - 15, t)
        ## 再回到原先角度
        t.right(20)
        ## 退回到原先的起始點
        t.backward(branchLen)

## run
t = turtle.Turtle()
myWin = turtle.Screen()
## 預設是面向右邊
## 因此把他左轉 90 度
t.left(90)
tree(75, t)
```

#### Sierpinski Triangle

