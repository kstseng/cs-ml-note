# Basic Data Structure - Stack

## Outline

* [Notes](#notes)
* [Implementation](#implementation)
    * [Stack Class](#stack-class)
    * [Balanced Parentheses (括號匹配)](#balanced-parentheses)
    * [General Infix-to-Postfix Conversion (十進位轉二進位)](#general-infix-to-postfix-conversion)
    * [Postfix Evaluation (中缀，前缀和后缀表達式)](#postfix-evaluation)


### Notes

1. 概念：後進先出 (Last-In-First-Out, LIFO) ，想像成**托盤**或是**一本本疊在桌上的書**。
1. 應用：瀏覽器的**返回鍵**。
1. 基本操作：
    1. `push(item)`: 將一個新項目 (item) 加入 Stack 的頂部 (放一個新托盤)
    1. `pop()`: 刪除 (修改) Stack 的頂部項目並回傳最頂項 (拿走一個托盤並取得該托盤的訊息)
    1. `peek()`: 取得 Stack 頂部項目的訊息
    1. `isEmpty()`: Stack 是否為空
    1. `size()`: Stack 的項目數量 (幾個托盤)
    

### Implementation

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/BasicDataStructure/stack.py)

#### Stack Class

建立一個 Stack Class

```python
class Stack:
    def __init__(self):
        ## 初始化一個空的 list 來存放 item
        self.items = []
    
    def push(self, item):
        ## 對 list 加上 item，且只要執行，不用回傳 stack，因為 append 會修改原 list。
        self.items.append(item)

    def pop(self):
        ## 刪除 list 的最後一項，並回傳該項數值
        return self.items.pop()

    def peek(self):
        ## 取得 list 最後的數值 (stack 的最頂項)
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        ## 確認 list 是否為空 
        return self.items == []

    def size(self):
        return len(self.items)

```

#### Balanced Parentheses

確定符號是否平衡。
* simpleParChecker: 符號只有 "("。
* parChecker: 可匹配多個符號，"([{"。

```python
def simpleParChecker(symbolString):
    """ 簡單括號匹配

    重要觀察：
        1. 從左到右，先只觀察 "("，亦即只紀錄 "("。
        2. 一但碰到 ")"，要先和最晚加入的 "(" 配對。
        3. 配對完成的條件為，
            1. 循遍字串的過程中，碰到 ")"，都有 "(" 可以被配對。
            2. 循遍完後，所有 "(" 都需要被配對。
        
    結論：
        適合使用 Stack 來存取資料。
    
    範例：
        symbolString = "(()())"
        1. 遇到 "("：存入
            ["("]
        2. 遇到 "("：存入
            ["(", "("]
        3. 遇到 ")"：要先從最晚加入的 ")" 配對
            ["(", "()"] --> ["("]
        4. 遇到 "("：存入
            ["(", "("]
        5. 遇到 ")"：要先從最晚加入的 ")" 配對
            ["(", "()"] --> ["("]
        6. 遇到 ")"：要先從最晚加入的 ")" 配對
            ["()"] --> []

    """
    ## 初始化一個 Stack
    s = Stack()
    balanced = True
    idx = 0
    while idx < len(symbolString) and balanced:
        symbol = symbolString[idx]
        if symbol == '(':
            ## 如果是 "("，把它 push 到 Stack 中
            s.push(symbol)
        else:
            ## 如果是 ")"
            ## 先確認該 Stack 是否為空（避免對空 list 執行 pop 會出錯）
            if s.isEmpty():
                ## 如果是 []，則不對稱，也因此會 break 此 while loop
                balanced = False
            else:
                ## 把最後塞入的 "(" 與該 ")" 配對
                s.pop()
        idx += 1
    
    if balanced and s.isEmpty():
        ## 會需要 s.isEmpty() 的原因，是因為可能 "(" 的數量多於 ")" 。
        ## eg: "(((())"
        ## 則 balanced 仍為 True，但卻有兩個 "(" 無法配對
        return True
    else:
        return False

def matches(open_char, close_char):
    """ 比對 open_char 和 close_char 是不是一對
    目的：把 "(" 推廣到不同符號
    """
    open_set = "{[("
    close_set = "}])"

    return open_set.index(open_char) == close_set.index(close_char)

def parChecker(symbolString):
    """ parChecker
    """
    s = Stack()
    balanced = True
    idx = 0
    while idx < len(symbolString) and balanced:
        symbol = symbolString[idx]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    ## 如果 top (open_char) 不是 symbol (close_char) 的配對，則對稱失敗
                    balanced = False
        idx += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
```

#### General Infix-to-Postfix Conversion

```python
test
```

#### Postfix Evaluation

```python
test
```
