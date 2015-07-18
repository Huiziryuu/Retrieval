__author__ = 'liuhui'

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        previousNode = None
        currentNode = self.head
        found = False

        while (not found) and currentNode != None:
            if currentNode.getData() == item:
                found = True
            elif currentNode.getData() < item:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            elif currentNode.getData() > item:
                return

        if found and previousNode == None:
            self.head = currentNode.getNext()
        elif found and previousNode != None:
            previousNode.setNext(currentNode.getNext())

    def search(self, item):
        currentNode = self.head
        found = False

        while (not found) and currentNode != None:
            if currentNode.getData() == item:
                found = True
            elif currentNode.getData() < item:
                currentNode = currentNode.getNext()
            else:
                return found

        return found

    def add(self, item):
        previousNode = None
        currentNode = self.head

        while currentNode != None and currentNode.getData() < item:
            previousNode = currentNode
            currentNode = currentNode.getNext()

        newNode = Node(item)
        if previousNode != None:
            newNode.setNext(currentNode)
            previousNode.setNext(newNode)
        else:
            newNode.setNext(currentNode)
            self.head = newNode


# for testing
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))