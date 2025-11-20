montant_initial_investis = 2000
taux_de_rendement = 0.04
gain_annuel = montant_initial_investis * taux_de_rendement
print(f"gain annuel en fonction du taux : {gain_annuel} €")
montant_initial_investis +=5000
taux_de_rendement +=0.02
gain_annuel=montant_initial_investis *taux_de_rendement
print(f"gain annuel en fonction du taux : {gain_annuel} €")
retrait = montant_initial_investis * 0.10
montant_initial_investis-= retrait
taux_de_rendement -=0.01
gain_annuel =montant_initial_investis * taux_de_rendement
print(f"gain annuel en fonction du taux : {gain_annuel} €")