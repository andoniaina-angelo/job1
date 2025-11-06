a=float(input("longueur coté a = " ))
b= float(input("longueur coté b = " ))
c=float(input("longueur coté c = " ))
if a+b <c or a+c <b or b+c <a:
    print("les longueurs ne permettent pas d'avoir un triangle")
if a==b==c:
    print("ce triangle est équilatérale")
if (a==b or c==b and a==c ) and not (a == b == c)  :
    print("ce triangle est isocèle")
if a==(b**2+c**2)**0.5 or b==(a**2+c**2)**0.5 or c==(a**2+b**2)**0.5 : 
    print("le triengle est rectangle")
if a!=b!=c and not a==(b**2+c**2)**0.5 or b==(a**2+c**2)**0.5 or c==(a**2+b**2)**0.5 :
    print(" ceci est triangle quelconque/scalène")
