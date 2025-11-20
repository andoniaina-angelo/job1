L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
i=0
c=1
while i< len(L) and c<len(L):
    if L[i]<L[c]:
        L[i]=L[c]
        c+=1
    elif L[i]>L[c]:
        c+=1
print(f"valeur max ",L[i])
d=0
v=1
while d< len(L) and v<len(L):
    if L[d]>L[v]:
        L[d]=L[v]
        v+=1
    elif L[d]<L[v]:
        v+=1
print(f"valeur min ",L[d])