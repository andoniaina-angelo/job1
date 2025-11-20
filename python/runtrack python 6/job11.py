""" L = [7, 11, 42, 39, 2]
i=0
while i<len(L):
    L[i]+=1
    i+=1"""
L = [x + 1 for x in [7, 11, 42, 39, 2]]
print(L) 