""" L=[1,2,3,4,5]
valeurtemps=L[4]
L[4]=L[0]
L[0]=valeurtemps
print(L) """

l = [1,2,3,4,5]
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)
