
# function to input an opération and return a list
def input_operation(a, b, sign):
    a = float(input("Enter a number: ", ))
    sign = input("Enter an operator (+, -, *, /): ", )
    b = float(input("Enter another number: ", ))
    return a, b, sign



def addition(a, b):
    return  a + b
    
def subtration(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculator(a, b, sign):
    if sign == "+":
        print(addition(a, b))
    elif sign == "-":
        print(subtration(a, b))
    elif sign == "*":
        print(multiplication(a, b))
    elif sign == "/":
        print(division(a, b))

def main():
    a = 0
    b = 0
    sign = 0
    a, b, sign = input_operation(a, b, sign)
    print(f"{a} {sign} {b} =")
    calculator(a, b, sign)



main()



