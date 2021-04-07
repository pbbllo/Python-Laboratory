import sys
sys.path.append('/Users/Shiro/Desktop/Python')

from Implementations.doubly_linked_list import Node
from Implementations.queue import Queue
import math

class BinaryTree():
    def __init__(self, root = None):
        self._nodes = 0
        self._root = root

        if root != None:
            self._nodes = 1

    '''    
    def __str__(self):
        output = ""
        preOrder = self.preOrder(self._root, output)
        inOrder = self.inOrder(self._root, output)
        postOrder = self.postOrder(self._root, output)

        return preOrder
    '''

    def insert(self, data):                     # Avarage - O(log(n)), Worst - O(n)
        if self.isEmpty():
            self._root = Node(data)
            self._nodes += 1
        elif self.contains(data):
            raise ValueError("Cannot accept the equal values inside the tree")
        else:
            self._insert(data, self._root)   
            self._nodes += 1
    
    def _insert(self, data, currentNode):
        if data > currentNode.getData():
            if currentNode.getRight() == None:
                currentNode.setRight(Node(data))
            else:
                self._insert(data, currentNode.getRight())
        elif data < currentNode.getData():
            if currentNode.getLeft() == None:
                currentNode.setLeft(Node(data))
            else:
                self._insert(data, currentNode.getLeft())

    def remove(self, data):                     # Avarage - O(log(n)), Worst - O(n)
        if not self.contains(data):
            raise ValueError("Cannot remove a data that not exist in the tree")
        else:
            self._remove(data, self._root)
            self._nodes -= 1
        '''
        # first case = the node is a leaf node
        # second case = the node has a right subtree but no left subtree
        # third case = the node has a left subtree but no right subtree
        # fourth case = the node has a right and left subtree
        '''    
    def _remove(self, data, currentNode):
        if data > currentNode.getData():
            node = currentNode.getRight()
            if data == node.getData():
                self._removeCases(node, currentNode)
            else:    
                self._remove(data, currentNode.getRight())
        elif data < currentNode.getData():
            node = currentNode.getLeft()
            if data == node.getData():
                self._removeCases(node, currentNode)
            else:
                self._remove(data, currentNode.getLeft())
        #elif data == currentNode.getData():

        

    def _removeCases(self, node, currentNode):
        rightChild = node.getRight()
        leftChild = node.getLeft()
        nodeData = node.getData()
        currentNodeData = currentNode.getData()

        #   first case
        if leftChild == rightChild == None:
            if nodeData > currentNodeData:
                currentNode.setRight(None)
            else:
                currentNode.setLeft(None)
        #   second case
        elif leftChild == None and rightChild != None:
            if nodeData > currentNodeData:
                currentNode.setRight(rightChild)
            else:
                currentNode.setLeft(rightChild)
        # third case
        elif leftChild != None and rightChild == None:
            if nodeData > currentNodeData:
                currentNode.setRight(leftChild)
            else:
                currentNode.setLeft(leftChild)
        # forth case
        elif leftChild != None and rightChild != None:
            successor = self._successor(node)
            successorData = successor.getData()
            node.setData(successorData)
            if successor == node.getRight():
                node.setRight(successor.getRight())
            else:
                self._remove(successorData, node.getRight())        
    
    def _find(self, data):                      # Avarage - O(log(n)), Worst - O(n)
        currentNode = self._root
        while currentNode != None and currentNode.getData() != data:
            if data > currentNode.getData():
                currentNode = currentNode.getRight()
            elif data < currentNode.getData():
                currentNode = currentNode.getLeft()
        return currentNode

    def contains(self, data):
        node = self._find(data)
        return node != None

    def _successor(self, node):
        currentNode = node.getRight()
        while currentNode != None:
            successor = currentNode
            currentNode = currentNode.getLeft()
        return successor
    
    def height(self):                           # O(1)
        return math.floor(math.log2(self._nodes))
    
    def isEmpty(self):
        return self._root == None

    def preOrder(self, node, string = ""):
        if node == None:
            return string
        string += node.toString() + " "
        string = self.preOrder(node.getLeft(), string)
        string = self.preOrder(node.getRight(), string)

        return string

    def inOrder(self, node, string = ""):
        if node == None:
            return string
        string = self.inOrder(node.getLeft(), string)
        string = string + node.toString() + " "
        string = self.inOrder(node.getRight(), string)

        return string

    def postOrder(self, node, string = ""):
        if node == None:
            return string
        string = self.postOrder(node.getLeft(), string)
        string = self.postOrder(node.getRight(), string)
        string = string + node.toString() + " "

        return string
    
    def levelOrder(self, node):
        queue = Queue()

binaryTree = BinaryTree()
binaryTree.insert(6)
binaryTree.insert(7)
binaryTree.insert(3)
binaryTree.insert(5)
binaryTree.insert(2)
binaryTree.insert(4)

print("------PREORDER------")
print(binaryTree.preOrder(binaryTree._root))

print("------INORDER------")
print(binaryTree.inOrder(binaryTree._root))

print("------POSTORDER------")
print(binaryTree.postOrder(binaryTree._root))

print("------------")
print(binaryTree.height())

binaryTree.remove(3)
print(binaryTree.preOrder(binaryTree._root))