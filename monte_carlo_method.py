import numpy as np

funcaoF = input('Digite a função f(x), "por exemplo --> x ** 2": ' )
funcaoG = input('Digite a função g(x), "por exemplo --> 2 ** x": ')

def f(x, funcaoF):
    return eval(funcaoF)

def g(x, funcaoG):
    return eval(funcaoG)

a,b = [int(x) for x in input('Digite os valores de a e b para o intervalo no eixo x, por exemplo --> 0 10: ').split()]
N = int(input('Digite o números de interações, quanto maior mais preciso o resultado: '))

pontoDentro = 0
x = a + (b-a) * np.random.uniform(size=N)

max_y = max([f(x[i],funcaoF) for i in range(N)]) 
y = max_y * np.random.uniform(size=N)

for i in range(N):
    if y[i] <= f(x[i], funcaoF) and y[i] >= g(x[i], funcaoG):
        pontoDentro += 1
       
area =  (pontoDentro/N) * max_y * (b-a)

print(area)