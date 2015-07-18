__author__ = 'liuhui'

import time

# # example
# def sumOfN2(n):
#     start = time.time()
#
#     theSum = 0
#     for i in range(1, n+1):
#         theSum = theSum + i
#
#     end = time.time()
#
#     return theSum,end-start
#
# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sumOfN2(10000))
#
# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sumOfN2(100000))
#
# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))

def compareN2(alist):
    lenList = len(alist)
    minNum = alist[0]
    for i in range(0, lenList):
        for j in range(0, lenList):
            if alist[i] > alist[j] and alist[j] < minNum:
                minNum = alist[j]

    print("first function minimum number is ", minNum)

def compareN(alist):
    minNum = alist[0]
    lenList = len(alist)
    for i in range(1, lenList):
        if minNum > alist[i]:
            minNum = alist[i]
            i = i + 1

    print("second function minimum number is ", minNum)

pa = range(1,99)

s1 = time.time()
compareN2(pa)
s2 = time.time()
print("first execution time is ", s2-s1)

s1 = time.time()
compareN(pa)
s2 = time.time()
print("second execution time is ", s2-s1)