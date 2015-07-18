__author__ = 'liuhui'

class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            newTree = BinaryTree(newNode)
            newTree.leftChild = self.leftChild
            self.leftChild = newTree

    def insertRight(self, newNode):
        newTree = BinaryTree(newNode)
        if self.rightChild == None:
            self.rightChild = newTree
        else:
            newTree.rightChild = self.rightChild
            self.rightChild = newTree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # preorder traversal
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

# for testing
# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())
#
#
# newTree = BinaryTree('a')
# newTree.insertRight('f')
# newTree.insertRight('c')
# newTree.getRightChild().insertLeft('e')
# newTree.insertLeft('b')
# newTree.getLeftChild().insertRight('d')