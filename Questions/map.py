class Grafo:
    def __init__(self):
        self.lista_Vertices = []  # Stores the vertices
        self.matriz = [[0,1,1,0,0,0,0,0],
                       [1,0,1,0,1,1,1,0],
                       [1,1,0,1,1,0,0,0],
                       [0,0,1,0,1,1,0,1],
                       [0,1,1,1,0,1,0,0],
                       [0,1,0,1,1,0,1,0],
                       [0,1,0,0,0,1,0,1],
                       [0,0,0,1,0,0,1,0]]

    def insert_listaVertices(self, vertice):
        self.lista_Vertices.append(vertice)

    def getLista_Vertices(self):
        return self.lista_Vertices

    def add_to_matriz(self, lista):
        self.matriz.append(lista)

    def getMatriz(self):
        return self.matriz


class Vertice:
    def __init__(self, info):
        self.info = info
        self.color = 'None'
        self.linked = []

    def setInfo(self, info):
        self.info = info

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getLinked(self):
        return self.linked

    def setLinked(self, vertice):
        self.linked.append(vertice)


def recursao(country):
    colors_current = []  # List unavailable colors of the country
    country_color = country.getColor()  # Get current color of the country
    for province in country.getLinked():  # Browse countries linked to the current country
        province_color = province.getColor()  # Get the color of the linked country
        if province_color == country_color:  # Compare the colors betwween linked country and current country
            colors_current.append(province_color)  # Add to the list unavailable colors of the country
            for color in colors:  # Search a new color for the current country
                if color not in colors_current:  # Check that it's not in list unavailable
                    country.setColor(color)  # Set the new color
                    break
            recursao(province)  # Enter on the route
        else:
            colors_current.append(
                province_color)  # Just add to the list unavailable don't enter on the route, because the country are colored
    if country.getColor() == 'None':
        for color in colors:  # Search a new color for the current country
            if color not in colors_current:  # Check that it's not in list unavailable
                country.setColor(color)  # Set the new color
                break

    return 0


number_countries = 8  # numbers of countries

mapa = Grafo()

colors = [x for x in range(number_countries)]

for i in range(number_countries):
    A = Vertice(i)
    mapa.insert_listaVertices(A)


matriz = mapa.getMatriz()
vertices = mapa.getLista_Vertices()

for i in range(number_countries): #Link the vertices
    for j in range(i + 1, number_countries):
        if matriz[i][j] == 1:
            vertices[i].setLinked(vertices[j])
            vertices[j].setLinked(vertices[i])

for country in vertices: #Make the answer
    number = recursao(country)
for country in vertices:
    if country.getColor() > number:
        number = country.getColor()
print(number + 1)
