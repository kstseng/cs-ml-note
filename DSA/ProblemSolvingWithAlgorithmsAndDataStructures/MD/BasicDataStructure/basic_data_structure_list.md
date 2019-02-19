# Basic Data Structure - List

## Outline

* [Linked List](#linked-list)
* [Unordered List](#unordered-list)
* [Ordered List](#ordered-list)

## Linked List

* 基本操作：

  * `add(item)`: 向 list 新增一個項
  * `remove(item)`: 從 list 刪除該項
  * `search(item)`: 搜尋 list 中的項目，並反回布林值
  * `isEmpty()`: 檢查 list 是否為空
  * `size()`: list 的項數
  * `append(item)`: 在 list 中的末尾新增一個項目
  * `index(item)`: 返回該項在 list 中的位置
  * `insert(pos, item)`: 在位置 pos 處新增此項
  * `pop()`: 刪除並回傳最後一項
  * `pop(pos)`: 刪除並回傳位置為 pos 的項

* 實現：

  * 利用 `Linked List` 來紀錄跟確保 `item` 的相對位置。在明確給定第一項的位置後，便可知道下一項。
  * `Linked List` 的基本構造是 `Node`

* 注意：在新增或是刪除時，調用的順序很重要。

  * 新增：
    * 從**頭項**新增項目：新項目相對於其他項目的位置不重要，因為都已經紀錄在 `getNext` 中。所以選擇要選最容易新增的位置；而 Linked List 都只有入口，所以選擇在頭項加入（`add` 方法可以簡單的將新結點放置在鏈表的頭。因為這是最簡單的訪問點。）
    * 要先將新項 `setNext` 為 `head`；再將 `head` 指向新項。若順序相反，則原先 head 之後的項都會因此斷掉。
  * 刪除：
    * 利用 `current` 和 `previous`。
    * 若還沒找到，在移動 `current` 和 `previous` 時，要先將 `previous` 移到 `current`，再把 `current` 移到下一個 Node。

## Unordered List

* 程式

```python
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
```

## Ordered List




