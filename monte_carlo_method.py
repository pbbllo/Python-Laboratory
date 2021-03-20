import numpy as np

funcaoF = input('Enter the function f (x), "for example -> x ** 2": ')
funcaoG = input('Enter the function g (x), "for example -> 2 ** x": ')

def f(funcaoF):
    return eval(funcaoF)

def g(funcaoG):
    return eval(funcaoG)

a,b = [int(x) for x in input('Enter the values of a and b for the interval on the x-axis, for example -> 0 10: ').split()]
N = int(input('Enter the number of interactions, the higher the more accurate the result: '))

pontoDentro = 0
x = a + (b-a) * np.random.uniform(size=N)

max_y = max([f(x[i],funcaoF) for i in range(N)]) 
y = max_y * np.random.uniform(size=N)

for i in range(N):
    if y[i] <= f(x[i], funcaoF) and y[i] >= g(x[i], funcaoG):
        pontoDentro += 1
       
area =  (pontoDentro / N) * max_y * (b-a)

print(area)
