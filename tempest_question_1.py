def CalcularNumero(data):
    contador = 0
    comprimento = 0
    data = [1,12,0,2,2,0,2,1]

    while contador < comprimento:
        if (data[contador] + contador) % 2 == 0:
            adicional = data[comprimento - (contador + 1)]
            data[contador] = data[contador] + adicional
        else:
            data[contador] = 0
        contador += 1
    
    return data

somatorio = sum(CalcularNumero([1,8,0,2,2,0,2,1]))
print(somatorio)
