""" i=1
while i in range(1,101):
    if i !=26 and i!=37 and i !=88 :
        print(i)
        i+=1
    else: 
        i+=1 """
N = ("nombre a afficher")
exclus = {26,37,88}
for N in range (0,101):
    if N not in exclus :
        print(N)
        