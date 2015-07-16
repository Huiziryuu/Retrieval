__author__ = 'liuhui'

import os
import sys

class leXicalDic:

    def __init__(self):
        # to compose a dictionary from word list
        self.lexical_dic = {}
        # to store the search result
        self.list_existed = []
        self.list_notExisted = []

    ''' read frequency list into memory
    '''
    def composeDic(self, filePath):
        # check file existence - exist
        if os.path.exists(filePath):
            # todo: to get file encode automatically
            f = open(filePath,'r', encoding="latin1")
            for i in f:
                word, freq = i.split()
                self.lexical_dic[word] = (word, freq)
            f.close()
        # check file existence - doesn't exist
        else:
            print('File', filePath, 'does not exist!')
            sys.exit(1)

    ''' search items from the dictionary
    '''
    def searchDic(self, items):
        for item in items:
            try:
                lexi = self.lexical_dic[item]
                self.list_existed.append((lexi[0], int(lexi[1])))
            except KeyError:
                self.list_notExisted.append(item)

        self.quickSort(self.list_existed)

    ''' sort search result according to the word frquency
    '''
    def quickSort(self, alist):
        self.quickSortHelper(alist,0,len(alist)-1)

    ''' sort helper functoin, mainly for recursive call
    '''
    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)

            self.quickSortHelper(alist,first,splitpoint-1)
            self.quickSortHelper(alist,splitpoint+1,last)

    ''' to find the partition point for each sort loop
    '''
    def partition(self, alist, first, last):
        pivovalue = alist[first][1]

        leftmark = first
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark][1] >= pivovalue:
                leftmark = leftmark + 1

            while rightmark >= leftmark and alist[rightmark][1] <= pivovalue:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        # exchange
        alist[first],alist[rightmark] = alist[rightmark],alist[first]

        return rightmark

def main():
    if len(sys.argv) < 3:
        print('input parameter error \n','usage: ./Retrieval_Hash.py freq_lexi_dic_file lexical_item1 lexical_item2 ...')
        exit(1)

    dic = leXicalDic()
    dic.composeDic(sys.argv[1])
    dic.searchDic(sys.argv[2:])
    print("retrieval result - available words:", dic.list_existed)
    print("retrieval result - words not in the lexicon:", dic.list_notExisted)

if __name__ == '__main__':
    main()


#####################################################
#
# for testing only
# execution time is 11 seconds around
#
#####################################################
# import timeit
# def test():
#     dic = leXicalDic()
#     dic.composeDic('/Users/liuhui/Documents/MasterStudy/2015/Programming_Project/source/ari/freq_eng')
#     dic.searchDic(['algorithmiquement','aagoel', 'homathorizon', 'huiliu', 'enghls', 'french', 'ok', 'whaoo', 'what', 'finland', 'python'])
#     print(dic.list_existed)
#     print(dic.list_notExisted)
#
# if __name__ == '__main__':
#     test1 = timeit.Timer("test()", "from __main__ import test")
#     print('test execution time is:',test1.timeit(1), 'seconds')