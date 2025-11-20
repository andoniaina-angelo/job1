def moyenne(a,b,c):
    moyenne=(a+b+c)/60*20
    if moyenne >= 15 and moyenne <=20:
        print("très bon élève")
    elif moyenne >= 11 and moyenne <=14:
        print("bon élève")
    elif moyenne >= 8 and moyenne <= 10:
        print("élève moyen")
    elif moyenne >=0 and moyenne<= 7:
        print("élève devant faire des éffort mais en vrai il doivent tous faire des effort ")
moyenne(int(input(f"note a:")),
    int(input(f"note b:")),
    int(input(f"note c:")))