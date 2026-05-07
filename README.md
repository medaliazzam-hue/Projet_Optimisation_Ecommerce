# Modélisation et Optimisation des Approvisionnements pour le Lancement d'une TPE E-commerce

**École Marocaine des Sciences de l'Ingénieur (EMSI)** **Matières :** Programmation Linéaire / Python  
**Auteurs :** Mohamed Ali Azzam
**Encadrants :** Pr. A. REHA, Pr. Yassine SAFSOUF  

---

## INTRODUCTION GÉNÉRALE

Dans un écosystème économique fortement numérisé, le secteur du e-commerce représente un vecteur de croissance incontournable. Cependant, le lancement d'une activité de vente en ligne se heurte invariablement au paradigme de la rareté des ressources : l'entrepreneur dispose d'un capital strictement limité, d'infrastructures logistiques réduites et d'une visibilité incertaine quant à l'absorption du marché. 

L'enjeu majeur de cette étude se résume par la question de recherche suivante : **« Comment allouer de manière optimale un budget d'investissement restreint et un espace de stockage limité entre différentes références de produits, de façon à maximiser le bénéfice net de la jeune entreprise ? »**

Pour répondre à cette problématique, ce projet applique les principes de la Recherche Opérationnelle, structuré en trois phases distinctes : la modélisation graphique, la résolution algébrique par le Simplexe, et l'automatisation informatique en Python.

---

## CHAPITRE 1 : MODÉLISATION ET RÉSOLUTION PAR LA MÉTHODE GRAPHIQUE

Ce chapitre modélise le lancement avec un catalogue restreint à deux produits pour permettre une visualisation géométrique du problème.

### 1.1. Modélisation Mathématique
* **Variables de décision :** * $x_1$ : Quantité d'Écouteurs sans fil à acquérir.
  * $x_2$ : Quantité de Batteries externes à acquérir.
* **Fonction Objectif (Maximisation du profit) :** $$Max(Z) = 70x_1 + 75x_2$$
* **Contraintes opérationnelles :**
  1. **Budget :** $50x_1 + 75x_2 \le 3000$
  2. **Stockage :** $x_1 + 2x_2 \le 60$
  3. **Demande globale :** $x_1 + x_2 \le 50$
  4. **Positivité :** $x_1 \ge 0, x_2 \ge 0$ (avec $x_1, x_2 \in \mathbb{N}$)

### 1.2. Interprétation
La résolution graphique (intersection des droites de contraintes) démontre que le point optimal se situe à la frontière de saturation des ressources budgétaires et spatiales.

---

## CHAPITRE 2 : MODÉLISATION ET RÉSOLUTION PAR LE SIMPLEXE

Pour simuler la croissance de l'entreprise, nous intégrons une troisième référence (gamme Premium) et une contrainte de temps logistique, nécessitant le passage à l'algorithme du Simplexe.

### 2.1. Le Système Élargi
* $x_3$ : Nombre d'Enceintes Bluetooth.
* **Nouvelle Fonction Objectif :** $$Max(Z) = 70x_1 + 75x_2 + 100x_3$$
* **Système sous forme standard (avec variables d'écart $e_1, e_2, e_3, e_4$) :**
  * $Z - 70x_1 - 75x_2 - 100x_3 = 0$
  * $50x_1 + 75x_2 + 100x_3 + e_1 = 3000$ (Budget)
  * $x_1 + 2x_2 + 3x_3 + e_2 = 60$ (Stockage)
  * $x_1 + x_2 + x_3 + e_3 = 50$ (Marché)
  * $5x_1 + 8x_2 + 12x_3 + e_4 = 300$ (Temps)

### 2.2. Résolution Algébrique (Tableau Final)
Après l'application rigoureuse des pivots de Gauss-Jordan (entrée de $x_3$ puis entrée de $x_1$), nous obtenons le tableau optimal suivant :

| Base | $Z$ | $x_1$ | $x_2$ | $x_3$ | $e_1$ | $e_2$ | $e_3$ | $e_4$ | Valeurs (RHS) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$L_0$** | 1 | 0 | 10 | 0 | 0 | 15 | 55 | 0 | **3650** |
| **$e_1$**| 0 | 0 | 0 | 0 | 1 | -25 | -25 | 0 | 250 |
| **$x_3$**| 0 | 0 | 1/2 | 1 | 0 | 1/2 | -1/2 | 0 | 5 |
| **$x_1$**| 0 | 1 | 1/2 | 0 | 0 | -1/2 | 3/2 | 0 | 45 |
| **$e_4$**| 0 | 0 | -1/2 | 0 | 0 | -7/2 | -3/2 | 1 | 15 |

*Test d'arrêt validé : Tous les coefficients de la ligne Z sont $\ge 0$.*

---

## CHAPITRE 3 : CONCEPTION INFORMATIQUE

### 3.1. Choix Technologique
L'automatisation a été réalisée en Python via la bibliothèque `pulp`, spécialisée dans l'optimisation combinatoire et la programmation linéaire.

### 3.2. Analyse des Résultats Informatiques
L'exécution du script `main.py` confirme rigoureusement les calculs manuels du Chapitre 2 :
* **$x_1^* = 45$** : Saturation de la demande en écouteurs.
* **$x_2^* = 0$** : Exclusion des batteries externes (volume logistique trop pénalisant face à la rentabilité).
* **$x_3^* = 5$** : Investissement du reliquat budgétaire dans les enceintes.
* **Profit net maximum ($Z^*$) : 3 650 DH.**

---

## CONCLUSION GÉNÉRALE

Ce projet a illustré l'importance des méthodes exactes d'optimisation dans la rationalisation des processus décisionnels en ingénierie d'affaires. Face à la complexité des ressources limitées, la Programmation Linéaire a permis de détecter des failles logistiques invisibles (l'encombrement critique des batteries) et de définir une stratégie de profit maximisée. 

Le développement d'une solution en Python constitue l'aboutissement de ce travail, transformant un concept mathématique en un outil logiciel automatisé. À terme, ce script pourrait être couplé à des modèles prédictifs d'Intelligence Artificielle pour anticiper les fluctuations du marché, transformant cette solution d'optimisation en une plateforme logistique proactive, indispensable à la pérennité d'une structure e-commerce.
