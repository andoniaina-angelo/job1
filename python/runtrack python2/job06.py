""" # job06.py

# On demande à l'utilisateur de saisir un entier N
N = int(input("Entrez un entier : "))

# Initialisation du compteur
i = 1

# Boucle while pour afficher les 10 premiers résultats de la table de 7
while i <= N:
    resultat = i * 7
    print(f"{i} x 7 = {resultat}")
    i += 1
      """
i=1
N= int(input("entrez un entier : "))
for i in range(1,N+1):
    resultat = i*7
    print(f"{i}x7={resultat}")
    i+=1 