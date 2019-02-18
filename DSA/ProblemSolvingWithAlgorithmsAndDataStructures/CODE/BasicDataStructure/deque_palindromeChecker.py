class Deque:
    """
    從前面 (Front) 新增和刪除項是 O(1)
    從後面 (Rear) 新增和刪除項是 O(n)
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

def palchecker(aString):
    """
    """
    ## 把 aString 存入一個 Deque
    chardeque = Deque()
    for char in aString:
        chardeque.addFront(char)
    
    stillMatching = True
    ## 如果 deque 的長度大於 1 () => 字串可能為單數，eg: radar
    while chardeque.size() > 1 and stillMatching:
        front_char = chardeque.removeFront()
        rear_char = chardeque.removeRear()
        if front_char != rear_char:
            stillMatching = False
    
    return stillMatching


def main():
    assert palchecker('abcdcba') == True
    assert palchecker('radar') == True
    assert palchecker('aabb') == False

if __name__ == "__main__":
    main()