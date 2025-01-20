
def input_operation():
    # initialisation des variables :
    num = 0  
    sign = 0
    dot = 0
    f = 1
    d = 10
    list = []
    test = False
    operation = input("Enter an operation : ",)

    while test == False:
        for i, char in enumerate(operation):
    # ATTENTION GESTION DES ERREURS DE SAISI ET D'OPERATION PAR 0
            if char == "-":
                sign = "-"
                if num != 0:
                    list.append(num)
                    num = 0
                    dot = 0
                    f = 1
                    d = 10
                    continue

            elif char.isnumeric() and type(num) != float:
                if sign == '-':
                    num = num * f + int(sign + char)
                else:
                    num = num * f + int(sign + int(char))
                sign = 0
                f = 10

            elif char == '.':
                if dot == 1:
                    print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                    operation = input("Try again : ",)
                    num = 0
                    dot = 0
                    f = 1
                    d = 10
                    break

                num = float(num)
                dot = 1
                continue

            elif char.isnumeric() and type(num) == float:
                num = num + (float(char) / d)
                d = d * 10
    
            elif char == ' ':
                if num != 0:
                    list.append(num)
                    num = 0
                    dot = 0
                    f = 1
                    d = 10
                continue

            elif char == "+" or char == "*" or char == "/" or char == '%' or char == '^':
                if num != 0:
                    list.append(num)
                    num = 0
                    dot = 0
                    f = 1
                    d = 10
                list.append(char)
                continue

            else :
                print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                operation = input("Try again : ",)
                num = 0
                f = 1
                d = 10
                break

            if i == (len(operation)-1):
                if not char.isnumeric():
                    print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                    operation = input("Try again : ",)
                    break

                else:
                    list.append(num)
                    test = True

    return list

def zero_division(sum, list):
        test = False
        while test == False :
            for i in range(0, len(list)):
                if i == (len(list)-1):
                    test = True
                    break
                elif list[i] == '/':
                    try:
                        list[i-1] / list[i+1]
                    except ZeroDivisionError: 
                            print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                            sum = None
                    else:
                        sum = 0
        return sum
                    


def calculator(list):
    sum = 0
    while len(list) != 1:
        test = False
        while test == False :
            for i in range(0, len(list)):
                if i == (len(list)-1):
                    test = True
                    break
                if list[i] == '^':
                    list[i] = list[i-1] ** list[i+1]
                    list.pop(i+1)
                    list.pop(i-1)
                    break

        test = False
        while test == False :
            for i in range(0, len(list)):
                if i == (len(list)-1):
                    test = True
                    break
                if list[i] == '*' or list[i] == '/':
                    if list[i] =='*':
                        list[i] = list[i-1] * list[i+1]
                        list.pop(i+1)
                        list.pop(i-1)
                        break
                    elif list[i] == '/':
                        list[i] = list[i-1] / list[i+1]
                        list.pop(i+1)
                        list.pop(i-1)
                        break 
                    elif list[i] == '%':
                        list[1] = list[i-1] % list[i+1]
                        list.pop(i+1)
                        list.pop(i-1)
                        break

    
        test = False
        while test == False: 
            for i in range(0, len(list)):
                if i == (len(list)-1):
                    test = True
                    break
                if list[i] == '+':
                    if list[i] == '+':
                        list[i] = list[i-1] + list[i+1]
                        list.pop(i+1)
                        list.pop(i-1)
                        break
                elif type(list[i]) == int or type(list[i]) == float:
                    if type(list[i+1]) == int or type(list[i+1]) == float:
                        list[i] = list[i] + list[i+1]
                        list.pop(i+1)
                        break

    sum = list[0]                    
    return sum

def main():
    sum = None
    list = []
    list = input_operation()
    while sum == None:
        sum = zero_division(sum, list)
        if sum == 0:
            continue
        list = input_operation()
        
    sum = calculator(list)


    print(sum)

main()

    




    
        
