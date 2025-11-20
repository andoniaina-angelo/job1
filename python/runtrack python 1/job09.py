prix = 1
nom = "pain"
quantité_du_stock = 666
print(f"Nom: {nom},prix:'prix{prix},quantité du stock:{quantité_du_stock},") 
nouveau_produit = int(input("quantité achat"))
quantité_du_stock += nouveau_produit
prix *= 1.10
print(f"stock mis à jour :{quantité_du_stock}")
print(f" prix mis a jour : {prix}")