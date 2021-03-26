#Program to check the sudoku 9x9 answer

def lines(array): #Check the lines, complexity O(1)
    if sum(array) == 45:
        return True
    else:
        return False

def columns(column, sudoku): #Check the colunms, complexity O(1)
    somatory = 0
    for line in range(9):
        somatory += sudoku[line][column]
    if somatory == 45:
        return True
    else:
        return False

def isCorrect(sudoku): #Complexity O(1)
    solve = True
    iteration = 0
    while solve and iteration < 9:            
        if not lines(sudoku[iteration]):
            solve = False
        if solve:
            if not columns(iteration, sudoku):
                solve = False
        
        iteration += 1

    if solve:
        print("\nThe sudoku answer is correct! :)")
    else:
        print("\nThe sudoku answer is wrong! :(")
        print("Look to the line {} or column {} to fix the error".format(iteration + 1, iteration + 1))


print("Input the lines of the sudoku, for example --> 1 2 3 4 5 6 7 8 9")
sudoku = [
    [int(i) for i in input("Line {}: ".format(j + 1)).split()]
    for j in range(9)
    ]

isCorrect(sudoku)