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
        
def main():
    toStr(10, 2)
    toStrStack(10, 2)

if __name__ == "__main__":
    main()
