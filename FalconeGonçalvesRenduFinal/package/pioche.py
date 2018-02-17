##PIOCHE
from package.carte import *
from package.deckGen import *

import random
#Pour creer une pioche on utilise la fonction
#creer_carte et on ajoute ces cartes dans la pioche (on rappelle qu'au début de la partie il y a 9 Soldats, 6 Gardes et 5 Archers)

#Crée une pioche complète.
#Une pioche complète comprend 9 Soldats, 6 Gardes et 5 Archers
#Utiliser la fonction creer_carte pour remplir la pioche

#FG / Structure de donnée
# (Carte)[0] puis on append à chaque ajout (Elle se comportera comme une pile, avec la posibilité de mélanger la pile)
def creer_pioche(identDebut,deckGen):
	pio = []
	ident = identDebut
	for i in range(9) : #0 à 8 inclus  0-4 Archer Garde Soldat (5) 5 Garde Soldat 6-8 Soldat (3)
		if i < 5 :
			carte = creer_carte(ident,"Archer","def")
			ajouterCarte(deckGen,carte)
			ident += 1
			pio.append(carte)

		if i < 6 :
			carte = creer_carte(ident,"Garde","def")
			ajouterCarte(deckGen,carte)
			ident += 1
			pio.append(carte)

		carte = creer_carte(ident,"Soldat","def")
		ajouterCarte(deckGen,carte)
		ident += 1
		pio.append(carte)

	return pio

#melanger_pioche : pioche -> pioche
#Melange une pioche en in/out
def melanger_pioche(pio):
	return random.sample(pio,len(pio))


#piocher_carte: pioche -> carte
#Renvoie la première carte de la pioche p et la retire de la pioche
def piocher_carte(pio):
	carte = pio[0]
	pio.remove(carte)
	return carte

#pioche_vide: pioche -> bool
#renvoie true si la pioche p n’a plus de carte
def pioche_vide(pio):
	return len(pio)==0



