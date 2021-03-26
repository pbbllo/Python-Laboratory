class Node:
    def __init__(self, data):
        self._data = data
        self._right = None

    def getData(self):
        return self._data
    
    def getRight(self):
        return self._right

    def setData(self, data):
        self._data = data
    
    def setRight(self, node):
        self._right = node

    def toString(self):
        return str(self._data)

class SinglyLinked:
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

    def clear(self):
        self._head = self._tail = None
        self._size = 0
    
    def isEmpty(self):
        return self._head == None

    def search(self, data): #Complexity O(n)
        if self.isEmpty():
            raise Exception("The list is empty")
        
        currentNode = self._head
        currentIndex = 0
        while currentNode != None:
            if currentNode.getData() == data:
                return currentIndex

            currentIndex += 1
            currentNode = currentNode.getRight()

        return -1

    def delete(self, index):        
        if self.isEmpty():
            raise Exception("The list is empty")

        if index < 0 or index >= self._size:
            raise IndexError("Index of out list range")
            
        if index == 0: #Complexity O(1)
            node = self._head
            self.removeFirst()
            return node.toString()
        
        if index == (self._size - 1):
            node = self._tail
            self.removeLast()
            return node.toString()

        currentIndex = 0
        currentNode = self._head
        while currentIndex != index: #Complexity O(n)
            nodeBeforeIndex = currentNode
            currentNode = currentNode.getRight()
            currentIndex += 1

        nodeBeforeIndex.setRight(currentNode.getRight())
        currentNode.setRight(None) #Clear the memory
        self._size -= 1

        return currentNode.getData()
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("The list is empty")
        self._head = self._head.getRight()
        self._size -= 1
    
    def removeLast(self): #Complexity O(n)
        if self.isEmpty():
            raise Exception("The list is empty")
        if self._size == 1:
            self._head = self._tail = None
        else:
            currentNode = self._head
            while currentNode.getRight() != self._tail:
                currentNode = currentNode.getRight()
            self._tail = currentNode
            currentNode.setRight(None)

        self._size -= 1

    def add(self, data): #Complexity O(1)
        node = Node(data)
        if self.isEmpty():
            self._head = self._tail = node    
        else:
            self.__addLast(data)
        
        self._size += 1

    def addFirst(self, data):
        node = Node(data)
        node.setRight(self._head)
        self._head = node
        self._size += 1
    
    def __addLast(self, data):
        node = Node(data)
        self._tail.setRight(node)
        self._tail = node      

    def addAt(self, data, index): #Complexity O(n)
        node = Node(data)

        if self.isEmpty() or index >= self.length():
            raise IndexError("Index out of list range")
        
        currentNode = self._head
        currentIndex = 0
        while currentIndex != index:
            nodeBeforeIndex = currentNode
            currentNode = currentNode.getRight()
            currentIndex += 1

        node.setRight(currentNode)
        nodeBeforeIndex.setRight(node)
        
        self._size += 1

'''
*-------TESTE CASES-------*

singly = SinglyLinked()
print(singly.isEmpty())

singly.add(1)
singly.add(2)
singly.add(4)
print(singly)

singly.addAt(3,1)
print("The index of the number 3 is: " + str(singly.search(3)))

singly.delete(1)
print(singly.length())

print(singly.isEmpty())
print(singly)

singly.addFirst(10)
print(singly)

singly.removeFirst()
print(singly)

singly.add(6)
print(singly)

singly.removeLast()
print(singly)

singly.clear()
print(singly)
'''