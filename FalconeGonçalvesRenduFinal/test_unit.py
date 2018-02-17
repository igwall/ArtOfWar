#coding:utf-8
import os
import time
from package.carte import *
from package.cdb import *
from package.cimetiere import *
from package.joueur import *
from package.main import *
from package.pioche import *
from package.reserve import *
from package.royaume import *
from package.deckGen import *

########### Test sur le Joueur et les Get ##########


def test_get_pioche(joueur):
	pioche = [4,5,6,7, 'bonjour']
	joueur['pioche']= pioche
	return pioche == get_pioche(joueur)

def test_get_cdb(joueur):
	cdb = [4,5,6,7, 'bonjour', ]
	joueur['cdb']= cdb
	return cdb == get_cdb(joueur)

def test_get_reserve(joueur):
	reserve = [4,5,6,7, 'bonjour', ]
	joueur['reserve']= reserve
	return reserve == get_reserve(joueur)

def test_get_royaume(joueur):
	royaume = [4,5,6,7, 'bonjour', ]
	joueur['royaume']= royaume
	return royaume == get_royaume(joueur)

def test_get_royaume(joueur):
	cimetiere = [4,5,6,7, 'bonjour', ]
	joueur['cimetiere']= cimetiere
	return cimetiere == get_cimetiere(joueur)

def test_get_main(joueur):
	main = [4,5,6,7, 'bonjour', ]
	joueur['main']= main
	return main == get_main(joueur)

def test_get_idet(joueur):
	joueur['ident']= 1
	return  get_ident(joueur) == 1

###########Tes cdb ###############

def test_placer_dans_cdb():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	if not ( not position_vide(pos,cdb) and est_dans_cdb(carte,cdb)):
		print("erreur placer_dans_cdb : carte non reconnu comme placée")
		return False
	return True
def test_est_dans_cdb():
	cdb = creer_cdb()
	indent = [0,1,2,3,4,5]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
		if not est_dans_cdb(carte, cdb):
			print("erreur est_dans_cdb : les cartes ajoutées dans cdb ne sont pas détectées par est_dans_cdb")
			return False
	return True


def test_position_vide():
	cdb = creer_cdb()
	positions = [0,1,2,3,4,5]
	for pos in positions :
		carte= pos
		if not position_vide(pos, cdb):
			print("erreur test_position_vide : position non vide alors que normalement si")
			return False
		placer_dans_cdb(carte, cdb, pos)
		if position_vide(pos, cdb):
			print("erreur test_position_vide : position vide alors qu'on a rajouter un élément'")
			return False
	return True
def test_retirer_du_cdb():
	cdb = creer_cdb()
	indent = [0,1,2,3,4,5]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
	positions = indent
	for pos in positions :
		carte = pos
		retirer_du_cdb(pos,cdb)
		if est_dans_cdb(carte, cdb):
				print("erreur retirer_du_cdb : les cartes retirees du cdb  sont toujours détectées par est_dans_cdb")
				return False
	return True

def test_is_front():
	cdb = creer_cdb()
	indent = [0,1,2,3,4,5]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
	return (is_front(1,cdb) and not is_front(2,cdb))

def test_get_position_utilisables():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	positions = [0,1,3,4,5]
	if get_positions_utilisables(cdb) == positions:
		return True
	return False

def test_est_position_utilisables():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	if not est_position_utilisable(cdb,2) and est_position_utilisable(cdb,3):
		return True
	return False

def test_mettre_en_position_def():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	mettre_en_position_def(cdb)
	return est_en_posture_defensive(carte)


def test_get_nombre_carte_cdb(cdb):
	cdb = creer_cdb()
	indent = [0,1,2,3,4,5]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
		if get_nombre_carte_cdb(cdb) != i+1 :
			return False
	return True

