#coding:utf-8
# === === Carte === === #
    
def estVerticale(carte) :
    # Pre-condition : La carte est de type Carte.
    # Post-condition : Aucune
    # Resultat : Retourne True si la carte est verticale, retourne False sinon
    
    pass

def changementMode(carte) : 
    # Pre-condition : la carte est de type Carte 
    # Post-condition : Aucune
    # Resultat : Le mode de la carte a été modifié :  Vertical si Horizontal et inversement. La carte est modifiée et renvoyée 
    
    pass
    

def positionCarte(carte) :
    # Pre-condition : La carte est type Carte 
    # Post-condition : Aucune
    # Resultat : Retourne la chaine de caractère représentant la position de la carte sur le plateau ("F1","F2",...,"A3")  
    
    pass
    
def setPositionCarte(carte,pos) : 
    # Pre-condition : La carte est type Carte, la pos est une string 
    # Post-condition : Aucune
    # Resultat : Modifie la position de la carte. Cette fonction renvoie aussi la carte modifiée
    
    pass
    
def pointAttaque(carte) : 
    # Pre-condition : la carte est de type Carte
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point d'attaque de la carte
    
    pass
    
def pointDefense(carte) : 
    # Pre-condition : la carte est de type Carte
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point de defense de la carte EN FONCTION DE SON MODE 
        
    pass
    
def pointDegat(carte) : 
    # Pre-condition : la carte est de type Carte
    # Post-condition : Aucune
    # Resultat : retourne le nombre de point de dégat subits de la carte
    
    pass
    
def capture(carte,joueur) : 
    # Pre-condition : la carte est de type Carte. le joueur est de type Joueur
    # Post-condition : Aucune
    # Resultat : la carte devient capturée. La carte est placée dans le Royaume du joueur entrée en parametre
    
    pass
    
def setPointDegat(carte,nouvDegat) :
    # Pre-condition : La carte est de type Carte, nouvDegat est de type Int. 
    # Post-condition : Aucune
    # Resultat : Modifie la carte donnée en parametre. pointDegats(carte) de la carte modifiée est egal à nouvDegat. 
    
    pass
    
def roleCarte(carte):
    # Pre-condition : carte est de type Carte
    # Post-condition : Renvoi un string parmis ces valeurs : Garde, Archer, Soldat, Roi
    # Resultat : Renvoi le rôle de la carte entrée en paramètre
        
    pass
    
def estAPortee(carte,cible) : 
    # Pre-condition : carte et cible sont toutes deux des Carte présentent sur le champ de bataille
    # Post-condition : 
    # Resultat : Renvoie True si la cible est à portée de la carte, False sinon
    
    pass
    
    