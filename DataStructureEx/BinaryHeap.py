__author__ = 'liuhui'

class BinaryHeap:

    def __init__(self):
        self.heap = []

    def insert(self, k):
        n = 0
        if self.isEmpty():
            self.heap.insert(0,k)
            print(self.heap)
        else:
            for item in self.heap:
                if k < item:
                    n = n + 1

            self.heap.insert(n, k)

    def finMin(self):
        return self.heap[-1]

    def delMin(self):
        minNum = self.heap[-1]
        self.heap.pop()
        return minNum

    def isEmpty(self):
        return self.heap == []

    def size(self):
        return len(self.heap)

    def buildHeap(self, alist):
        for i in alist:
            self.insert(i)


# for testing
bh = BinaryHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())