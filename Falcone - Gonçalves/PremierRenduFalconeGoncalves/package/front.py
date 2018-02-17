#coding:utf-8
# === === Front === === #
    
<<<<<<< Updated upstream
def creerFront() :
=======
done def creerFront() -> Front
>>>>>>> Stashed changes
    # Pre-condition : Aucune
    # Post-condition : Aucune 
    # Resultat : Créer un element de Type Front
    
    pass

<<<<<<< Updated upstream
def envoyerFront(front,carte,pos):  #======= ======== On a enlevé larriere attention si on doit le remettre
    # Pre-condition : front est de type Front, carte de type Carte et pos de type str
=======
done def envoyerFront(Front,Carte,Str)->Front 
    # Pre-condition : La carte doit être situé à l'arrière
>>>>>>> Stashed changes
    # Post-condition : Aucune 
    # Resultat : La carte est envoyé au front à la position indiquée en paramètre. Le front est modifié et renvoyé !
    
    pass

<<<<<<< Updated upstream
def nbCarteFront(front) : 
    # Pre-condition : front est de type Front
=======
done def nbCarteFront(Front)->Int
    # Pre-condition : La carte doit être situé à l'arrière
>>>>>>> Stashed changes
    # Post-condition : Aucune 
    # Resultat : Indique le nombre de carte présente sur le front
    
    pass

<<<<<<< Updated upstream
def extraireFront(front, pos) : 
    # Pre-condition : front est de type Front, pos est de type str et designe une position non vide
=======
done def estVideFront(Front, Str)->Bool
    # Pre-condition : La carte doit être situé à l'arrière
    # Post-condition : Aucune 
    # Resultat : Renvoi True si la position est vide, renvoi False sinon

done def extraireFront(Front,Str)->Carte 
    # Pre-condition : Aucune
>>>>>>> Stashed changes
    # Post-condition : Aucune
    # Resultat : Renvoie la carte située à la position "pos" du front donné en parametre. Le front est modifié (car la carte est retiré du front) et la carte retirée est renvoyée. 
    
    pass
        