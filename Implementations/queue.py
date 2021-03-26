from Implementations.doubly_linked_list import DoublyLinked

class Queue(DoublyLinked):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return super().__str__()

    def enqueue(self, data):
        return super().add(data)
    
    def dequeue(self):
        return super().removeFirst()
    
    def peek(self):
        if self.isEmpty():
            return "None"
        return self._head

    def length(self):
        return super().length()

    def isEmpty(self):
        return super().isEmpty()

'''
*-------TESTE CASES-------*
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.length())
print(queue)

queue.dequeue()
print(queue.length())
print(queue)

'''