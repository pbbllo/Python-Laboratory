class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def getData(self):
        return self._data
    
    def getRight(self):
        return self._right
    
    def getLeft(self):
        return self._left

    def setData(self, data):
        self._data = data
    
    def setRight(self, node):
        self._right = node
    
    def setLeft(self, node):
        self._left = node
        
    def toString(self):
        return str(self._data)

class DoublyLinked:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __str__(self):
        if self._size == 0:
            return "[]"

        output = "["
        currentNode = self._head
        while currentNode != None:
            if currentNode == self._tail:
                output += currentNode.toString() + "]"
            else:
                output += currentNode.toString() + ","   
            currentNode = currentNode.getRight()
            
        return output

    def length(self):
        return self._size
    
    def isEmpty(self):
        return self._head == None

    def search(self, data):
        if self.isEmpty():
            raise Exception("The list is empty")
        
        currentNode = self._head
        while currentNode != None:
            if currentNode.getData() == data:
                return currentNode.getData()

            currentNode = currentNode.getRight()

        return -1
    
    def delete(self, index):
        if self.isEmpty():
            raise Exception("The list is empty")

        if index >= self._size:
            raise IndexError("Index of out list range")
            
        if index == 0: #Complexity O(1)
            node = self._head
            self.removeFirst()
            return node.getData()

        currentNode = self._head
        currentIndex = 0
        while currentIndex != index: #Complexity O(n)
            currentNode = currentNode.getRight()
            currentIndex += 1
        
        currentNode.getRight().setLeft(currentNode.getLeft())
        currentNode.getLeft().setRight(currentNode.getRight())
        currentNode.setRight(None)
        currentNode.setLeft(None)
        self._size -= 1

        return currentNode.getData()
        
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("The list is empty")
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.getRight()
            self._head.setLeft(None)
        self._size -= 1
    
    def removeLast(self):
        if self.isEmpty():
            raise Exception("The list is empty")
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.getLeft()
            self._tail.setRight(None)

        self._size -= 1

    def add(self, data):
        node = Node(data)

        if self.isEmpty():
            self._head = self._tail = node
        else:
            self.__addLast(data)

        self._size += 1

    def addFirst(self, data):
        node = Node(data)
        node.setRight(self._head)
        self._head.setLeft(node)
        self._head = node
        self._size += 1
    
    def __addLast(self, data):
        node = Node(data)
        node.setLeft(self._tail)
        self._tail.setRight(node)
        self._tail = node

    def addAt(self, data, index): #Complexity O(n)
        node = Node(data)

        if self.isEmpty() or index >= self.length():
            raise IndexError("Index out of list range")
        
        currentNode = self._head
        currentIndex = 0
        while currentIndex != index:
            currentNode = currentNode.getRight()
            currentIndex += 1

        node.setRight(currentNode)
        node.setLeft(currentNode.getLeft())
        currentNode.getLeft().setRight(node)
        currentNode.setLeft(node)

        
        self._size += 1

'''
*-------TESTE CASES-------*

doubly = DoublyLinked()
doubly.add(1)
doubly.add(2)
doubly.addAt(10,1)

print(doubly)

doubly.delete(1)

print(doubly)

doubly.removeFirst()

print(doubly)

doubly.removeLast()

print(doubly)

'''