import sys
sys.path.append('/Users/Shiro/Desktop/Python')

from Implementations.doubly_linked_list import DoublyLinked

class Stack(DoublyLinked):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return super().__str__()

    def pop(self):
        return super().removeLast()
    
    def push(self, data):
        super().add(data)

    def peek(self):
        if self.isEmpty():
            return "None"
            
        return self._tail.toString()

    def length(self):
        return super().length()

    def isEmpty(self):
        return super().isEmpty()


#*-------TESTE CASES-------*

stack = Stack()

stack.push(4)
stack.push(2)
stack.push(5)
stack.push(13)
print(stack)

stack.pop()
stack.pop()
print(stack)


stack.push(10)
print(stack)

stack.pop()
stack.pop()
stack.pop()
print(stack)


