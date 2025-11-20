def diagonale(N):
    i=0
    c=0
    d=N
    m=0
    while c<=N+2:
   
        if c ==0 or c==N+2:
            print("+","-"*(N+3),"+")
            c+=1
            i+=1
        elif c>0:
            print("|","#"*d," ","#"*m,"|")
            c+=1
            i+=1
            d-=1
            m+=1
    print(i)
diagonale(9)