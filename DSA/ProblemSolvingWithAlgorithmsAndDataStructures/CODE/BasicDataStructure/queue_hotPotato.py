class Queue:
    """ 
    定義：假設總長為 n
        Rear: index 為 0
        Front: index 為 (n - 1)
    
    ==> 
        enqueue (入隊) 的複雜度為 O(n)
        dequeue (出隊) 的複雜度為 O(1)
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        """ 入隊
        """
        self.items.insert(0, item)

    def dequeue(self):
        """ 出隊
        """
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
def hotPotato(namelist, num):
    """ 約瑟夫問題
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    
    ## 當還存在至少兩個人時
    while simqueue.size() > 1:
        for i in range(num):
            ## 把排在 front 的人叫出來，並把它排到 rear
            ## (叫出來後重新排隊)
            item_to_dequeued = simqueue.dequeue()
            simqueue.enqueue(item_to_dequeued)
        ## 當執行 num 次，把 front 的人去除
        simqueue.dequeue()
    
    return simqueue.dequeue()

def main():
    namelist = ["Bill","David","Susan","Jane","Kent","Brad"]
    num = 7
    print(hotPotato(namelist, num))

if __name__ == "__main__":
    main()
