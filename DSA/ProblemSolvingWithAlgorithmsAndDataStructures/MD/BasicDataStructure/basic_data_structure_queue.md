# Basic Data Structure - Queue

## Outline

* [Notes](#notes)
* [Implementation](#implementation)
    * [Queue Class](#queue-class)
    * [Simulation: Hot Potato (燙手山芋)](#hot-potato)
    * [Simulation: Printing Tasks (打印機)](#printing-tasks)

### Notes

1. 概念：先進先出 (First-In-First-Out, FIFO)，想像成**排隊**。添加新項的一端稱為 `Rear`，刪除項目的一端稱為 `Front`。
1. 應用：多個程序進行。
1. 基本操作：
    1. `enqueue(item)`: 將一個新項目 (item) 加入 Queue 的尾巴（新用戶要排隊）
    1. `dequeue()`: 刪除 (修改) Queue 的 Front 並回傳該項 (已被服務完的用戶)
    1. `isEmpty()`: Queue 是否為空
    1. `size()`: Queue 的項目數量
    

### Implementation

[code in github](https://github.com/kstseng/dsa-ml-tool-note/blob/master/DSA/ProblemSolvingWithAlgorithmsAndDataStructures/CODE/BasicDataStructure)

#### Queue Class

```python
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
```

#### Hot Potato

```python
```

#### Printing Tasks

```python
```
