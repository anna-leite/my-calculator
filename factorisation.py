list = []
num = 2
char = '-'
sign = 0
tens = 12
dot = 1
decimals = 100

def reset_variables(num, tens, dot, decimals):
    # fonction qui réinitialise les variables 
    num = 0
    tens = 1
    dot = 0
    decimals = 10
    return num, tens, dot, decimals

def is_negative_number(char, num, sign, tens, dot, decimals, list):
    # détermine si un nombre est négatif
    # par défault la variable sign détermine un positif
    if char == '-':
        sign = '-' # la variable signe prends '-' pour un négatif
        if num != 0: # si le num est non nul (un nombre est stocker dedans) 
                     # alors il est ajouter à list et réinitialisation des variables
            list.append(num)
            num, tens, dot, decimals = reset_variables(num, tens, dot, decimals)

            my_list=[num, sign, tens, dot, decimals, list]

    return my_list

num, sign, tens, dot, decimals, list = is_negative_number(char, num, sign, tens, dot, decimals, list)

num = is_negative_number()[0]
print(num)

print(num, sign, tens, dot, decimals, list)


    








    

