__author__ = 'liuhui'

class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # shift with the parent node, if current node is smaller than the parent node
    def perUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp

            i = i // 2

    # add new value into the binary heap
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perUp(self.currentSize)

    # percDown : swap the whole structure to keep the balance property
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    # return the smaller child node position
    def minChild(self, i):
        # there is no right child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    # delete the minimum value of the heap
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    # build an entire heap from a list of keys
    def buildHeap(self, alist):
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        i = self.currentSize // 2
        # shape the heap to balance it
        while (i > 0):
            self.percDown(i)
            i = i - 1

h = BinHeap()
h.buildHeap([5,6,9,2,1,5,3,8,4,2])
print(h.heapList)