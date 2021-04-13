def minDistance(coordinates, p, lines, columns):        # O(n) + O(n) = O(n + n) = O(2n) => O(n)
    if len(coordinates) == 0:
        return ""
    
    distance = lines * columns
    for point in coordinates:
        soma = abs(p[1] - point[1]) + abs(p[2] - point[2])
        if soma <= distance:
            travel = point
            distance = soma

    coordinates.remove(travel)
    return travel[0] + " " + minDistance(coordinates, travel, lines, columns)

lines, columns = map(int, input().split())
matriz = []
coordinates = []
for l in range(lines):                                 # O(n ** m) =>  O(n²)
    line = input().split()
    matriz.append(line)
    for c in range(columns):
        if line[c] != "0":
            coordinates.append((line[c], l, c))
        if line[c] == "R":
            start = (line[c], l, c)

coordinates.remove(start)
print(minDistance(coordinates, start, lines, columns))
