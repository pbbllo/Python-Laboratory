import math

def arranjo(start, elements, path = [], array = []):        #O(n!)
    if len(elements) == 0:
        new_path = [start] + path
        array.append(new_path)
        return array
    else:
        for i, element in enumerate(elements):
            path.append(element)
            array = arranjo(start, elements[:i] + elements[i + 1:], path, array)
            path.remove(element)
            
    return array

def betterDistance(array, string = ""):                     #O(n²)
    betterPath = math.inf
    for path in array:
        distance = 0
        points = ""
        for i, p in enumerate(path[1:]):
            before_p = path[i-1]
            distance += (before_p[1] - p[1]) + (before_p[2] - p[2])
            points += p[0] + " "
        if distance <= betterPath:
            betterPath = distance
            string = points

    return string

    

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
            
array = arranjo(start, cities)
print(betterDistance(array))