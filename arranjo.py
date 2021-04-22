import math

def arranjo(elements, path, array):
    if len(elements) == 0:
        array.append(path)
        return array
    else:
        for i, element in enumerate(elements):
            array = arranjo(elements[:i] + elements[i + 1:], path + element, array)
            
    return array

def betterDistance(array, cities, start):
    betterPath = math.inf

    return betterPath

    
'''
cities = []
elements = []
start = None    
lines, columns = map(int, input().split())
for l in range(lines):
    line = input().split()
    for c in range(columns):
        if line[c] == "R":
            start = (line[c], l, c)
        elif line[c] != "R" and line[c] != "0":
            cities.append((line[c], l, c))
            elements.append(line[c])
'''

elements = input().split()
array = []
array = arranjo(elements, "", array)
print(array)