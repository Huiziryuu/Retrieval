__author__ = 'liuhui'

class TreeNode:

    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.playload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, bal, lc, rc):
        self.key = key
        self.playload = value
        self.balanceFactor = bal
        self.rightChild = rc
        self.leftChild = lc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BalancedBinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        current = TreeNode(key, val)
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = current

        self.size = self.size + 1

    # to add key to the proper node
    def _put(self, key, val, currentNode):
        if key == currentNode.key:
            return currentNode.replaceNodeData(key,val,currentNode.balanceFactor,currentNode.leftChild, currentNode.rightChild)
        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    # update the balance factor for add item
    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.reBalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            # evaluate the chain effect
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    # right-heavy, so rotate part of the right to the left
    # steps:
    # 1. Promote the right child (B) to be the root of the subtree.
    # 2. Move the old root (A) to be the left child of the new root.
    # 3. If new root (B) already had a left child then make it the right child of the new left child (A).
    # (If new root (B) already had a left child then make it the right child of the new left child (A).
    # point. This allows us to add a new node as the right child without any further consideration.)
    def rotateLeft(self, rotRoot):
        # 1. promote the right child to be the new root
        newRoot = rotRoot.rightChild

        # let the left child of new root to be the right child of rot root node
        # !!! don't forgte to update the parent references
        rotRoot.rightChild = newRoot.leftChild
        if rotRoot.rightChild:
            rotRoot.rightChild.parent = rotRoot

        # in case the rotRoot is root of the tree
        # update the tree root reference
        newRoot.parent = rotRoot.parent
        if not newRoot.parent:
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot

        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot

        # update balance information
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - max(rotRoot.balanceFactor, 0)

    # left-heavy, to rotate part of the left to the right subtree
    # rotate steps:
    # 1. Promote the left child (C) to be the root of the subtree.
    # 2. Move the old root (E) to be the right child of the new root.
    # 3. If the new root(C) already had a right child (D) then make it the left child of the new right child (E).
    # (Since the new root (C) was the left child of E, the left child of E is guaranteed to be empty at
    # this point. This allows us to add a new node as the left child without any further consideration.)
    def rotateRight(self, rotRoot):
        # promote the left child as new root
        newRoot = rotRoot.leftChild

        # move the right child
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild:
            rotRoot.leftChild.parent = rotRoot

        # move the original root node as the right child of new root
        newRoot.rightChild = rotRoot
        if rotRoot.parent:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        # set the new parent to the rot root
        newRoot.parent = rotRoot.parent
        rotRoot.parent = newRoot
        # if the new root is the root of the whole tree
        if not newRoot.parent:
            self.root = newRoot

        rotRoot.balanceFactor = rotRoot.balanceFactor - min(0, newRoot.balanceFactor) - 1
        newRoot.balanceFactor = rotRoot.balanceFactor + max(0, rotRoot.balanceFactor) - 1


    # balance rule:
    # 1. If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child.
    #    If the right child is left heavy then do a right rotation on the right child, followed by the original left rotation.
    # 2. If a subtree needs a right rotation to bring it into balance, first check the balance factor of the left child.
    #    If the left child is right heavy then do a left rotation on the left child, followed by the original right rotation.
    def reBalance(self, node):
        if node.balanceFactor < 0 and node.hasRightChild():
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)

            self.rotateLeft(node)
        elif node.balanceFactor > 0 and node.hasLeftChild():
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)

            self.rotateRight(node)

    # overload the [] operator for assignment
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.playload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        elif currentNode.key < key:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, item):
        return self.get(item)

    # implement 'in' operation
    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False

     # overrides 'for x in' operation
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRighChild():
                for elem in self.rightChild:
                    yield elem


# ==================================================================================== #
import os
import sys
import timeit

class leXicalDic:

    def __init__(self):
        # to compose a dictionary from word list
        self.lexical_dic = BalancedBinarySearchTree()
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

# def main():
#     if len(sys.argv) < 3:
#         print('input parameter error \n','usage: ./Retrieval_Hash.py freq_lexi_dic_file lexical_item1 lexical_item2 ...')
#         exit(1)
#
#     dic = leXicalDic()
#     dic.composeDic(sys.argv[1])
#     dic.searchDic(sys.argv[2:])
#     print("retrieval result - available words:", dic.list_existed)
#     print("retrieval result - words not in the lexicon:", dic.list_notExisted)
#
# if __name__ == '__main__':
#     main()

#####################################################
#
# for testing only
# execution time is 11 seconds around
#
#####################################################
import timeit
def test():
    dic = leXicalDic()
    dic.composeDic('/Users/liuhui/Documents/MasterStudy/2015/Programming_Project/source/ari/freq_eng')
    dic.searchDic(['algorithmiquement','aagoel', 'homathorizon', 'huiliu', 'enghls', 'french', 'ok', 'whaoo', 'what', 'finland', 'python'])
    print(dic.list_existed)
    print(dic.list_notExisted)

if __name__ == '__main__':
    test1 = timeit.Timer("test()", "from __main__ import test")
    print('test execution time is:',test1.timeit(1), 'seconds')