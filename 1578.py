#Uri Questions
#Python
#Matriz de Quadrados
n = int(input())
for z in range(n):
    print('Quadrado da matriz #{}:'.format(4+z))
    globo = []
    test = int(input())
    for e in range(test):
        r = []
        for read in [int(x) for x in input().split()]:
            r.append(str(read*read))
        globo.append(r)
    space = []
    for ee in range(test):
        hai = 0
        for read in globo:
            if len(read[ee]) > hai:
                hai = len(read[ee])
        space.append(hai)
    for eee in globo:
        answer = []
        for p,a in enumerate(eee):
            answer.append(' '*(space[p]-len(a))+a)
        answer = ' '.join(answer)
        print(answer)
    if z < n-1:
        print()
