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