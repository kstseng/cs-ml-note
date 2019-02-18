import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
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

def main():
    for i in range(10):
        simulation(3600, 5)

if __name__ == "__main__":
    main()