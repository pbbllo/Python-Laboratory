def arranjo(elements, string):
    if len(elements) == 0:
        print(string)
    else:
        for i, element in enumerate(elements):
            arranjo(elements[:i] + elements[i + 1:], string + element)
elements = input().split()
arranjo(elements, "")