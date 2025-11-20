
""" def pair_impair():
    b = float(input("Entre un nombre : "))

    if b < 0:
        return "Entrez un nombre positif"
    
    if b % 1 != 0:
        return "Entrez un nombre entier"
    
    if b % 2 == 0:
        print(f"Le nombre {b} est pair")
    else:
        print(f"Le nombre {b} est impair")

pair_impair()
result = pair_impair()
print(result) """

def pair_impair():
    b = input(("Entre un nombre : "))

    if b < 0:
        return "Entrez un nombre positif"
    
    if b % 2 != 0:
        return "Entrez un nombre entier"
    
    if b % 2 == 0:
        print(f"Le nombre {b} est pair")
    else:
        print(f"Le nombre {b} est impair")

pair_impair()
result = pair_impair()
print(result) 
