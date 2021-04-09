lines, columns = map(int, input().split())
matriz = [input().split() for i in range(lines)]
coordinates = []
start = 0

for line in range(lines):                               # O(n ** 2)
    for column in range(columns):
        if matriz[line][column] != "0":
            coordinate = (matriz[line][column], line, column)
            coordinates.append(coordinate)
        if matriz[line][column] == "R":
            start = len(coordinates) - 1

def minDistance(coordinates, p, lines, columns)
    distance = lines * columns
    for point in coordinates:
        a = p[1] - point[1]
        b = p[2] - point[2]
        soma = abs(a + b)
        
        if soma <= distance:
            return 0


print(coordinates)

#print(minDistance(matriz, lines, columns))