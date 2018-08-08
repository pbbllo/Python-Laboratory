#URI Questions
#Python
#Contando Carneirinhos
for a in range(int(input())):
    n = input()
    n = [int(x) for x in input().split()]
    alist = sorted(n)
    a = alist[0]
    cont = 1
    for p,e in enumerate(alist):
        if e != a:
            a = alist[p]
            cont += 1
    print(cont)
