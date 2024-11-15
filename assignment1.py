# Declaring variables that will hold the inputed values

num1 = float(input('Enter first number'))
num2 = float(input('Enter second number'))
operation = input('enter operation sign. E.g -, +, /, or *')

#Using conditional statement to check for operation value

if operation == '-':
    result = num1 - num2
elif operation == '+':
    result = num1 + num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1/num2
    else:
        result = "You can't divide by 0."
else:
    result = "Invalid operation."

#Outputing or printing the result value

print('Result: ', result)


