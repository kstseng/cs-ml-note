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


def main():
    print("[TEST] infixToPostfix")
    assert infixToPostfix("( A + B ) * ( C + D )") == 'AB+CD+*'
    assert infixToPostfix("( A + B ) * C") == 'AB+C*'
    assert infixToPostfix("A + B * C") == 'ABC*+'

    print("[TEST] postfixEval")
    print(postfixEval('7 8 + 3 2 + /'))

if __name__ == '__main__':
    main()

