import sys
sys.path.append('/Users/Shiro/Desktop/Python')

from Implementations.dynamicList import Array

class PriorityQueue(Array):
    def __init__(self, capacity = 0):
        super().__init__(capacity = capacity)

    def add(self, data):
        if data == None:
            raise Exception("The data cannot be null")
        return super().add(data)

    def delete(self, index):
        return super().delete(index)        

    def isEmpty(self):
        return super().isEmpty()
    
    def clear(self):
        return super().clear()
    
    def length(self):
        return super().length()
    
    def peek(self):
        if self.isEmpty() == True:
            raise IndexError("The List is empty")
        return self.get(0)
    
    def pool(self):
        if self.isEmpty() == True:
            raise IndexError("The List is empty")
        return self.delete(0)



