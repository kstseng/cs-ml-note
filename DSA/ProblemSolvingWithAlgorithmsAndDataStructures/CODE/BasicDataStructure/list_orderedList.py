class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext
    
class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        ## 因為是 Unordered List，所以新 item 相對於對於已經在 list 中的其他項的位置不重要，
        ## 因此選擇將新 item 放在最容易放的位置。
        ##
        ## Linked List 只提供入口，因此最簡單加入新 item 的地方，便是在 Linked List 的頭部
        new_node = Node(item)
        ## 要先將 head 設為 new_node 的 next，才能去改 head
        ## 若以下兩行互換，則原先接在 head 後面的都沒辦法被訪問到
        new_node.setNext(self.head)
        self.head = new_node
    
    def size(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.getNext()
        
        return count
    
    def search(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
            
        return found
    
    def remove(self, item):
        """ 假設欲刪除的 item 存在於此 list => 先不考慮不存在的狀況
        """
        found = False
        current = self.head
        previous = None
        while not found:
            if current.getData() == item:
                found = True
            else:
                ## 要先把 previous 換成 current
                ## 才能把 current 移動到下個 node
                ## ==> 俗稱 inch-worming
                previous = current
                current = current.getNext()
        
        ## 搜索完成（且找到）
        ##
        ## 情況一：若欲刪除的是第一個項
        if previous == None:
            self.head = current.getNext()
        else:
            ## 其他情況：越過 current (刪除)
            ## 若欲刪除的是最後一項，仍適用
            previous.setNext(current.getNext())

def main():
    unordered_list = UnorderedList()
    unordered_list.add(10)
    unordered_list.add(20)
    unordered_list.add(4)
    unordered_list.add(7)

    assert unordered_list.search(5) == False
    unordered_list.size()
    unordered_list.remove(4)

if __name__ == "__main__":
    main()
