
i=0
c=0
v=0
v+=1
g=int(input("hauteur du triangle :" ))-1
v=g
x=0
x=g+1
while c<=g :
    if c==0: 
        
        print(" "*x,"/\\")
        c+=1
    elif c<g:
        print(" "*v,"/"," "*i,"\\")
        i+=2 
        c+=1
        v-=1
    elif c==g:
        print(" "*v,"/","_"*i,"\\")
        break
