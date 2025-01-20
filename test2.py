def reset_variables():
    num = 0
    num_sign = '+'
    tens = 1
    dot = False
    decimals = 10
    return num, num_sign, tens, dot, decimals
                
def input_operation():
    """cette fonction parcour une chaine de caractère, grace à une boucle, afin d'en isolé et retourné nombre et opérateur d'une opération valide
    elle gère les erreurs de saisie
    elle retourne un liste qui contient une opération valide""" 

    valid_input = True 

    while valid_input:
        num, num_sign, tens, dot, decimals = reset_variables()
        operation_parsed = [] # la varible operation_parsed va récupérer les caractère de la saisie opération

        input_string = input("Enter an input : ",).replace(" ", "") # la varialble _input est une string qui est entrée par l'utilisateur

        for i, char in enumerate(input_string):

            # verifie une erreur de division par zéro
            if char == '/':
                if input_string[i+1] == '0':
                    print("Operation impossible. Try again")
                    break

            # vérifie si le nombre est positif ou négatif
            if char == "-": 
                if num != 0: # si la variable num contient un nombre, il est renvoyé dans la list
                    operation_parsed.append(num)
                    # puis réinitialisation des variables afin de trier les prochains caractères
                    num, num_sign, tens, dot, decimals = reset_variables()

                num_sign = '-' # num_sign prend la string '-'
                continue 

            # verifie si le nombre est un float 
            elif char == '.':
                if dot: # gestion d'erreur si il ya deux points dans un chiffre
                    print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                    break

                num = float(num) # si char est un point alors num est un flot
                dot = True # au premier point, dot = True pour vérifier si il n'y a pas de deuxième point
                continue
                
            # verifie si char est un chiffre :
            elif char.isnumeric(): 
                if type(num) == int: 
                        num = num * tens + int(num_sign + char) # char est adittioner à "-" et retourné en entier, (num * tens) pour controler les dizaines
                        tens = 10 # la variable prend la valeur 10 décaler d'une dizaine à chaque boucle jusqu'à ce que le nombre soit ajouté à operation_parsed
                elif type(num) == float: 
                    num = num + (float(num_sign + char) / decimals) # (float(char) / décimals) gère la place après la virgule
                    decimals = decimals * 10 # la variable decimals est multipliée par 10 à chaque boucle tant que le num n'est pas ajouté à operation_parsed


            # verifie si char correspond à un opérateur pris en charge par le programme
            elif char == "+" or char == "*" or char == "/" or char == '%' or char == '^':
                operation_parsed.append(num) 
                num, num_sign, tens, dot, decimals = reset_variables()
                operation_parsed.append(char) 
                continue

            else : # toute autre caractère saisie
                print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                break

            
            # verifie si char est le dernier caractère de la string operation
            if i == (len(input_string)-1):
                if not char.isnumeric():
                    print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                    break
                else:
                    operation_parsed.append(num)  
                    if len(operation_parsed) == 1 : 
                        print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                        break

                    valid_input = False

    return operation_parsed

def calculator(operation_parsed):
    """cette fonction réalise des opération mathématique selon les règles de priorité.
    elle prend en paramètre une liste composé de nombre et d'opérateur qui propose une opération correct (sauf pour diviser 0)"""

    result = 0 

    while len(operation_parsed) != 1: # la condition de sortie de la boucle est que operation_parsed ne contienne plus que 1 élément (qui sera le résultat)
        remaining_operation = True
        # la première boucle réalise toute les opération de puissance de operation_parsed, la plus prioritaire de toute les opérations mathématiques
        while remaining_operation :
            for i in range(0, len(operation_parsed)):
                if i == (len(operation_parsed)-1):
                    remaining_operation = False
                    break
                if operation_parsed[i] == '^': 
                    operation_parsed[i] = operation_parsed[i-1] ** operation_parsed[i+1] 
                    operation_parsed.pop(i+1) # supprime les nombres qui ont été utilisé, operation_parsed ne contient plus que le résultat de l'opération
                    operation_parsed.pop(i-1)
                    break 

        remaining_operation = True
        # cette boucle "while" gère les opération de division, multiplication et modulo selon la méthode de la boucle précédente
        while remaining_operation:
            for i in range(0, len(operation_parsed)):
                if i == (len(operation_parsed)-1):
                    remaining_operation = False
                    break
                if operation_parsed[i] == '*' or operation_parsed[i] == '/' or operation_parsed[i] == '%':
                    if operation_parsed[i] =='*':
                        operation_parsed[i] = operation_parsed[i-1] * operation_parsed[i+1]
                        operation_parsed.pop(i+1)
                        operation_parsed.pop(i-1)
                        break
                    elif operation_parsed[i] == '/':
                        operation_parsed[i] = operation_parsed[i-1] / operation_parsed[i+1]
                        operation_parsed.pop(i+1)
                        operation_parsed.pop(i-1)
                        break 
                    elif operation_parsed[i] == '%':
                        operation_parsed[1] = operation_parsed[i-1] % operation_parsed[i+1]
                        operation_parsed.pop(i+1)
                        operation_parsed.pop(i-1)
                        break

    
        remaining_operation = True
        # enfin cette boucle gère les additions et soustractions
        # attention : les soustraction sont repérée lorsqu'il n'y a pas d'opérateur entre deux nombres, le deuxième nombre étant obligatoirement négatif
        while remaining_operation: 
            for i in range(0, len(operation_parsed)):
                if i == (len(operation_parsed)-1):
                    remaining_operation = False
                    break
                if operation_parsed[i] == '+':
                    if operation_parsed[i] == '+':
                        operation_parsed[i] = operation_parsed[i-1] + operation_parsed[i+1]
                        operation_parsed.pop(i+1)
                        operation_parsed.pop(i-1)
                        break
                elif type(operation_parsed[i]) == int or type(operation_parsed[i]) == float:
                    if type(operation_parsed[i+1]) == int or type(operation_parsed[i+1]) == float:
                        operation_parsed[i] = operation_parsed[i] + operation_parsed[i+1]
                        operation_parsed.pop(i+1)
                        break
    
    # lorsqu'il ne reste qu'une seule valeur dans operation_parsed, c'est le résultat!
    result = operation_parsed[0]                    
    return result

def main():
    operation_parsed = input_operation()
    result = calculator(operation_parsed)
    print(" = ", result)

main()

    




    
        
