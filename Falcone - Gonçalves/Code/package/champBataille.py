#coding:utf-8
# === === Champs Bataille === === #

def creerChampBataille():
    # Pre-condition : Le joueur entré en paramètre ne doit pas avoir de champ de bataille existant
    # Post-condition : Aucune
    # Resultat : Crée un champ de bataille vide. Crée un front et un arriere, les associent au champ créé et renvoie le champ.
    
    pass
    
def redresseCartes(champ):
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : Toutes les cartes du champ de bataille sont verticales. Le champ de bataille est donc modifié et renvoyé. 
    
    pass

def estVide(champ) :
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : Retourne True si aucune carte n'est placée sur le champs de bataille, false sinon
    
    pass

def obtenirCarte(champ,pos) :
    # Pre-condition : La position (pos de type String) entrée en paramètre doit correspondre à une position du plateau et une carte doit se trouver à cet emplacement. champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : Renvoie la carte se trouvant à cette position SANS l'enlever
    
    pass

def nbCarteChampBataille(champ):
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Indique le nombre de carte présente dans le champ de bataille
    pass

def front(champ):
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : retourne le front du champ entré en paramètre
    
    pass

def arriere(champ):
    # Pre-condition : le champ est de type ChampBataille
    # Post-condition : Aucune
    # Resultat : retourne l'arriere du champ entré en paramètre
    
    pass

def touteHorizontale(champ):
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Retourne True si toutes les cartes du champ de bataille sont horizontales, retourne False sinon
    
    return True

def estVidePosition(champ,pos):
    # Pre-condition : pos est un string
    # Post-condition : Aucune
    # Resultat : Retourne True si la position contient une carte (en utilisant les fonction estVideFront et estVideArriere)
    
    pass 

def verifArriere(champ,pos):
    # Pre-condition : Soit String (chaine de caractère) correspondant la position de la carte cible.
    # Post-condition : Aucune
    # Resultat : Retourne True si l'Arriere situé derrière la carte cible est occupé, retourne False sinon (ou si la carte cible donnée en paramètre n'est pas au front).
    
    pass

def avancerCarte(champ,pos):
    # Pre-condition : La position donnée en paramètres est precedemment occupée par une carte au front et une autre carte se situe derriere elle
    # Post-condition : Aucune
    # Resultat : Modifie le champ de bataille dans lequel la carte (située à l'arriere) est envoyée au front. La fonction retourne aussi ce champ. 
    
    pass
    
    
   