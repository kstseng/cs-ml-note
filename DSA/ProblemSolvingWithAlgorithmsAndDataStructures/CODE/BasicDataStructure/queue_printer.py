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
        self.timeRemaining = 0
    
    def tick(self):
        if self.currentTask != None:
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
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    watingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            watingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()
    
    averageWait = sum(watingtimes) / len(watingtimes)
    print("Average Wait {} secs {} tasks remaining".format(averageWait, printQueue.size()))

def newPrintTask():
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
