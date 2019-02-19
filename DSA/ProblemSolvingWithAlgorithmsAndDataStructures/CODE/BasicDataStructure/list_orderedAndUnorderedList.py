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

class OrderedList:
    """ 只在 search 跟 add 上與 UnorderedList 不同
    """
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.getNext()
        
        return count
    
    def search(self, item):
        """ 因為是排序，所以當 current 的值大於 item，在後面一定也找不到。
        """
        current = self.head
        found = False
        stop = False
        while not found and current != None and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        
        return found
    
    def add(self, item):
        """ 重要!
        """
        current = self.head
        previous = None
        stop = False
        ## 先找到要放置的節點
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        ## 找到後，再執行替換動作
        temp = Node(item)

        if previous == None:
            ## 要加入的 item 是最小，要擺在最前面
            ## ==> 像 Unordered List 的 add 一樣
            temp.setNext(self.head)
            self.head = temp
        else:
            ## 發生在 Ordered List 的中間
            temp.setNext(current)
            previous.setNext(temp)

def printList(alist):
    """ 印出 list 內的所有 item
    """
    current = alist.head
    while current != None:
        print(current.data)
        current = current.getNext()

def main():
    ## 
    ## Unorder List
    ##
    unordered_list = UnorderedList()
    unordered_list.add(10)
    unordered_list.add(20)
    unordered_list.add(4)
    unordered_list.add(7)
    print("Original unordered List")
    printList(unordered_list)

    assert unordered_list.search(5) == False
    unordered_list.size()
    unordered_list.remove(4)
    ##
    print("Unordered List after remove 4")
    printList(unordered_list)

    ##
    ## Unorder List
    ##
    ordered_list = OrderedList()
    ordered_list.add(10)
    ordered_list.add(20)
    ordered_list.add(30)
    ordered_list.add(40)
    print("Original ordered List")
    printList(ordered_list)

    assert ordered_list.search(5) == False
    ordered_list.add(25)
    ## 確認是否加入後仍是 Ordered List
    print("Ordered List after add 25")
    printList(ordered_list)
    
if __name__ == "__main__":
    main()
