class Array:
    def __init__(self, capacity = 0):
        self._tam = 0
        self._capacity = capacity
        self._array = [None]

        if capacity < 0:
            print("Illegal capacity: {}".format(capacity))
        else:
            self._array = [None] * capacity
    
    def __str__(self):
        if self._tam == 0:
            return "[]"
        output = ""
        for i in range(self._tam):
            if i == (self._tam - 1):
                output += str(self._array[i])
            else:
                output += str(str(self._array[i]) + ",")
        
        return "[" + output + "]"

    def length(self):
        return self._tam
    
    def isEmpty(self):
        return self.length() == 0
    
    def get(self, index):
        return self._array[index]

    def set(self, index, data):
        self._array[index] = data

    def clear(self):
        for i in range(self._capacity):
            self._array[i] = None
        self._tam = 0
    
    def add(self, data):
        if (self._tam + 1) >= self._capacity:
            if self._capacity == 0:
                self._capacity = 1
            else:
                self._capacity *= 2
            newArray = [None] * self._capacity
            for i in range(self._tam):
                newArray[i] = self._array[i]
            self._array = newArray
        self._array[self._tam] = data
        self._tam += 1
    
    def delete(self, index):
        if (index >= self._tam) and (index < 0):
            print("Invalid index: {}".format(index))
            return -1
        data = self._array[index]
        newArray = [None] * (self._tam - 1)
        j = -1
        for i in range(self._tam):
            j += 1
            if (i == index):
                j -= 1
            else:
                newArray[j] = self._array[i]
        self._array = newArray
        self._tam -= 1
        self._capacity -= 1
    
    def index(self, data):
        for i in range(self._tam):
            if self._array[i] == data:
                return i
        return -1

dynamicList = Array(0)
print(dynamicList)

dynamicList.add(1)
dynamicList.add(2)

print(dynamicList.length())
print(dynamicList)
print(dynamicList.isEmpty())
print(dynamicList.get(0))

dynamicList.set(1,3)
print(dynamicList.get(1))