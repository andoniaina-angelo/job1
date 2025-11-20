liste=[10, 20,0, 20, 10, 50, 60, 40, 80, 50, 40,24,26,24,10]
i=0
def calc():
    compteur=0
    for _ in liste:
        compteur+=1
    return compteur
v=calc()
print(v)

while i <v-1:
    c=i+1
    print(i,c)
    while c<v:
        if liste[i]==liste[c]:
            del liste[c]
            v-=1
        
        else:
            c+=1
    i+=1

print(liste)