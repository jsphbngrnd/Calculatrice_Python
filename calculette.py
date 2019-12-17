print('Début travail calculette')

# On déclare les différentes variables

select = input("Sélectionner le type d'opération 1,2,3,4:")

Donnée_1 = int(input("Entrez premier chiffre"))
Donnée_2 = int(input("Entrez second chiffre"))

# On annonce les différents types d'opération

# Addition

if select == 1:
    print(Donnée_1+Donnée_2)

# Soustraction

elif select == 2:
    print(Donnée_1-Donnée_2)

# Multiplication

elif select == 3:
    print(Donnée_1*Donnée_2)

# Division

elif select == 4:
    print(Donnée_1/Donnée_2)

else:
    print("Invalide")
