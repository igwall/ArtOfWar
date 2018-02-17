###MAIN
from package.carte import *

#Crée une main vide
#FG / Structure de donnée
# (Carte)[0] puis on append à chaque ajout (c'est donc une liste)
def creer_main():
	return []

#placer_dans_main : carte x main -> main
#ajoute carte c dans la main m du joueur, in/out
def placer_dans_main(carte,main):
	return main.append(carte)

#Retirer_de_main : carte x main -> main
# retire la carte c de la main m, in/out
#CI : on vérifie que cette carte c est bien dans m

#VERIF SI LA CARTE EST DANS LA MAIN (voir dans le main.py)
def retirer_de_main(carte,main):
	return main.remove(carte)

#main_vide : main -> bool
#Renvoie True si la main m est vide
def main_vide(main):
	return get_nombre_carte_main(main) == 0

#get_nombre_carte_main: main ->int
#Renvoie le nombre de carte qu’il y a dans la main m
def  get_nombre_carte_main(main):
	return len(main)

#affiche_main : main -> string
#Décrit une main, par ex : "Roi, Garde, Garde, Soldat, Archer, Archer"
#FG : On change la description en y intégrant l'Ident de la carte. On a alors px "1 Garde, 12 Garde, 30 Soldat, 28 Archer, 24 Archer"
def decrire_main(main):
	res = "Voici votre main : \n"
	for c in main[:-1] :
		res += str(getID(c)) + " " + get_type(c)+", "
	res += str(getID(main[-1])) + " " + get_type(main[-1])
	res += "\n\n"
	return res

#est_dans_main: carte x main -> bool
#renvoie true si il existe au moins une carte de type c dans la main m
def est_dans_main(carte,main):
	return carte in main



