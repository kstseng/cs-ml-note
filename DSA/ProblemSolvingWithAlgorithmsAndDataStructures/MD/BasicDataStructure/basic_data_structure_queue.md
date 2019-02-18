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

約瑟夫問題：把最前面的人叫出來後，重新排隊，該步驟執行 `num` 次後，把當前最前面的人去除。

```python
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
```

#### Printing Tasks

* 故事：假設影印機一個小時內，會有`10`位學生，每個學生需要影印`2`次。換言之

* 解析：3600 秒要服務 20 個任務 => 平均每 180 秒會有一個任務 ==> 每一秒有任務的機率為 1/180

* 虛擬碼：

對每一秒而言：
    * 如果影印機不忙，且有任務存在
        * 取出任務
        * 計算需等待的時間 (`當前秒數`與`任務被創建的時間戳記`的差)，並存進 list。
        * 根據任務的資訊，計算任務所需的時間
        
    * 若有任務的話 => 執行任務 => 剩餘時間減一秒
 
* 程式碼

```python
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        ## 完成某任務所剩餘的時間
        self.timeRemaining = 0
    
    def tick(self):
        ## 有任務在身
        if self.currentTask != None:
            ## 每經過一秒，除了時間點更新外，任務剩餘時間也少一秒
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        else:
             False
    
    def startNext(self, newtask):
        self.currentTask = newtask
        ## 計算此任務所需的時間
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 20)
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        ## 當前的時間 減去 該任務被創建的時間
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    watingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            ## 有沒有新任務產生
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        ## 如果影印機不忙，而且仍有任務
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            ## 則取出下一個任務
            nexttask = printQueue.dequeue()
            ## 計算所需的等待時間
            watingtimes.append(nexttask.waitTime(currentSecond))
            ## 計算此任務所需的執行時間，也就是所需的剩餘時間
            labprinter.startNext(nexttask)
        
        ## 如果有任務在身，則更新該任務所需的剩餘時間
        labprinter.tick()
    
    averageWait = sum(watingtimes) / len(watingtimes)
    print("Average Wait {} secs {} tasks remaining".format(averageWait, printQueue.size()))

def newPrintTask():
    ## 每一秒會有任務的機率是 1 / 180
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
```
