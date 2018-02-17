#coding:utf-8
# === === Main === === #
    
def creerMain(indice) : 
    # Pre-condition : indice est de type Int
    # Post-condition : Aucune
    # Resultat : Créer un element de type Main contenant une carte Roi correspondant à l'indice donné
    
    pass

def descriptionMain(main) : 
    # Pre-condition : main est de Type Main
    # Post-condition : Aucune
    # Resultat : renvoie un String permettant de decrire la main du joueur. On pourra par exemple mettre les Roles des cartes séparés par des virgules. ex : la fonction peut renvoyer "Roi, Garde, Archer, Archer" 
    
    pass

done def extraireCarteMain(main,i) : 
    # Pre-condition : main est de Type Main, i l'indice de la carte voulue 
    # Post-condition : Aucune
    # Resultat : Renvoie la i-eme carte de la main. La main est modifiée : On enleve la carte de la main. (I-eme carte dans l'ordre utilisé pour la descritpionMain. en récupérant l'exemple précedent : en utilisant extraireCarteMain(main,2) on obtient la carte de role "Garde"). 
    
    pass

done def ajouterCarteMain(main, carte) :
    # Pre-condition : main de type Main et carte de type Carte
    # Post-condition : Aucune
    # Resultat : Modifie la main entrée en parametre et y ajoute la carte donnée en parametre. Cette fonction renvoie aussi la main modifiée
    
    pass

done def nbCarteMain(main) : 
    # Pre-condition : main est de type Main.
    # Post-condition : Aucune
    # Resultat : Renvoie le nombre de carte présente dans la main donnée en parametre
    
    pass
        