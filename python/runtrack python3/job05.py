i=2
while i <=1001:
    est_premier=True
    n=2
    while n<i :
     if i%n == 0:
        est_premier= False
        break
     n+=1  
    if est_premier:
        print(i)
    i +=1