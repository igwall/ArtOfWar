#deckGen 
from package.carte import *

#Ce type va comprendre toutes les cartes du jeu. Cela permettra de retrouver facilement les cartes choisies par l'utilisateur lorsqu'il nous donne un int (identifiant de la carte)

#Structure : Dico de cartes
#id de type int 
#carte de type Carte
#{id : carte} 

def creerDeck():
	return {} 

#On donne l'identifiant, elle renvoie la carte
def getCarte(deckGen, ident) :
	return deckGen[ident]

#Ajoute la carte dans la liste 
def ajouterCarte(deckGen, carte):
	deckGen[getID(carte)] = carte
	return deckGen

