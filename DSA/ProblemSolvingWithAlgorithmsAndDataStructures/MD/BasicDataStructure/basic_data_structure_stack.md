# Basic Data Structure - Stack

## Outline

* [Notes](#notes)
* [Implementation](#implementation)
    * [Stack Class](#stack-class)
    * [Balanced Parentheses (括號匹配)](#balanced-parentheses)
    * [Converting Decimal Numbers to Binary Numbers (十進位轉二進位)](#converting-decimal-numbers-to-binary-numbers)
    * [Infix, Prefix and Postfix Expressions (中缀、前缀和后缀表達式)](#infix-prefix-and-postfix-expressions)


### Notes

1. 示意圖
    ```
    [item_1, item_2, item_3, ..., item_n] <== Top
    ```
1. 概念：後進先出 (Last-In-First-Out, LIFO) ，想像成**托盤**或是**一本本疊在桌上的書**。
1. 應用：瀏覽器的**返回鍵**。
1. 基本操作：
    1. `push(item)`: 將一個新項目 (item) 加入 Stack 的頂部 (放一個新托盤)
    1. `pop()`: 刪除 (修改) Stack 的頂部項目並回傳最頂項 (拿走一個托盤並取得該托盤的訊息)
    1. `peek()`: 取得 Stack 頂部項目的訊息
    1. `isEmpty()`: Stack 是否為空
    1. `size()`: Stack 的項目數量 (幾個托盤)
    

### Implementation

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/BasicDataStructure)

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

#### Converting Decimal Numbers to Binary Numbers

十進位轉二進位

* 筆記：連續除法

```
13 = 1 + 2(6) = 
     1 + 2(0 + 2(3)) = 
     1 + 2(0 + 2(1 + 2(1))) = 
     1*2^0 + 0*2^1 + 1*2^2 + 1*2(3)

==> 1101    
```

* 程式

```python
def divideBy2(decNumber):
    """
    概念：最先除 2 所得的餘數，再建立二進位字串的時候，是最後加入（建立字串時為由左至右）
    """
    remainder_stack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remainder_stack.push(rem)
        decNumber = decNumber // 2
    
    ## 建立 binary string
    bin_string = ""
    while not remainder_stack.isEmpty():
        bin_string += str(remainder_stack.pop())
    
    return bin_string


def baseConverter(decNumber, base):
    """
    """
    if base < 2 or base > 16:
        raise ValueError('base should between 2 and 16')

    digits = "0123456789ABCDEF"
    remainder_stack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remainder_stack.push(rem)
        decNumber = decNumber // base
    
    bin_string = ""
    while not remainder_stack.isEmpty():
        bin_string += digits[remainder_stack.pop()]
    
    return bin_string
```

#### Infix, Prefix and Postfix Expressions

中綴、前綴與後綴表達式。
此處只練習**中綴轉後綴**與**後綴求值**。

* 筆記

    * 中綴轉後綴：由於運算符號有可能因為優先次序不同，而需要反轉，便可利用Stack 的特性，讓最頂項始終是最近保存的運算符號。參考 `A * B + C * D` 的運算過程。
    * 後綴求值：由於是用後綴表達式，在碰到運算符號時，最靠近運算符號的兩個數，也就是`後`加入的兩個數要`先`進行運算。因此使用 Stack。

* 程式

```python
def infixToPostfix(infixexpr):
    """ 中綴轉後綴
    infixexpr = "A * B + C * D"

    範例：
    
    1. 
        infixexpr = A * B + C

        | current | postfixList | opStack |
        |---------|-------------|---------| 
        | A       | A           | []      |
        | *       | A           | [*]     |
        | B       | AB          | [*]     |
        | +       | AB*         | [+]     |
        | C       | AB*C        | [+]     |

        ==> AB*C+

    2. 
        infixexpr = (A + B) * C

        | current | postfixList | opStack |
        |---------|-------------|---------| 
        | (       |             | [(]     |
        | A       | A           | [(]     |
        | +       | A           | [(, +]  |
        | B       | AB          | [(, +]  |
        | )       | AB+         | []      |
        | *       | AB+         | [*]     |
        | C       | AB+C        | [*]     |

        ==> AB+C*

    3. 
        infixexpr = A * B + C * D

        | current | postfixList | opStack |
        |---------|-------------|---------| 
        | A       | A           |         |
        | *       | A           | [*]     |
        | B       | AB          | [*]     |
        | +       | AB*         | [+]     |
        | C       | AB*C        | [+]     |
        | *       | AB*C        | [+, *]  |
        | D       | AB*CD       | [+, *]  |

        ==> AB*CD*+
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            ## 假設是字母或是數字，則直接 append 
            postfixList.append(token)
        elif token == '(':
            ## 把 "(" 記起來，以便紀錄當遇到 ")" 時，需操作所有在括弧內的運算。
            opStack.push(token)
        elif token == ')':
            ## 把屬於這組括弧內的操作清空，直到遇到最上層的右括號為止
            ## (利用最上層的右括弧作為停止點)
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            ## 基本運算符號
            while not opStack.isEmpty() and (prec[opStack.peek()] >= prec[token]):
                ## 若當前的 token 順位比 opStack 中的 pop 操作符來得小，
                ## 則需要先把 opStack 的 pop item 先放到 postfixList 中
                ## ==> 代表先進行 opStack 優先次序高的操作
                ##
                ## eg: A * B + C
                ## 當 token 是 '+'，而 top token 是 "*"
                ## 則需要先操作 top token ==> 把 '*' 加入 postfixList
                postfixList.append(opStack.pop())
            opStack.push(token)
        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    return "".join(postfixList)

def postfixEval(postfixExpr):
    """ 後綴求值
    """
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            ## 一但碰到運算符號，則取 Stack 最後兩個數字進行運算
            ## 然後再附加回原來的 stack，以便做後續的運算
            topOperand = operandStack.pop()
            secondOperand = operandStack.pop()
            result = doMath(token, topOperand, secondOperand)
            operandStack.push(result)
    return operandStack.pop()

def doMath(token, operand1, operand2):
    """
    """
    if token == "+":
        return operand1 + operand2
    elif token == "-":
        return operand1 - operand2
    elif token == "*":
        return operand1 * operand2
    elif token == "/":
        return operand1 / operand2
    else:
        ValueError("Token is not recognizable.")
```
