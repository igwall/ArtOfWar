#coding:utf-8
# === === Royaume === === #
    
done def creerRoyaume() :
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Royaume
    
    pass

def extraireRoyaume(royaume,role) :
    # Pre-condition : royaume est de type Royaume, role est de type String. Au moins une carte avec Role = role se trouve dans le royaume. 
    # Post-condition : Aucune
    # Resultat : renvoie une carte ayant Role = role. Le royaume est donc modifié car la carte a été retirée du royaume
    pass 

done def entrerRoyaume(royaume,carte) : 
    # Pre-condition : royaume est de type Royaume, carte est de type Carte 
    # Post-condition : Aucune
    # Resultat : Ajoute la carte entrée en paramètre dans le royaume. Le royaume est modifié et renvoyé 
    
    pass

done def nbCarteRoyaume(royaume) : 
    # Pre-condition : royaume est de type Royaume 
    # Post-condition : Aucune
    # Resultat : Retourne le nombre de citoyens (cartes) dans le royaume placé en paramètre
    
    pass
    
def nbCarteRoleRoyaume(royaume,role) : 
    # Pre-condition : royaume est de type Royaume, role est un String
    # Post-condition : Aucune
    # Resultat : Retourne le nombre de citoyens (cartes) ayant le role donné dans le royaume placé en paramètre 
    
    pass
    

def estEffondre(royaume) :  
    # Pre-condition : Aucune
    # Post-condition :
    # Resultat : Renvoie True si le royaume est effondré et False sinon 
    
    pass

def effondre(royaume) :
    # Pre-condition : Aucune
    # Post-condition :
    # Resultat : Modifie l'état d'éffondrement du Royaume du joueur passé en paramètre. Le royaume est modifié et renvoyé 
    
    pass 

def descriptionRoyaume(royaume) : 
    # Pre-condition : royaume est de type Royaume
    # Post-condition :
    # Resultat : renvoie un string qui est une description du royaume donné en parametre. La chaine de caratere contiendra les Roles des cartes ainsi que le nombre des cartes. Finalement elle comprend le total. Par exemple la chaine de caractere pourra renvoyer "Roi : 0, Soldat : 2, Archer : 3, Garde : 1, Total : 6"
    
    pass

    