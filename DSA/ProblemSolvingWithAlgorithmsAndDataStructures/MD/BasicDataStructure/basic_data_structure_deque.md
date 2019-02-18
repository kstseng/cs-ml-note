# Basic Data Structure - Deque

## Outline

* [Notes](#notes)
* [Implementation](#implementation)
    * [Deque Class](#deque-class)
    * [Palindrome-Checker (迴文檢查)](#palindrome-checker)

### Notes

1. 示意圖
    ```
    Rear ==> [item_1, item_2, item_3, ..., item_n] <== Front
    ```
1. 概念：不限制新增或刪除資料的方式 => 可從 front 新增或刪除資料，亦可從 rear 新增或刪除資料，
1. 應用：
1. 基本操作：
    1. `addFront(item)`: 將一個新項目 (item) 加入 deque 的首部（front）
    1. `addRear(item)`: 將一個新項目 (item) 加入 deque 的尾部（rear）
    1. `removeFront()`: 刪除首項，deque 被修改
    1. `removeRear()`: 刪除尾項，deque 被修改
    1. `isEmpty()`: deque 是否為空
    1. `size()`: Queue 的項目數量
    

### Implementation

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/BasicDataStructure)

#### Deque Class

複雜度：
* 從前面 (Front) 新增和刪除項是 O(1)
* 從後面 (Rear) 新增和刪除項是 O(n)

```python
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
        return len(self.size)
```

#### Palindrome-Checker

迴文檢查：正著念和反著念都是相同的句子

例如：`上海自來水來自海上`、`abcdcba`、`radar`。

概念：把字串存入 Deque 後，比較 `front` 和 `rear` 是否相同。


```python
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
```