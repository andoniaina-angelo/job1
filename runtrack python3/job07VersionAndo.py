index = 0
ligne = 1
chaine = "abcdefghijklmnopqrstuvwxyz"*10
while index + ligne <= len(chaine):
    print(chaine[ 0:ligne])  # on prend une “tranche” de la chaîne
    index += ligne  # on avance dans la chaîne
    ligne += 1      # la prochaine ligne sera plus longue
