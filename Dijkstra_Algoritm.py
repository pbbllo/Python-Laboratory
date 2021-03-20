def dijkstra(grafo, origem, predecessor, origem_to_vertice,cities):
    visited = []
    for e in range(cities):
        predecessor[e] = -1
        origem_to_vertice[e] = -1
        visited.append(0)

    origem_to_vertice[origem] = 0

    for x in range(cities-1):
        variable = minDistance(origem_to_vertice, visited,cities)

        visited[variable] = 1
        for f in grafo[variable]:
            if origem_to_vertice[f] < 0:
                origem_to_vertice[f] = origem_to_vertice[variable] + 1
                predecessor[f] = variable
            elif origem_to_vertice[f] > origem_to_vertice[variable] + 1:
                    origem_to_vertice[f] = origem_to_vertice[variable] + 1
                    predecessor[f] = variable
    return origem_to_vertice

def minDistance(origem_to_vertice, visited,cities):
    first_visit = True
    menor = 0
    for i in range(cities):
        if origem_to_vertice[i] >= 0 and visited[i] == 0:
            if first_visit:
                first_visit = False
                menor = i
            elif origem_to_vertice[menor] > origem_to_vertice[i]:
                menor = i
    return menor
        
    
grafo = []
predecessor = []
origem_to_vertice = []
