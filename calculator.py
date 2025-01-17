
# function to input an opération and return a list
def input_operation(a, b, sign):
    test = False
    while test == False:
        a = input("Enter a number: ", )
        try :
            a = float(a)
            if type(a) == float :
                test = True
        except ValueError : print("Invalid input. Please a valid number.") 

    test =  False
    while test == False:
        sign = input("Enter an operator (+, -, *, /): ", )
        if sign == "+" or sign == "-" or sign == "*" or sign == "/":
            test = True
        else:
            print("Invalid input. Please choose the operator between +, -, *, /.")
    
    test = False
    while test == False:
        b = input("Enter another number: ", )
        try :
            b = float(b)
            if b == 0:
                print("Operation impossible. Please enter another number.") 
            elif type(b) == float:
                test = True          
        except ValueError : print("Invalid input. Please enter a valid number.")

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


# division par 0
main()



