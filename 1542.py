#Uri Questions
#Python
#Lendo Livros
while True:
    num = [int(x) for x in input().split()]
    if num == [0]: break;
    x = num[2]*num[1]/(num[2]-num[0])
    answer = int(x*num[0])
    if answer == 1: print(answer, 'pagina')
    else: print(answer, 'paginas')
