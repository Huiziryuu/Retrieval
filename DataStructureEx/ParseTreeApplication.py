__author__ = 'liuhui'

import operator

from DataStructureEx import BinaryTree, Stack


def buildParseTree(fpexp):
    fplist = fpexp.split()
    eTree = BinaryTree.BinaryTree('')
    pStack = Stack.Stack()
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+': operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

# preorder traversal external call
def preorder(tree):
    # if the tree is None, then the function returns without
    # taking any action
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# inorder traversal
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# postorder raversal
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def printexp(tree):
    val = ""
    if tree:
        val = '(' + printexp(tree.getLeftChild())
        val = val + str(tree.getRootVal())
        val = val + printexp(tree.getRightChild()) + ')'
    return val

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(printexp(pt))