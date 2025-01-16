# Simple calculator program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erreur : La division par zéro n'est pas possible.")
        return None

# Function to raise one number to the power of the second number 
def power(a, b):
    return a ** b

# Function to show the remainder when one number is divided by a second number
def remainder(a, b):
    return a % b

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
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            num1s = input("Saisir le premier numéro : ")
            if num1s.endswith('!'): # Reset program
                return 0
            if num1s.endswith('#'): # End program
                return -1

            try:
                num1 = float(num1s)
                break
            except ValueError:
                print("Le numéro n'est pas valide, veuillez le saisir à nouveau.")
                continue

        while True:
            num2s = input("Saisir le deuxième numéro : ")
            if num2s.endswith('!'): # Reset program
                return 0
            if num2s.endswith('#'): # End program
                return -1
            try:
                num2 = float(num2s)
                break
            except ValueError:
                print("Le numéro n'est pas valide, veuillez le saisir à nouveau.")
                continue

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Quelque chose n'a pas fonctionné.")

        if result is not None:  # Only log if the result is valid
            last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
            print(last_calculation)
            log_calculation(last_calculation)
    else:
        print("Opération non reconnue")

while True:
    print("          --------------------------")
    print("          |  CALCULATRICE PYTHON   |")
    print("          --------------------------")
    print("          |         Ajouter: +     |")
    print("          |      Soustraire: -     |")
    print("          |      Multiplier: *     |")
    print("          |         Diviser: /     |")
    print("          |       Puissance: ^     |")
    print("          |    Modulo/Reste: %     |")
    print("          |   Réinitialiser: !     |")
    print("          |      Historique: ?     |")
    print("          |          Fermer: #     |")
    print("          --------------------------")

    # Take input from the user
    choice = input("Saisir le choix [+] [-] [*] [/] [^] [%] [#] [!] [?] ")
    if select_op(choice) == -1:
        # End program
        print("Fermé.")
        exit()