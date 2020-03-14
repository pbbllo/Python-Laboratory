#Instance Examples
'''
Enter = INICIO OP 1 OP 2 OP 3 FIM / Out = 6
Enter = INICIO LOOP 10 OP 4 LOOP 3 LOOP 5 OP 1 FIM OP 2 FIM OP 1 FIM OP 17 FIM / Out = 277
Enter = INICIO OP 199 LOOP 10 LOOP 10 OP 1 FIM FIM FIM / Out = 299
'''

instance = input().split()
pile = []
total = 0

for word in instance:
    
    if word == "FIM":
        while word != "LOOP" and word != "INICIO":
            word = pile.pop()
            if word.isnumeric():
                num = int(word)
            elif word == "OP":
                total += num
            elif word == "LOOP":
                total *= num
                
    else:
        pile.append(word)
        
print(total)

        
