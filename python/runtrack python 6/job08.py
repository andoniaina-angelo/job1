""" L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
for L%2=0 in L:
    res = sum(L)
print(res) """
""" L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
i=0
while i < len(L):
    if L[i]%2!=0:
        del L[i]
    else:
        i+=1
res =sum(L)
print(res)
 """
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
""" sum_even = sum(x for x in L if x % 2 == 0)
print(sum_even) """
