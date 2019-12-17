# Calculatrice_Python

Une calculatrice en python

# Explication création d'une calculatrice en Python

## Étape 1

Pour commencer nous allons déclarer plusieurs variables.

Variable **select** va permettre à l'utilisateur d'annoncer le type d'opération qu'il va vouloir effectuer.

Variable **A** permet à l'utilisateur d'entrer le **premier numéro** de son opération.
Variable **B** permet à l'utilisateur d'entrer le **second numéro** de son opération

## Étape 2 - Addition

Nous commençons par l'addition (il n'y a pas d'ordre particulier à suivre, j'ai choisi de faire dans cet ordre : addition, soustraction, multiplication, division).

Nous commençons par vérifier la valeur de la variable **select** avec un if.
Puis nous allons déclarer la variable **resultadd** correspondant au résultat de la somme de nos variables **A** et **B**
Enfin nous affichons un résultat grâce à un print de **resultadd**

## Étape 3 - Soustraction

Suivre la même logique que pour l'addition en remplaçant if par elif.
Déclarer une nouvelle variable **resultsub**.
Print du résultat.

## Étape 4 - Multiplication

Suivre la même logique que pour l'addition en remplaçant if par elif.
Déclarer une nouvelle variable **resultmult**.
Print du résultat.

## Étape 5 - Division

Suivre la même logique que pour l'addition en remplaçant if par elif.
Déclarer une nouvelle variable **resultdiv**.
Print du résultat.

## Étape 6 - Entrée invalide

Enfin faire un else pour déclarer ce qu'il se passe dans le cas d'une erreur d'entrée.
Print "Invalide"

| Variable   | Input type |
| ---------- | :--------: |
| select     |   String   |
| A          |  Integer   |
| B          |  Integer   |
| resultadd  |  Integer   |
| resultsub  |  Integer   |
| resultmult |  Integer   |
| resultdiv  |  Integer   |
