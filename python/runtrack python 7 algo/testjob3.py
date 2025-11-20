def tapis(n):
    for x in range(n + 1):
        for y in range(n + 1):
            if x == y:          # Si on est sur la diagonale
                print("+", end=" ")
            else:
                print(" ", end="#")
        print()  # nouvelle ligne

# Exemple :
tapis(16)
