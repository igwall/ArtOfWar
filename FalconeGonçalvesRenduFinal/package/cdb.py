###CHAMP DE BATAILLE
from package.carte import *

#Le champ de bataille est vide quand on le crée,
#on le remplit dans le main du programme

#Crée un champ de bataille vide

# FG : Structure décidée
# (Case)[6]
# Case:(Carte | "Vide")

def creer_cdb():
	return ["Vide"]*6

#placer_dans_cdb : carte x champ_de_bataille x int-> cdb
#Ajoute une carte c sur le champ de bataille cdb à la position p, in/out.
#Il ne faut pas oublier de prendre en compte le fait que si on place une carte sur une position occupé alors la carte occupant la position est remplacée et renvoyée dans la main
#resultat : champ_de_bataille auquel on a ajouté c

def placer_dans_cdb(carte, cdb, pos):
	cdb[pos] = carte
	return cdb


#est_dans_cdb: carte x cdb -> bool
#Indique si une carte en particulier est dans le cdb
#carte : c'est la carte
#cdb : champ de bataille dans lequel on effectue la recherche
def est_dans_cdb(carte,cdb):
	return carte in cdb

#position_vide : int x cdb -> bool
#Indique si une position du champ de bataille est vide
#position : entier représentant l'indice de position
#cdb : champ de bataille où l'on souhaite faire la vérification
def position_vide(pos, cdb):
	return cdb[pos] == "Vide"

#retirer_du_cdb: int x cdb -> cdb
#Retire une carte du champ de bataille, in/out
#position : position de la carte que l'on souhaite retirer
#cdb : champ de bataille duquel on enlève la carte
#ON RETIRE SANS DEMANDER LA CARTE ?
def retirer_du_cdb(pos,cdb):
	cdb[pos] = "Vide"
	return cdb

#is_front: int x cdb -> bool
#Renvoie true si il y a une carte devant la position p du champ de bataille cdb
#p : position à partir de laquelle on souhaite faire la vérification, ce doit être une position de la ligne arrière (0 <= p <= 2)
#cdb : champ de bataille concerné par la vérification
def is_front(p, cdb):
	#Verif p < 3 ???
	return not position_vide(p+3,cdb)

#get_positions_utilisables : cdb -> int[]
#Renvoie les positions du champ de bataille cdb où il est possible de poser une carte
#cdb : champ de bataille que l'on souhaite analyser
#résultat : un tableau d'entier dans lequel sont stockées les indices des positions utilisables
def get_positions_utilisables(cdb):
	res = []
	for pos in range(6) :
		if est_position_utilisable(cdb,pos) :
			res.append(pos)
	return res

#est_position_utilisable: cdb x int -> bool
#Indique si une position du champ de bataille est utilisable, c.à.d que l'on a le droit de placer une carte dessus
#On rappelle que l'on ne peut pas placer de carte sur une case de la backline si il n'y a pas de carte devant
#cdb : cdb que l'on souhaite analyser
#p : position concerné par la vérification
#résultat : true si la position est utilisable

#FG : S'il y a deja quelqu'un, ça compte comme utilisable ???? oui
def est_position_utilisable(cdb,p):
	if p >= 3 and p <= 5:
		return True
	elif p >= 0 and p <= 2 :
		return is_front(p,cdb)
	else :
		return False

#decrire_cdb: cdb -> string
#Décrit le champs de bataille cdb, e.g :    "1. Garde, 2. Vide, 3. Soldat,
#                                            4. Archer, 5. Vide, 6. Archer"
#cdb : champ de bataille à décrire
def decrire_cdb(cdb):
	res = "Voici votre champ de bataille : \n"
	for i in range(3) :
		carte = getCarteCDB(i+3,cdb)
		if estVide(carte) :
			if i == 2 :
				res += str(i+3)+". [Vide] "
			else :
				res += str(i+3)+". [Vide], "
		else :
			if i == 2 :
				res +=  str(i+3)+". ["+str(getID(carte))+" "+ get_type(carte)+"] "
			else :
				res +=  str(i+3)+". ["+str(getID(carte))+" "+ get_type(carte)+"], "

	res += "\n"

	for i in range(3) :
		carte = getCarteCDB(i,cdb)
		if estVide(carte) :
			if i == 2 :
				res +=  str(i)+". [Vide] "
			else :
				res +=  str(i)+". [Vide], "
		else :
			if i == 2 :
				res +=  str(i)+". ["+str(getID(carte))+" "+ get_type(carte)+"] "
			else :
				res +=  str(i)+". ["+str(getID(carte))+" "+ get_type(carte)+"], "


	return res

