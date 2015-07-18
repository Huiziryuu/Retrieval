__author__ = 'liuhui'

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, elem):
        self.items.insert(0, elem)

    def addFront(self, elem):
        self.items.append(elem)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# application palindorme
def palchecker(aString):
    toProcess = Deque()

    for elem in aString:
        toProcess.addFront(elem)

    while (not toProcess.isEmpty()) and (toProcess.size() > 1):
        if toProcess.removeFront() != toProcess.removeRear():
            return False
        else:
            return True

# for testing
# d=Deque()
# print(d.isEmpty())
# d.addRear(4)
# d.addRear('dog')
# d.addFront('cat')
# d.addFront(True)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.removeRear())
# print(d.removeFront())

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))