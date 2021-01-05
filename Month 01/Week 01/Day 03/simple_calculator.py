from art import calc_art, calc_logo

print(calc_logo)
print(calc_art)

#Addition
def add(n1, n2):
    return n1, n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiplication
def multiply(n1, n2):
    return n1 * n2

#Division
def divide(n1, n2):
    n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 =int(input("What's the first number?"))
num2 =int(input("What's the second number?"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation symbol from the lines above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")