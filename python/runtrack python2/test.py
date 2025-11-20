N = int(input("table à afficher : "))
i = 1
R = N * i
T = 1

while T <= N:
    while i < 11:
        print(f"table de multiplication : {T}")
        print(f"{N} x {i} = {R}")
        i += 1
        T += 1
