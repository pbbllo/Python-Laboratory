import sys
sys.path.append('/Users/Shiro/Desktop/Python')

from Implementations.doubly_linked_list import Node
from Implementations.queue import Queue

class BinaryTree():
    def __init__(self, root = None):
        self._nodes = 0
        self._root = root

        if root != None:
            self._nodes = 1
        
    def __str__(self):
        self.preOrder(self._root)
        self.inOrder(self._root)
        self.postOrder(self._root)

    def insert(self, data):                     # Avarage - O(log(n)), Worst - O(n)
        node = Node(data)

        if self.isEmpty():
            self._root = node
            self._nodes += 1
        if self.contains(data):
            raise ValueError("Cannot accept the equal values inside the tree")
        else:   
            currentNode = self._root
            while currentNode != None:
                parent = currentNode
                if data > currentNode.getData():
                    currentNode = currentNode.getRight()
                elif data < currentNode.getData():
                    currentNode = currentNode.getLeft()
            if data > parent.getData():
                parent.setRight(node)
            else:
                parent.setRight(node)
            self._nodes += 1

    '''Figure out how to make on recursive way'''
    def remove(self, data):                     # Avarage - O(log(n)), Worst - O(n)
        find = self._find(data)
        if find[0] == None:
            raise Exception("Cannot remove a data that not exist in tree")

        node, parent = find[0], find[1]
        right = node.getRight()
        left = node.getLeft()

        if right == left == None:               # first case = the node is a leaf node
            node = None
        elif right != None and left == None:    # second case = the node has a right subtree but no left subtree
            if parent.getRight() == node:
                parent.setRight(node.getRight)
            else:
                parent.setLeft(node.getRight)
        elif right == None and left != None:    # third case = the node has a left subtree but no right subtree
            if parent.getRight() == node:
                parent.setRight(node.getLeft)
            else:
                parent.setLeft(node.getLeft)
        else:                                   #fourth case = the node has a right and left subtree
            successor = self._successor(node)
            node.setData(successor.getData())
            self.remove(successor)
        self._nodes -= 1
    
    def _find(self, data):                      # Avarage - O(log(n)), Worst - O(n)
        currentNode = self._root
        while currentNode.getData() != data:
            parent = currentNode
            if data > currentNode.getData():
                currentNode = currentNode.getRight()
            elif data < currentNode.getData():
                currentNode = currentNode.getLeft()
        return (currentNode, parent)

    def contains(self, data):
        return self._find(data)[0].getData() == data

    def _successor(self, node):
        currentNode = node.getRight()
        while currentNode != None:
            successor = currentNode
            currentNode = currentNode.getLeft()
        return successor
    
    def height(self):                           # O(n)
        node = self._root
        if node == None:
            return 0
        return max(self.height(node.getLeft(), self.height(node.getRight()))) + 1
    
    def isEmpty(self):
        return self._root == None

    def preOrder(self, node):

        if node == None:
            return
        print(node.value)
        self.preOrder(node.getLeft())
        self.preOrder(node.getRight())
    
    def inOrder(self, node):
        
        if node == None:
            return
        self.inOrder(node.getLeft())
        print(node.getData())
        self.inOrder(node.getRight)

    def postOrder(self, node):

        if node == None:
            return
        self.postOrder(node.getLeft())
        self.postOrder(node.getRight())
        print(node.getData())
    
    def levelOrder(self, node):
        queue = Queue()

binaryTree = BinaryTree()
binaryTree.insert(0)
print(binaryTree)
binaryTree.insert(1)
print(binaryTree)
binaryTree.insert(2)
print(binaryTree)
binaryTree.insert(3)
print(binaryTree)