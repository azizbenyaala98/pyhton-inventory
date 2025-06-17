
# Exercice : Gestion de stock 
# Objectif : Implémenter un système simple de gestion de stock en utilisant uniquement des listes (arrays).
# Chaque fonction doit être complétée par l'étudiant.

# Déclaration des listes globales
produits = ["toffe7","tomate"]     # Liste des noms des produits
quantites = [50,20]    # Liste des quantités disponibles pour chaque produit
prix = [5.5,2.2]        # Liste des prix unitaires pour chaque produit

# 1. Afficher les produits
# Afficher chaque produit avec sa quantité et son prix.
# Si la liste est vide, indiquer qu'aucun produit n'est en stock.

def afficher_produits():
    for i in range (len(produits)) :
        print("nom du produit : "+produits[i]+" la quantité "+str(quantites[i])+" son prix unitaire "+str(prix[i]))
    # À compléter par l'étudiant


    pass

# 2. Ajouter un produit
# Demander à l'utilisateur un nom de produit, une quantité et un prix.
# Ne pas ajouter le produit s'il existe déjà dans la liste.
def ajouter_produit():
    # À compléter par l'étudiant
    pass

# 3. Modifier la quantité d’un produit
# Demander le nom du produit, et une quantité à ajouter ou retirer.
# Vérifier que la quantité totale ne devient pas négative.
def modifier_quantite():
    # À compléter par l'étudiant
    pass


# 4. Modifier le prix d’un produit
# Demander le nom du produit, et le nouveau prix à appliquer.
def modifier_prix():
    # À compléter par l'étudiant
    pass

# 5. Supprimer un produit
# Demander le nom du produit à supprimer, et le retirer des trois listes s’il existe.
def supprimer_produit():
    # À compléter par l'étudiant
    pass

# 6. Acheter un produit
# Demander le nom du produit et la quantité souhaitée.
# Vérifier que le stock est suffisant, afficher le coût total, et réduire la quantité.

def acheter_produit():
    # À compléter par l'étudiant
    pass

# 7. Produit le plus cher
# Trouver et afficher le produit ayant le prix le plus élevé.
def produit_plus_cher():
    # À compléter par l'étudiant
    pass

# 8. Valeur totale du stock
# Calculer la valeur totale du stock en multipliant quantité * prix pour chaque produit.
def valeur_totale():
    # À compléter par l'étudiant
    pass

# 9. Menu principal# Proposer un menu en boucle pour 

#utiliser toutes les fonctionnalités du programme.
def menu():
    # À compléter par l'étudiant
    pass

# Décommenter la ligne suivante après avoir implémenté les fonctions :
# menu()
afficher_produits()