def test_reste_carte_en_position_defensive():
	cdb = creer_cdb()
	indent = [0,1,2,3,4,5]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
		mettre_en_offensif(carte)
		if reste_carte_en_position_defensive(cdb):
			return False
	mettre_en_defensive(carte)
	return reste_carte_en_position_defensive(cdb)


################## Pioche ######################

def test_creerPioche():
	DeckGen= creerDeck()
	p=creer_pioche(1,DeckGen)
	return pioche_vide(p) == False


def test_melangerPioche():
	DeckGen= creerDeck()
	P = creer_pioche(1,DeckGen)
	T = P
	P = melanger_pioche(P)
	return T!=P


def test_piochercarte():
	DeckGen= creerDeck()
	pioche=creer_pioche(1,DeckGen)
	PiocheDebut = pioche
	carte = piocher_carte(pioche)
	return (PiocheDebut != pioche)


##################### Reserve ############

def test_PlacerdansReserve():
	res= creer_reserve()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_reserve(carte,res)
	return est_dans_reserve( carte,res)

def test_EstDansreserve():
	res=creer_reserve()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_reserve(carte,res)
	if not est_dans_reserve(carte,res):
		return False
	piocher_dans_reserve(res)
	return not est_dans_reserve(carte,res)

def test_get_nombre_carte_reserve():
	res=creer_reserve()
	i=1
	carte = creer_carte(1, "Garde", "def")
	while i<10 :
		placer_dans_reserve(carte,res)
		if i!= get_nombre_carte_reserve(res):
			return False
		i+=1
		return True


############### Cimetière ################

def test_PlacerdansCimetiere():
	cim1 = creer_cimetiere()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_cimetiere(carte, cim1)
	cim2 = creer_cimetiere()
	carte = creer_carte(2, "Garde", "def")
	placer_dans_cimetiere(carte, cim2)
	return cim1 != cim2



############### Main ###############



def test_main_vide():
	main = creer_main()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_main(carte,main)
	return not main_vide(main)

def test_get_nombre_carte_main():
	main = creer_main()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_main(carte,main)
	return get_nombre_carte_main(main) == 1

def test_est_dans_main():
	main = creer_main()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_main(carte,main)
	return est_dans_main(carte,main)


def test_placer_dans_main():
	main = creer_main()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_main(carte,main)
	return est_dans_main(carte,main)


def test_retirer_de_main():
	main = creer_main()
	carte = creer_carte(1, "Garde", "def")
	placer_dans_main(carte,main)
	retirer_de_main(carte,main)
	return not est_dans_main(carte,main)














################### Main ############""
deckGen = creerDeck()
cimetiere = creer_cimetiere()
royaume = creer_royaume()
pioche = creer_pioche(2,deckGen)
main = creer_main()
reserve = creer_reserve()
ident = 1
cdb = creer_cdb()


joueur= creer_joueur(ident, pioche, main, royaume, cdb, cimetiere, reserve)

print(test_get_pioche(joueur))
print(test_get_cdb(joueur))
print(test_get_reserve(joueur))
print(test_get_royaume(joueur))
print(test_get_royaume(joueur))
print(test_get_main(joueur))
print(test_get_idet(joueur))
print(test_placer_dans_cdb())
print(test_est_dans_cdb())
print(test_position_vide())
print(test_retirer_du_cdb())
print("Celui là")
print(test_is_front())
print("Celui là")
print(test_get_position_utilisables())
print(test_est_position_utilisables())
print(test_mettre_en_position_def())
print(test_get_nombre_carte_cdb(cdb))
print(test_reste_carte_en_position_defensive())
print(test_creerPioche())
print(test_melangerPioche())
print("Celui là")
print(test_piochercarte())
print(test_PlacerdansReserve())
print(test_EstDansreserve())
print(test_get_nombre_carte_reserve())
print(test_PlacerdansCimetiere())
print(test_main_vide())
print(test_get_nombre_carte_main())
print(test_est_dans_main())
print(test_placer_dans_main())
print(test_retirer_de_main())
