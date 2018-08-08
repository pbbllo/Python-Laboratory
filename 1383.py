# Uri-Questions
#Python
#Sudoku
for n in range(int(input())): #números de casos testes
    sudoku = [[int(x) for x in input().split()]for y in range(9)]
    solve = True
    for l in sudoku:#Confere as linhas
        if solve:
            for ll in l:
                if l.count(ll) > 1:
                    solve = False
        else: break;
    if solve:#Confere as colunas
        for c in range(9):
            coluna = [sudoku[a][c] for a in range(9)]
            if solve:
                for cc in coluna:
                    if coluna.count(cc) > 1:
                        solve = False
            else: break;
    if solve:#Confere os blocos de 3x3
        line = start = 0
        bloco = 0
        limite = 3
        while bloco < 9:
            cont = 0
            hai = []
            if solve:
                if bloco % 3 == 0:
                    line = 0
                    start = bloco
                    limite = bloco + 3
                while cont < 3:
                    cont += 1
                    for z in range(start,limite):
                        hai.append(sudoku[line][z])
                    line += 1
                for read in hai:
                    if hai.count(read) > 1:
                        solve = False
                bloco += 1
            else: break;
    print('Instancia %d'%(n+1))
    if solve:
        print('SIM')
        print()
    else:
        print('NAO')
        print()
