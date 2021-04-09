lines, columns = map(int, input().split())
matriz = [input().split() for i in range(lines)]    #O(n)
coordinates = []

for line in range(lines):
    for column in range(columns):
        if matriz[line][column] != "0":
            coordinate = (matriz[line][column], line, column)
            coordinates.append(coordinate)

print(coordinates)

#print(minDistance(matriz, lines, columns))