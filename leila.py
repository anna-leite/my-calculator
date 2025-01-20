def reset_variables(num, sign, tens, dot, decimals):
    # fonction qui réinitialise les variables 
    num = 0
    sign = '+'
    tens = 1
    dot = 0
    decimals = 10
    return num, sign, tens, dot, decimals

def input_operation():
    # cette fonction parcour une chaine de caractère, grace à une boucle, afin d'en isolé et retourné nombre et opérateur d'une opération valide
    # elle gère les erreurs de saisie
    # elle retourne un liste qui contient une opération valide 

    test = False # variable boléenne, condition de sortie de la boucle "while" 

    # boucle de test pour une saisie correct, gère les erreurs de saisie
    while test == False:

        # initialisation des variables :
        num = 0  # variable pour stocker un nombre, initialiser à 0 pour le besion des opérations 
        sign = '+' # variable pour stocker le signe d'un nombre, posotif par défault
        tens = 1 # variable pour la gestion des dizaines des grands nombres
        dot = 0 # variable qui contrôle le type float
        decimals = 10 # varible pour la gestion des chiffres après la virgule
        list = [] # la varible list va récupérer les caractère de la saisie opération

        operation = input("Enter an operation : ",).replace(" ", "") # la varialble operation est une string qui est entrée par l'utilisateur

        # boucle qui parcours chaque caractères de la string de la variable opératiion 
        for i, char in enumerate(operation):
            # condition pour verifier une division par 0
            if char == '/':
                if operation[i+1] == '0':
                    print("Operation impossible. Try again")
                    break

            #condition pour vérifier si le nombre est positif ou négatif
            elif char == "-": 
                if num != 0: # si la variable num contient un nombre, il est renvoyé dans la list
                    list.append(num)
                    # puis réinitialisation des variables afin de trier les prochains caractères
                    num, sign, tens, dot, decimals = reset_variables(num, sign, tens, dot, decimals)

                sign = '-' # sign prend la string '-'
                continue 

            # condition pour savoir si le nombre est un float 
            elif char == '.':
                if dot == 1: # gestion d'erreur si il ya deux points dans un chiffre
                    print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                    break

                num = float(num) # si char est un point alors num est un flot
                dot = 1 # au premier point, dot = 1 pour vérifier si il n'y a pas de deuxième point
                continue
                
            # condition si char est un chiffre :
            elif char.isnumeric(): 
                if type(num) == int: # si num est un entier
                        num = num * tens + int(sign + char) # char est adittioner à "-" et retourné en entier, 
                        # (num * tens) pour controler les dizaines
                        tens = 10 # la variable prend la valeur 10 décaler d'une dizaine à chaque boucle jusqu'à ce que le nombre soit ajouté à list
                elif type(num) == float: # si num est un numbre à virgule
                    num = num + (float(sign + char) / decimals) # (float(char) / décimals) gère la place après la virgule
                    decimals = decimals * 10 # la variable decimals est multipliée par 10 à chaque boucle tant que le num n'est pas ajouté à list


            # condition si char correspond à un opérateur pris en charge par le programme
            elif char == "+" or char == "*" or char == "/" or char == '%' or char == '^':
                list.append(num) # num est ajouté à list
                num, sign, tens, dot, decimals = reset_variables(num, sign, tens, dot, decimals)
                list.append(char) # la string de l'opérateur est ajouté à list
                continue

            else : # condition pour toute autre caractère saisie
                print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                break

            
            # condition tester à chaque boucle : si char est le dernier caractère de la string operation
            if i == (len(operation)-1):
                if not char.isnumeric(): # si un opérateur est le dernier caractère de opération
                    print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                    break
                else:
                    list.append(num)  # num est ajouté à list
                    if len(list) == 1 : # si list ne contient qu'un élément
                        print("Invalid input. Please enter a correct operation with at least two numbers (float or integer) and operator choosen between +, -, *, / :")
                        break

                    test = True # condition de sortie de boucle

    return list

def calculator(list):
    # cette fonction réalise des opération mathématique selon les règles de priorité.
    # elle prend en paramètre une liste composé de nombre et d'opérateur qui propose une opération correct (sauf pour diviser 0)

    result = 0 # la variable résultat est initialisé à 0

    while len(list) != 1: # la condition de sortie de la boucle est que list ne contienne plus que 1 élément (qui sera le résultat)

        test = False
        # la première boucle réalise toute les opération de puissance de list, la plus prioritaire de toute les opérations mathématiques
        while test == False :
            # la boucle for parcours tout les éléments de list
            for i in range(0, len(list)):

                if i == (len(list)-1): # si le programme lit le dernier élément alors on sort de la boucle "while"
                    test = True
                    break
                if list[i] == '^': # si le programme détecte la saisie "^"
                    list[i] = list[i-1] ** list[i+1] # le programme réalise l'opération
                    list.pop(i+1) # le programme supprime les nombres qui ont été utilisé, list ne contient plus que le résultat de l'opération
                    list.pop(i-1)
                    break # on sort de la boucle 'for' pour recommencer à parcourir list grâce à la boucle "while"

        test = False
        # cette boucle "while" gère les opération de division, multiplication et modulo selon la méthode de la boucle précédente
        while test == False :
            for i in range(0, len(list)):
                if i == (len(list)-1):
                    test = True
                    break
                if list[i] == '*' or list[i] == '/' or list[i] == '%':
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
        # enfin cette boucle gère les additions et soustractions
        # attention : les soustraction sont repérée lorsqu'il n'y a pas d'opérateur entre deux nombres, le deuxième nombre étant obligatoirement négatif
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
    
    # lorsqu'il ne reste qu'une seule valeur dans list, c'est le résultat!
    result = list[0]                    
    return result

def main():
    # fonction qui demande une opération et retourne un résultat
    result = 0
    list = input_operation()
    result = calculator(list)
    print(" = ", result)


# Function to store the history of calculations in a separate .txt file
def log_calculation(calculation):
    with open("calculations.txt", "a") as file:
        file.write(calculation + "\n")

# Function to display the history of calculations for the user
def history():
    try:
        with open("calculations.txt", "r") as file:
            calculations = file.readlines()
            if calculations:
                for calc in calculations:
                    print(calc.strip())
            else:
                print("Pas de calculs antérieurs à montrer.")
    except FileNotFoundError:
        print("Pas de calculs antérieurs à montrer.")

# function to manage user choice
def select_op(choice):
    if choice == '?':
        return history()
    if choice == '#':
        return -1
    elif choice == '!':
        return 0
    elif choice in ('+'):
        main()


# ATTENTION LOG HISTORIQUE
    

while True:
    print("          --------------------------")
    print("          |  CALCULATRICE PYTHON   |")
    print("          --------------------------")
    print("          |      Calculator: +     |")
    print("          |   Réinitialiser: !     |")
    print("          |      Historique: ?     |")
    print("          |          Fermer: #     |")
    print("          --------------------------")

    # Take input from the user
    choice = input("Saisir le choix [+] [!] [?] [#] ")
    if select_op(choice) == -1:
        # End program
        print("Fermé.")
        exit()