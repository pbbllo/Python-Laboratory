def suc(num):
    sucessor = num + 1
    return sucessor

def sum(num1, num2):
    if num2 == 0:
        return num1
    else:
        return sum(suc(num1), num2 - 1)
        
def multi(num1, num2):
    if num2 == 1:
        return num1
    elif num2 == 0 or num1 == 0:
        return 0
    else:
        return sum(num1, multi(num1, num2 - 1))       

print(multi(5, 5))

#The num2 value must be lower or equal than num1 value
