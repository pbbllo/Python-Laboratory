#Uri Questions
#Python
#Adivinha
for x in range(int(input())):
    qt,s = map(int, input().split())
    luck = [int(y) for y in input().split()]
    if s in luck:
        print(luck.index(s)+1)
    else:
        delta = 10000000000000000
        answer = 0
        for p,e in enumerate(luck):
            if abs(s-e) < delta:
                answer = p
                delta = abs(s-e)
        print(answer+1)
