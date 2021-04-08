'''
-------- Problem -----------
Given a string made up of the following brackets: ()[]{},
determine whether the brackets properly match.

Examples:
input: [{}]     output: Valid
input: (()())   output: Valid
input: {]       output: Invalid
input: [()))()] output: Invalid
input: [        output: Invalid
input: ]        output: Invalid

'''
'''---Path to Implementations module---'''
import sys
sys.path.append('/home/shiro/Desktop/Python')

from Implementations.stack import Stack

def answer(string): #The Solution Complexity is O(n)
    stack = Stack()

    for substring in string:
        tail = stack.peek()
        join = tail + substring

        if (substring == "[") or (substring == "(") or (substring == "{"):
            stack.push(substring)
        elif (stack.isEmpty() == False) and ((join == "[]") or (join == "()") or (join == "{}")):
            stack.pop()
        else:
            return "Invalid"
    
    if stack.isEmpty():
        return "Valid"
    else:
        return "Invalid"

string = input()
print(answer(string))




