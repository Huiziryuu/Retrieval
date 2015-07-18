__author__ = 'liuhui'

import os
import sys

import timeit

class leXicalDic:

    def __init__(self):
        self.lexical_dicA = {}
        self.lexical_dicB ={}
        self.lexical_dicC = {}
        self.lexical_dicD = {}
        self.lexical_dicE = {}
        self.lexical_dicF = {}
        self.lexical_dicG = {}
        self.lexical_dicH = {}
        self.lexical_dicI = {}
        self.lexical_dicJ = {}
        self.lexical_dicK = {}
        self.lexical_dicL = {}
        self.lexical_dicM = {}
        self.lexical_dicN = {}
        self.lexical_dicO = {}
        self.lexical_dicP = {}
        self.lexical_dicQ = {}
        self.lexical_dicR = {}
        self.lexical_dicS = {}
        self.lexical_dicT = {}
        self.lexical_dicU = {}
        self.lexical_dicV = {}
        self.lexical_dicW = {}
        self.lexical_dicX = {}
        self.lexical_dicY = {}
        self.lexical_dicZ = {}
        self.lexical_dicOther = {}
        self.list_existed = []
        self.list_notExisted = []
        self.switcher = {
                'A': self.lexical_dicA,
                'B': self.lexical_dicB,
                'C': self.lexical_dicC,
                'D': self.lexical_dicD,
                'E': self.lexical_dicE,
                'F': self.lexical_dicF,
                'G': self.lexical_dicG,
                'H': self.lexical_dicH,
                'I': self.lexical_dicI,
                'J': self.lexical_dicJ,
                'K': self.lexical_dicK,
                'L': self.lexical_dicL,
                'M': self.lexical_dicM,
                'N': self.lexical_dicN,
                'O': self.lexical_dicO,
                'P': self.lexical_dicP,
                'Q': self.lexical_dicQ,
                'R': self.lexical_dicR,
                'S': self.lexical_dicS,
                'T': self.lexical_dicT,
                'U': self.lexical_dicU,
                'V': self.lexical_dicV,
                'W': self.lexical_dicW,
                'X': self.lexical_dicX,
                'Y': self.lexical_dicY,
                'Z': self.lexical_dicZ
            }

    ''' read frequency list into memory
    '''
    def composeDic(self, filePath):
        # check file existence - exist
        if os.path.exists(filePath):
            # todo: to get file encode automatically
            #f = open(filePath,'r', encoding="latin1")
            f = open(filePath,'r', encoding="iso-8859-1")
            for i in f:
                word, freq = i.split()
                dic = self.switcher.get((word[0].upper()))
                if dic == None:
                    dic = self.lexical_dicOther
                dic[word] = (word, freq)
        # check file existence - doesn't exist
        else:
            print('File', filePath, 'does not exist!')
            sys.exit(1)

    ''' search items from the dictionary
    '''
    def searchDic(self, items):
        for item in items:
            try:
                dic = self.switcher.get((item[0].upper()))
                if dic == None:
                    dic = self.lexical_dicOther
                self.list_existed.append(dic[item])
            except KeyError:
                self.list_notExisted.append(item)

def test():
    dic = leXicalDic()
    dic.composeDic('/Users/liuhui/Documents/MasterStudy/2015/Programming_Project/source/ari/freq_eng')
    #print(dic.lexical_dicA)
    dic.searchDic(['algorithmiquement','aagoel', 'homathorizon', 'huiliu', 'enghls', 'french]'])
    # print(dic.list_existed)
    # print(dic.list_notExisted)

if __name__ == '__main__':
    # main()
    test1 = timeit.Timer("test()", "from __main__ import test")




print("composeDic start", test1.timeit(0)*1000, "ms")
