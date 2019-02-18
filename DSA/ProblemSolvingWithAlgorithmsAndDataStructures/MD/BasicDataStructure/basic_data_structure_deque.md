# Basic Data Structure - Deque

## Outline

* [Notes](#notes)
* [Implementation](#implementation)
    * [Deque Class](#deque-class)
    * [Simulation: Hot Potato (燙手山芋)](#hot-potato)
    * [Simulation: Printing Tasks (打印機)](#printing-tasks)

### Notes

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
