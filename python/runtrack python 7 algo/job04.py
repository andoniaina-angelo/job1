""" i=0
liste=[input("message à chiffrer: ").split]
N=int(input("clé de chiffrement: "))
while i <len(liste):
    liste[i]=chr(ord(liste[i])+N)
    if liste[i]=="z":
        liste[i]=chr(ord(liste[i]+N)%26)
    i+=1
print(liste) """

""" liste = ["input("message à chiffrer: ").]
liste[0] = "a" 
if liste[0] == "z" else chr(ord(liste[0]) + 1)
    print(liste)  # ['a']
 """
message = input("message à chiffrer: ")

resultat = ""

for c in message:
    if "a" <= c <= "z":
        # Décalage circulaire
        resultat += chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
    else:
        # On laisse les caractères non alphabétiques tels quels
        resultat += c

print(resultat)
