###CIMETIERE

#Le cimetière est vide quand on le crée, on le remplit dans le main du programme

#Crée un cimetière vide
#FG / Structure de donnée 
# (Carte)[0] puis on append à chaque ajout (c'est donc une liste)

def creer_cimetiere():
	return []

#placer_dans_cimetiere: carte x cimetiere -> cimetiere
#Place la carte c dans le cimetière cim, en in/out
#renvoie le cimetière
def placer_dans_cimetiere(carte,cim):
	cim.append(carte)
	return cim 