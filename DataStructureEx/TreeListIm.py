__author__ = 'liuhui'

# 1. simple tree definition in list
# myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
# print(myTree)
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])


# 2. formalize the definition of the tree data structure

# Tree constructor
def BinaryTree(r):
    return [r,[],[]]

# Insert a left child into the first level
# first lever? How strange it is!
def insertLeft(root, newBranch):
    t = root.pop(1)
    root.insert(1, [newBranch, t, []])
    return root

# insert a right child into the first level
def insertRight(root, newBranch):
    t = root.pop(2)
    root.insert(2, [newBranch, [], t])
    return t

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# for testing
r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
