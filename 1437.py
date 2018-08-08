#Uri Questions
#Python
#Esquerda, Volver!
dic = {0:'N',1:'L',2:'S',3:'O'}
while True:
    n = int(input())
    if n == 0: break;
    comand = input()
    n = 0
    for read in comand:
        if read == 'D': n += 1
        else: n -= 1
    n = n%4
    print(dic[n])
