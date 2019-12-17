print('Début travail calculette')

# On déclare les différentes variables

select = input("Sélectionner le type d'opération 1,2,3,4 : ")

A = int(input("Entrez premier chiffre : "))
B = int(input("Entrez second chiffre : "))

# On annonce les différents types d'opération

# Addition

if select == "1":
    resultadd = A + B
    print(resultadd)

# Soustraction

elif select == "2":
    resultsub = A - B
    print(resultsub)

# Multiplication

elif select == "3":
    resultmult = A * B
    print(resultmult)

# Division

elif select == "4":
    resultdiv = A / B
    print(resultdiv)

# Autre entrée

else:
    print("Invalide")
