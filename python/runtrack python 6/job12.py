L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def calc():
    compteur=0
    for _ in L:
        compteur+=1
    return compteur

v= calc()
print (v)
i=0
while i<v:
    c=i+1
    while c<v:
        if L[i] > L[c]:
            L[i],L[c]=L[c],L[i]
        c+=1
    i+=1 
print(L)  