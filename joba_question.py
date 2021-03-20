
n = 100
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i < j and j < k:
                count += 1
                #print(i, j, k)
print(count)

'''
def somatorio(n):

    soma = 0
    for i in range(n):
        soma +=  n ** 2
    
    print(soma)

somatorio(10)
'''