###RESERVE
from package.carte import *

#La réserve est vide quand on la crée, on la remplit dans le main du programme

#Crée une réserve vide, en in/out

#FG / Structure de donnée
# (Carte)[0] puis on append à chaque ajout (elle se comporte comme une File. On ne récupèrera la premiere carte posée FIFO)

def creer_reserve():
	return []

#placer_dans_reserve : carte x reserve -> int
#Met en réserve une carte c dans la reserve r, in/out
#resultat : 0
def placer_dans_reserve(carte, reserve):
	reserve.append(carte)
	return reserve

#est_dans_reserve: carte x reserve -> bool
#Renvoi true si la carte c est dans la réserve res
def est_dans_reserve(carte,res):
	return carte in res

def reserve_vide(reserve) :
	return get_nombre_carte_reserve(reserve) == 0

#Afficher_Reserve: reserve -> string
#Renvoi une chaine de caractère décrivant la réserve dans l'ordre, e.g : "Archer, Garde, Garde, Archer, Soldat"
def decrire_reserve(res):
	if not reserve_vide(res) :
		cdc = "Voici votre réserve : \n"
		for c in res[:-1] :
			cdc += str(getID(c)) + " " + get_type(c)+", "
		cdc += str(getID(res[-1])) + " " + get_type(res[-1])
	else :
		cdc = "Votre réserve est vide"
	return cdc


#get_nombre_carte_reserve: reserve ->int
#Renvoie le nombre de carte qu’il y a dans la reserve r
def get_nombre_carte_reserve(res):
	return len(res)

#piocher_reserve: reserve -> carte
#Retourne la première carte de la réserve res et la retire
def piocher_dans_reserve(res):
	carte = res[0]
	res.remove(carte)
	return carte



