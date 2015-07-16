__author__ = 'liuhui'

class TreeNode:

    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.playload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

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

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.playload = value
        self.rightChild = rc
        self.leftChild = lc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

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
        rootNode = self.root
        current = TreeNode(key, val)
        if not rootNode:
            self.root = current
        else:
            self._put(key, val, self.root)
        self.size = self.size + 1

    def _put(self,key, val, currentNode):
        if key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
        elif key < currentNode.key:
            if currentNode.hasRightChild():
                self._put(key,val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        elif key == currentNode.key:
            return currentNode.replaceNodeData(key,val,currentNode.leftChild, currentNode.rightChild)

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

    # delete operation
    def delete(self,key):
        if self.size > 1:
            # to check whether the there is such node in the tree
            nodeToRemove = self._get(key, self.root)
            # the node exits
            if nodeToRemove:
                # call the remove function to remove this node
                self.remove(nodeToRemove)
                self.size = self.size -1
            else:
                raise KeyError('Error, key not in the tree')
        # in case the node is the root of the tree
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        # the tree itself is None
        else:
            raise KeyError('Error, key not in the tree')

    def __delitem__(self, key):
        self.delete(key)

    ''' remove a node from a tree, it is called by function delete(key)
    The to be deleted node might be:
    1. The node to be deleted has no children -> leaf node
    2. The node to be deleted has only one child
    3. The node to be deleted has two children
        '''
    def remove(self, currentNode):
        # case 1 - leaf node
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # case 3 -- has both leftChild and rightChild
        elif currentNode.hasBothChildren():
            # search for the successor which could replace
            # current node
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.playload = succ.playload
        # case 2 - has only one child
        else:
            if currentNode.parent:
                if currentNode.hasLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    if currentNode.isLeftChild():
                        currentNode.parent.leftChild = currentNode.leftChild
                    else:
                        currentNode.parent.rightChild = currentNode.leftChild

                else:
                    currentNode.rightChild.parent = currentNode.parent
                    if currentNode.isLeftChild():
                        currentNode.parent.leftChild = currentNode.rightChild
                    else:
                        currentNode.parent.rightChild = currentNode.rightChild
            else:
                if currentNode.hasLeftChild():
                    repalceNode = currentNode.leftChild
                else:
                    replaceNode = currentNode.rightChild

                currentNode.replaceNodeData(replaceNode.key, replaceNode.playload,repalceNode.leftChild, repalceNode.rightChild)

    # look for the successor for current node, there are three cases:
    # 1. current node has a right child - the smallest node of the right subtree
    # 2. current node doesn't have right child and is the right node of the parent node
    # 3. current node doesn't have right child and is the left child of the parent node
    # repalceNode.leftChild, replaceNode.rightChild)
    def findSuccessor(self):
        succ = None
        # case 1
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:

            if self.parent:
                # case 3
                if self.isLeftChild():
                    succ = self.parent
                # case 2
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    # the minimum node is the smallest left child node
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    # to compile the moved node and rest structure
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

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