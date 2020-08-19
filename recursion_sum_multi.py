def suc(numero):
    sucessor = numero+1
    return sucessor

def soma(numero1, numero2):
    if numero2 == 0:
        return somafinal
    else:
        return soma(suc(numero1), numero2-1)
        
def multi(numero1, numero2):
    if numero2 == 1:
        return numero1
    elif numero2 == 0 or numero1 == 0:
        return 0
    else:
        return soma(numero1,multi(numero1, numero2-1))       

print(multi(3,5))
