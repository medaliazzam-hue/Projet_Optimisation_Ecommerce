# ==========================================
# PROJET D'OPTIMISATION E-COMMERCE - EMSI
# Auteurs : Mohamed Ali Azzam
# Module : Programmation Linéaire / Python
# Encadrants : Pr. A. REHA / Pr. Yassine SAFSOUF
# ==========================================

import pulp

def optimiser_inventaire():
    """
    Modèle d'optimisation par Programmation Linéaire pour déterminer
    la stratégie d'approvisionnement e-commerce la plus rentable.
    """
    # 1. Création du problème (Objectif : Maximiser le profit)
    projet = pulp.LpProblem("Maximisation_Profit_Ecommerce", pulp.LpMaximize)

    # 2. Déclaration des variables de décision (Quantités = Entiers positifs)
    # x1 : Écouteurs sans fil
    # x2 : Batteries externes
    # x3 : Enceintes Bluetooth
    x1 = pulp.LpVariable('Ecouteurs', lowBound=0, cat='Integer')
    x2 = pulp.LpVariable('Batteries', lowBound=0, cat='Integer')
    x3 = pulp.LpVariable('Enceintes', lowBound=0, cat='Integer')

    # 3. Fonction Objectif (Z) : Les marges nettes
    projet += 70 * x1 + 75 * x2 + 100 * x3, "Profit_Total"

    # 4. Ajout des contraintes opérationnelles
    projet += 50 * x1 + 75 * x2 + 100 * x3 <= 3000, "Limite_Budget_DH"
    projet += 1 * x1 + 2 * x2 + 3 * x3 <= 60,   "Limite_Stockage_Volume"
    projet += 1 * x1 + 1 * x2 + 1 * x3 <= 50,   "Limite_Demande_Marche"
    projet += 5 * x1 + 8 * x2 + 12 * x3 <= 300, "Limite_Temps_Preparation"

    # 5. Exécution du Solveur
    projet.solve()

    # 6. Affichage structuré des résultats
    print("--- RÉSULTATS DE L'OPTIMISATION ---")
    print(f"Statut de la résolution : {pulp.LpStatus[projet.status]}")
    print("-" * 50)
    print("STRATÉGIE D'ACHAT OPTIMALE :")
    print(f" => Quantité d'Écouteurs (x1) : {int(x1.varValue)} unités")
    print(f" => Quantité de Batteries (x2) : {int(x2.varValue)} unités")
    print(f" => Quantité d'Enceintes (x3) : {int(x3.varValue)} unités")
    print("-" * 50)
    print(f"PROFIT NET MAXIMUM (Z) : {int(pulp.value(projet.objective))} DH")

if __name__ == "__main__":
    optimiser_inventaire()
