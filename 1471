#Uri Questions
#Python
#Mergulho
while True:
    try:
        n,r = map(int, input().split())
        back = [int(x) for x in input().split()]
        answer = []
        for x in range(1,n+1):
            if x not in back: answer.append(x);
        answer.sort()
        if len(answer) == 0:
            print('*')
        else:
            r = ''
            for y in answer:
                r += str(y)+' '
            print(r)
    except EOFError:
        break
