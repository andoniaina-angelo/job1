L=[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
i=0
while i<len(L):
    if L[i]<25 :
        del L[i]
    
    elif  L[i]>90:
        del L[i]
    else:
        i+=1 
""" import math
res =math.prod(L) """
res =1
for x in L:
    
    res*=x
print (res)
