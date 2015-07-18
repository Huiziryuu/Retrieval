__author__ = 'liuhui'

# bubble sort
def bubbleSort(alist):
    icount = len(alist) - 1

    while icount > 0:
        for i in range(icount):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        icount = icount - 1

# short bubble sort
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1


# selection sort, comparison is executed first, get the biggest number, then change it with the
# end of the unsorted items.
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1,fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]

# insertion sort -- hui version
# def insertionSort(alist):
#
#     for i in range(len(alist)):
#         found = False
#         for j in range(i + 1):
#             if alist[j] > alist[i] and not found:
#                 inserPos = j
#                 found = True
#             if alist[j] <= alist[i] and not found:
#                 continue
#             if found:
#                 break
#
#         if found:
#             icount = i
#             while icount > inserPos:
#                 alist[icount],alist[icount-1] = alist[icount-1],alist[icount]
#                 icount = icount - 1

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue

# shell sort
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "This list is", alist)

        sublistcount = sublistcount // 2

def gapInsertSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):

    if len(alist) > 1:
        # recursive divide the list into smaller pieces
        separatePoint = len(alist) // 2
        lefthalf = alist[:separatePoint]
        righthalf = alist[separatePoint:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        # compose the bigger items in the rest of righthalf list or lefthalf list
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def quickSortI(alist):
    quickSortHelperI(alist,0,len(alist)-1)

def quickSortHelperI(alist, first, last):
    if first < last:
        splitpoint = partitionI(alist, first, last)

        quickSortHelperI(alist,first,splitpoint-1)
        quickSortHelperI(alist,splitpoint+1,last)

def partitionI(alist, first, last):
    pivovalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivovalue:
            leftmark = leftmark + 1

        while rightmark >= leftmark and alist[rightmark] >= pivovalue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first],alist[rightmark] = alist[rightmark],alist[first]

    return rightmark

# for testing
alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)

# insertionSort(alist)
# print(alist)
# b =  [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
# shellSort(alist)
# print(alist)

quickSortI(alist)
print(alist)

