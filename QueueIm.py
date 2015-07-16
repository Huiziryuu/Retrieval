__author__ = 'liuhui'

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, elem):
        self.items.insert(0, elem)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# queue application
def hotPotato(namelist, num):
    q = Queue()

    for player in namelist:
        q.enqueue(player)

    iCount = 0
    while iCount < num:
        toQ = q.dequeue()
        q.enqueue(toQ)
        iCount = iCount + 1

    return q.dequeue()

# simulation of printer
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate

import random
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):

    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labPrinter.startNext(nexttask)

        labPrinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 91)
    if num == 90:
        return True
    else:
        return False

# for testing
# q = Queue()
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print(q.size())
# print(q.isEmpty())
# print(q.dequeue())
# print(q.dequeue())
# print(q.size())

# print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

for i in range(10):
    simulation(3600,5)