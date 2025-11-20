""" def tapis(n):
    def draw_rectangle(Width,height):
    
        print("+","#"*Width,"+")
        i=0
        while i!= height-2:
            print("|"," "*Width,"|")
            i+=1
            print( "+","#"*Width,"+")
    draw_rectangle(13,13)
tapis(10) """

""" print(tableau[0][0])  # 1 (ligne 0, colonne 0)
print(tableau[1][2])  # 6 (ligne 1, colonne 2)
for i in range(len(tableau)):        # lignes
    for j in range(len(tableau[i])): # colonnes
        print(f"({i},{j}) = {tableau[i][j]}")
        # Création d'un tableau 5x5 initialisé avec des zéros """
""" N=10
tab = [['#' for _ in range(N+3)] for _ in range(N+3)]

# Définition de la dimension du tableau
N+1 == len(tab)

tab[0][1]="+"
x=2 
y=0

while tab[x][y]:
    if tab[x==2][y<N+3]:
        i=1
        print(i)
        y+=1
        i+=1
for ligne in tab:
    for truc in ligne:
        print(truc,i ,end="")
    print() """
N=10
tab = [['#' for _ in range(N+3)] for _ in range(N+3)]
i = 1
y=3
x=6

while y < N:
    if tab[x][y] == "#":
        print(i)
        i += 1
    y += 1
    x-=10