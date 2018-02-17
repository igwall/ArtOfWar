##ROYAUME
from package.carte import *
#Le royaume est vide quand on le crée, on le remplit dans le main du programme

#Crée un royaume vide, in/out

#FG / Structure de donnée
# (Carte)[] puis on append à chaque ajout (c'est donc une liste)
def creer_royaume():
	return []

#placer_dans_royaume : carte x royaume -> royaume
#Place une carte c dans le royaume r, in/out
def placer_dans_royaume(carte, roy):
	roy.append(carte)
	return roy

#get_nombre_carte_royaume: royaume -> int
#Renvoie le nombre de carte d’un royaume roy
def get_nombre_carte_royaume(roy):
	return len(roy)

#Afficher_Royaume: royaume -> string
#Décrit le royaume passer en paramètre sous forme de chaine de caractère, e.g : "5 Soldats, 2 Gardes, 3 Archers"
def decrire_royaume(roy):
	res = "Voici votre royaume : \n"
	for c in roy[:-1] :
		res += str(getID(c)) + " " + get_type(c)+", "
	res += str(getID(roy[-1])) + " " + get_type(roy[-1])
	return res

#Retirer_carte_royaume: royaume x carte -> royaume
#Retire une carte c du royaume r, en in/out
def retirer_du_royaume(roy,carte):
	roy.remove(carte)
	return roy
	#VERIF EST CE QUE LA FONCTION EST LANCEE EN VERIFIANT QUE LA CARTE EST BIEN DANS LE ROYAUME

#est_dans_royaume: carte x roy -> bool
#renvoie true si il existe une carte de meme type que c dans le royaume #POURQUOI NE PAS DEMANDER LE TYPE DIRECTEMENT ?!
def est_dans_royaume(carte,roy):
	while i < len(roy)-1 :
		if get_type(roy[i]) == get_type(carte) :
			return True
		i += 1
	return False


#Reinitialiser_carte_royaume: royaume -> royaume
#Réinitialise les cartes du royaume.
def reinitialiser_carte_royaume(royaume):
	for carte in royaume :
		if carte != "Vide" :
			reinitialiser_carte(carte)
	return royaume






