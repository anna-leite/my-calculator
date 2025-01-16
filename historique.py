# fichier = open("data.txt", "a", "r")
# fichier.write("Bonjour monde")
# print(fichier.read())


with open("data.txt", "r") as fichier:
    print(fichier.read())

with open("data.txt", "a") as fichier:
    fichier.write("\nBonjour monde!")


# with open("data.txt", "r") as fichier:
#     print(fichier.read())

with open("data.txt", "r+") as fichier:
    fichier.truncate()

with open("data.txt", "r") as fichier:
    print(fichier.read())

