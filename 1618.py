#URI Questions
#Python
#Colisão
for n in range(int(input())):
    Ax,Ay,Bx,By,Cx,Cy,Dx,Dy,Rx,Ry = [int(x) for x in input().split()]
    if Ax <= Rx <= Bx and Ay <= Ry <= Dy:
        print('1')
    else:
        print('0')
