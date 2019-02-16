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

def main():
    print(baseConverter(107, 16))

if __name__ == '__main__':
    main()