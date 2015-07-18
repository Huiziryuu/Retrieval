__author__ = 'liuhui'

# 1
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

# 2
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

# 3
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while not found and first <= last:
        nextPos = (last + first) // 2
        # print(alist[nextPos])
        if alist[nextPos] == item:
            found = True
        else:
            if alist[nextPos] > item:
                last = nextPos - 1
            else:
                first = nextPos + 1

    return found

def binarySearchC(alist, item):
    if len(alist) == 0:
        return False
    else:
        nextPos = len(alist) // 2
        # print(alist[nextPos])
        if alist[nextPos] == item:
            return True
        else:
            if alist[nextPos] > item:
               return binarySearchC(alist[:nextPos], item)
            else:
               return binarySearchC(alist[nextPos+1:], item)



# for testing
# 1
# testList = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequentialSearch(testList, 3))
# print(sequentialSearch(testList, 13))

#2
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(orderedSequentialSearch(testlist, 3))
# print(orderedSequentialSearch(testlist, 13))

# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
# print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 13))
#
# print(binarySearchC(testlist, 3))
# print(binarySearchC(testlist, 13))

alist = [3,5,6,8,11,12,14,15,17,18]
print(binarySearch(alist, 16))
print(binarySearchC(alist, 16))