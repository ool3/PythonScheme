# Write a function called calculate that takes 3 values. The first and third values are numbers. The second value is a character. If the character is "+" , "-", "*", or "/", the function will return the result of the corresponding mathematical function on the two numbers. If the string is not one of the specified characters, the function should return null (throw an ArgumentException in C#).

# calculate(2,"+", 4); //Should return 6
# calculate(6,"-", 1.5); //Should return 4.5
# calculate(-4,"*", 8); //Should return -32
# calculate(49,"/", -7); //Should return -7
# calculate(8,"m", 2); //Should return null

# MY SOLUTION

def calculate(num1, operation, num2): 
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == 'm':
        return
    elif operation == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 
