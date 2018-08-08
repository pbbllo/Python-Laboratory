#Uri Questions
#Python
#Instruções do Robô
for e in range(int(input())):
    move = []
    for x in range(int(input())):
        string = input().split()
        if string == ['LEFT']:
            move.append(-1)
        elif string == ['RIGHT']:
            move.append(1)
        else:
            a = int(string[2])
            move.append(move[a-1])
    print(sum(move))
