from package.cdb import *
from package.royaume import *



#Crée un joueur.
#ident : identifiant du joueur, compris entre 1 et 2
#pioche : pioche du joueur
#main : main du joueur
#royaume : royaume du joueur
#cdb : champ de batail du joueur
#cimetiere : cimetière du joueur
#reserve : réserve du joueur
#creer_joueur : int x pioche x main x royaume x cdb x cimetiere x reserve-> joueur

#FG : Structure de donnée choisie
# {'ident' : int, 'pioche' : pioche,'main' : main,'royaume' : royaume,'cdb' : cdb,'cimetiere' : cimetiere,'reserve' : reserve}
def creer_joueur(ident, pioche, main, royaume, cdb, cimetiere, reserve):
	return {'ident':ident,'pioche':pioche,'main':main,'royaume':royaume,'cdb':cdb,'cimetiere':cimetiere,'reserve':reserve}

#Renvoi la pioche du joueur
#get_pioche : joueur -> pioche
def get_pioche(joueur):
	return joueur['pioche']

#Renvoi le champ de bataille du joueur
#get_pioche : joueur -> cdb
def get_cdb(joueur):
	return joueur['cdb']

#Renvoie la réserve d’un joueur
#get_reserve : joueur -> reserve
def get_reserve(joueur):
	return joueur['reserve']

#Renvoie le royaume d’un joueur
#get_royaume : joueur -> royaume
def get_royaume(joueur):
	return joueur['royaume']

#Renvoie le cimetière d’un joueur
#get_cimetière : joueur -> cimetière
def get_cimetiere(joueur):
	return joueur['cimetiere']

#Renvoie la main d’un joueur
#get_main(joueur) : joueur -> Main
def get_main(joueur):
	return joueur['main']

def get_ident(joueur):
	return joueur['ident']

#Reinitialiser_carte: joueur -> joueur
#Remet la défense et le marqueur de touche de toutes les cartes du champ de bataille et du royaume du joueur j à leur état initial.

#Ne pouvant pas accéder à la structure de donnée du royaume et du cdb d'ici et n'ayant pas d'itérateur en place, on a décidé de séparer en deux la fonction reinitialiser carte.
def reinitialiser_carteJoueur(joueur):
	reinitialiser_carte_cdb(get_cdb(joueur))
	reinitialiser_carte_royaume(get_royaume(joueur))
	return joueur