def decrire_cdbAdverse(cdb):
	res = "Voici votre champ de bataille : \n"

	for i in range(2,-1, -1) : #(start, end, step)
		carte = getCarteCDB(i,cdb)
		if estVide(carte) :
			if i == 0 :
				res +=  str(i)+". [Vide] "
			else :
				res +=  str(i)+". [Vide], "
		else :
			if i == 0 :
				res +=  str(i)+". ["+str(getID(carte))+" "+ get_type(carte)+"] "
			else :
				res +=  str(i)+". ["+str(getID(carte))+" "+ get_type(carte)+"], "

	res += "\n"

	for i in range(2,-1,-1) :
		carte = getCarteCDB(i+3,cdb)
		if estVide(carte) :
			if i == 0 :
				res += str(i+3)+". Vide "
			else :
				res += str(i+3)+". Vide, "
		else :
			if i == 0 :
				res +=  str(i+3)+". "+str(getID(carte))+" "+ get_type(carte)+" "
			else :
				res +=  str(i+3)+". "+str(getID(carte))+" "+ get_type(carte)+", "


	return res


#Mettre_en_position_def: cdb -> cdb
#Met toutes les cartes d’un champ de bataille cdb en position defensive, in/out
def mettre_en_position_def(cdb):
	for pos in range(6) :
		carte = getCarteCDB(pos,cdb)
		if carte != "Vide" :
			mettre_en_defensive(carte)
	return cdb

#get_nombre_carte_cdb: cdb -> int
#Renvoie le nombre de carte qu’il y a sur le champ de bataille cdb
def get_nombre_carte_cdb(cdb):
	count = 0
	for cart in cdb :
		if cart != "Vide" :
			count+=1
	return count

#reste_carte_en_position_defensive: cdb -> bool:
#Renvoie True si il reste au moins une carte en position défensive
def reste_carte_en_position_defensive(cdb):
	pos = 0
	while pos < 6 :
		carte = getCarteCDB(pos,cdb)
		if(carte != "Vide") :
			if est_en_posture_defensive(carte) :
				return True
		pos += 1
	return False

#possibilité_attaquer: cdb x cdb -> bool
#renvoie true si le champ de bataille cdb1 a des cartes pouvant attaquer une des
#cartes du cdb2
def possibilite_attaquer(cdb1,cdb2):
	pos1 = 0
	while pos1 < 6 :
		pos2 = 0
		carte = getCarteCDB(pos1,cdb1)
		if carte != "Vide" :
			while pos2 < 6 :
				carte2 = getCarteCDB(pos2,cdb2)
				if carte2 != "Vide" :
					if touche(carte,carte2,cdb1,cdb2) :
						return True
				pos2 += 1
		pos1 += 1
	return False

#avancer_unite: int x cdb -> cdb
#Avance la carte sur le front, modifie en in/out le champ de bataille
#Le front ne doit pas être occupé par une autre carte ##LA VERIFICATION EST FAITES ?##
#p : position de la carte à avancer
def avancer_unite(pos, cdb):
	carte = getCarteCDB(pos,cdb)
	placer_dans_cdb(carte,cdb,pos+3)
	return cdb

#Renvoie la carte à la position pos du champ de bataille cdb
# int x cdb -> carte
def getCarteCDB(pos,cdb) :
	return cdb[pos]

#get_position: carte x cdb -> int
#Renvoie la position (coordonnée) de la carte c sur le champ de bataille cdb
def get_position(c,cdb):
	i = 0
	while i<=len(cdb)-1:
		carteCdb = getCarteCDB(i,cdb)
		if not(estVide(carteCdb)) and (getID(c) == getID(carteCdb)):
			return i
		i+=1
	return -1


#Reinitialiser_carte: cdb -> cdb
#Reinitialise les cartes du cdb
def reinitialiser_carte_cdb(cdb) :
	for carte in cdb :
		if carte != "Vide" :
			reinitialiser_carte(carte)
	return cdb
