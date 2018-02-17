#coding:utf-8

## ATTENTION TOUS LES FICHIERS SONT A EXECUTER AVEC PYTHON3. SANS PYTHON3 LES FONCTIONS INPUT NE FONCTIONNENT PAS ##

from package.arriere import *
from package.carte import *
from package.champBataille import *
from package.cimetiere import *
from package.front import *
from package.joueur import *
from package.mainJoueur import *
from package.partie import *
from package.pioche import *
from package.reserve import *
from package.royaume import *

# =========== Diverses fonctions nécessaires pour l'interfece ================ 
def verifAction(action) : 
    if action < 0 or action > 3 : 
        return False
    else : 
        return True 
                             
def estPosition(choix) :
    if(choix[0]=='A' or choix[0]=="F") :
        if(int(choix[1]) >= 1 and int(choix[1]) <= 3):
            return True
        else:
            return False
    else :
        return False
                                            
                                            
def positionValide(choix,joueur) : 
    if(choix[0] == "A"):
        return estPosition(choix) and not(estVidePosition(champBataille(joueur),"F"+choix[1])) #La position est valide à l'arriere si le front est occupé au meme indice 
    else : 
        return estPosition(choix)
                            
def askAttaque(joueur):
    choix = int(input(nom(joueur)+" voulez-vous encore attaquer ? 1 = Oui, 0 = Non\nChoix : "))
    if(choix == 0):
        return False
    elif(choix == 1):
        return True
    else :
        return askAttaque(joueur)
                                            
def askAttaqueCible(joueur):
    choix = int(input(nom(joueur)+" voulez-vous encore attaquer cette cible ? 1 = Oui, 0 = Non\nChoix : "))
    if(choix == 0):
        return False
    elif(choix == 1):
        return True
    else :
        return askAttaqueCible(joueur) 

def demandeDevelop(JA):
    print(descriptionMain(main(JA)))
    choix = input("Voulez-vous mettre une carte de votre main au royaume ?\n1 = Oui , 0 = Non. Choix : ")
    if choix == 0 :
        return False 
    elif choix == 1 : 
        return True
    else:
        return demandeDevelop(JA)
    
def demandeAttaquerCible(JA) :
    choix = input("Voulez-vous encore attaquer la meme cible ?\n1 = Oui , 0 = Non. Choix : ")
    if choix == 0 :
        return False 
    elif choix == 1 : 
        return True
    else: 
        return demandeAttaquerCible(JA)
    
def demandeAttaquer(JA) :
    choix = input("Voulez-vous encore attaquer ?\n1 = Oui , 0 = Non. Choix : ")
    if choix == 0 :
        return False 
    elif choix == 1 : 
        return True
    else: 
        return demandeAttaquer(JA)
    
def deploiementCarte(joueur,nbCarteAPlacerReserve,nbCarteAPlacerRoyaume) : 
    #Permet de placer nbCarteAPlacerReserve cartes provenant de la reserve sur le champ de bataille et nbCarteAPlacerRoyaume cartes provenant du royaume sur le champ de bataille. 
    for i in range(nbCarteAPlacerReserve) :
        #A deux reprises on demande au joueur de placer une carte sur le champ 
        positionCarteSecours = input(nom(joueur) + ", où voulez-vous placer la carte de votre réserve ?")
        while(not(estPosition(positionCarteSecours)) or not(estVidePosition(champBataille(joueur),positionCarteSecours))) : 
        #Arret : Qd la position est bonne & qd la position est vide
        #pousuite : qd la position est fausse ou qd la position est non vide
            positionCarteSecours = input(nom(joueur) + "veuillez indiquer une position valide ! Où voulez-vous placer la carte de votre réserve ?")
        #On place sur le champs de bataille
        if(positionCarteSecours[0] == "F"):
            Carte = premiereCarteReserve(reserve(joueur))
            envoyerFront(front(champBataille(joueur)),Carte,positionCarteSecours) 
        else: #si choix[0] == "A"
            while(not(estPosition(positionCarteSecours)) or not(estVidePosition(champBataille(joueur),positionCarteSecours)) or not(estVidePosition(champBataille(joueur),"A"+positionCarteSecours[1]))) : 
                #Arret : Qd la position est bonne & qd la position est vide & qd il y a quelqu'un devant 
                #pousuite : qd la position est fausse ou qd la position est non vide ou qd il y a personne devant 
                positionCarteSecours = input(nom(joueur) + "veuillez indiquer une position valide ! Où voulez-vous placer la carte de votre réserve ?")
            Carte = premiereCarteReserve(reserve(joueur))
            envoyerArriere(arriere(champBataille(joueur)),Carte,positionCarteSecours)
            
    for i in range(nbCarteAPlacerRoyaume) : 
        #A deux reprises on demande au joueur de placer une carte sur le champ 
        print(descriptionRoyaume(royaume(joueur)))
        roleChoisi = input(nom(joueur) + " quel est le role de la carte que vous voulez extraire du royaume ?")
        while(roleChoisi != "Roi" and roleChoisi != "Soldat" and roleChoisi != "Archer" and roleChoisi != "Garde") : 
            #Arret quand role = "Roi" ou .... ou ... ou ... 
            #Poursuite tant que role != "Roi" et 
            roleChoisi = input(nom(joueur) + " quel est le role de la carte que vous voulez extraire du royaume ?")

        positionCarteSecours = input(nom(joueur) + ", où voulez-vous placer la carte de votre royaume ?")
        while(not(estPosition(positionCarteSecours)) or not(estVidePosition(champBataille(joueur),positionCarteSecours))) : 
        #Arret : Qd la position est bonne & qd la position est vide
        #pousuite : qd la position est fausse ou qd la position est non vide
            positionCarteSecours = input(nom(joueur) + "veuillez indiquer une position valide ! Où voulez-vous placer la carte de votre royaume ?")
        #On place sur le champs de bataille
        if(positionCarteSecours[0] == "F"):
            Carte = extraireRoyaume(royaume(joueur),roleChoisi)
            envoyerFront(front(champBataille(joueur)),Carte,positionCarteSecours) 
        else: #si choix[0] == "A"
            while(not(estPosition(positionCarteSecours)) or not(estVidePosition(champBataille(joueur),positionCarteSecours)) or not(estVidePosition(champBataille(joueur),"A"+positionCarteSecours[1]))) : 
                #Arret : Qd la position est bonne & qd la position est vide & qd il y a quelqu'un devant 
                #pousuite : qd la position est fausse ou qd la position est non vide ou qd il y a personne devant 
                positionCarteSecours = input(nom(joueur) + "veuillez indiquer une position valide ! Où voulez-vous placer la carte de votre réserve ?")
            Carte = extraireRoyaume(royaume(joueur),roleChoisi)
            envoyerArriere(arriere(champBataille(joueur)),Carte,positionCarteSecours)
        
def premierAjoutFront(joueur):
    print(descriptionMain(main(joueur)))
    choix = int(input(nom(joueur) + " quelle carte voulez vous mettre au front ?"))
    while(choix<1 or choix>4):
        #Arret quand choix est >= 1 et <= 4 
        #Poursuite quand choix est < 1 ou > 4 
        choix = int(input(nom(joueur) + " quelle carte voulez vous mettre au front ?"))
        
    pos = input(nom(joueur) + " votre carte va être envoyé au Front. Où voulez-vous mettre votre carte ? (F puis 1|2|3)")
    while(not(estPosition(pos)) or pos[0]!='F') : 
        #Arret quand pos est position et que pos[0] == 'F'
        #Poursuite tant que pos n'est pas positon ou que pos[0] != 'F'
        pos = input(nom(joueur) + " votre carte va être envoyé au Front. Où voulez-vous mettre votre carte ? (F puis 1|2|3)")   
        
    envoyerFront(front(champBataille(joueur)),extraireCarteMain(main(joueur),choix),pos)
    
def premierAjoutReserve(joueur): 
    
    print(descriptionMain(main(joueur)))
    choix = int(input(nom(joueur) + " quelle carte voulez vous mettre en reserve ?"))
    while(choix<1 or choix>3):
        #Arret quand choix est >= 1 et <= 3 
        #Poursuite quand choix est < 1 ou > 3 
        choix = int(input(nom(joueur) + " quelle carte voulez vous mettre en reserve ?"))
        
    envoiReserve(reserve(joueur),extraireCarteMain(main(joueur),choix))
        
#================= fin des fonctions diverses ============================

# === Création de la partie === # 

#Début de la partie



nom1 = input("Entrez le nom du joueur 1 : ")
JA = creerJoueur(1,nom1)

nom2 = input("Entrez le nom du joueur 2 : ")
JoueurAdverse = creerJoueur(2,nom2)

Partie = creerPartie(JA,JoueurAdverse)

#=== ==== INITIALISATION ==== ===

#Les deux joueurs récupèrent leur Roi avec 3 unité (3 unités au hasard)
ajouterCarteMain(main(JA),piocher(pioche(JA)))
ajouterCarteMain(main(JA),piocher(pioche(JA)))
ajouterCarteMain(main(JA),piocher(pioche(JA)))

ajouterCarteMain(main(JoueurAdverse),piocher(pioche(JoueurAdverse)))
ajouterCarteMain(main(JoueurAdverse),piocher(pioche(JoueurAdverse)))
ajouterCarteMain(main(JoueurAdverse),piocher(pioche(JoueurAdverse)))

#Une autre unité tirée est démobilisée et envoyée au royaume

entrerRoyaume(royaume(JA),piocher(pioche(JA)))
entrerRoyaume(royaume(JoueurAdverse),piocher(pioche(JoueurAdverse)))    

#J1 : Une carte est envoyée au front
premierAjoutFront(JA)
#J2 : Une carte est envoyée au front 
premierAjoutFront(JoueurAdverse)
#J1 : Une carte est envoyée en reserve
premierAjoutReserve(JA)
#J2 : Une carte est envoyée en reserve
premierAjoutReserve(JoueurAdverse)
    
#=== ==== La partie commence ==== === 
          
while(not(finDePartieEff) and not(finDePartieRoi) and not(finDePartiePioche)) :
    #=== ==== Déroulement d'un tour ==== ===
    #JA = Joueur actif
    JA = joueurCourant(Partie)
    JoueurAdverse = joueurAdverse(Partie)

    #==== Phase Préparation : ===== 
    # JA : Redresse ses cartes du champ de bataille en vertical (prêt à attaquer)
    redresseCartes(champBataille(JA))

    # JA : Mobilise une nouvelle unité = Pioche une carte
    ajouterCarteMain(main(JA),piocher(pioche(JA)))

    # 
    #==== Phase Action ====
    # JA doit soit : 
    action = int(input(nom(JA) + " que voulez vous faire dans ce tour ? \n0 : Rien \n1 : Mettre une carte en réserve \n2 : Déployer une unité \n3: Attaquer une cible\nAction : "))
    while not(verifAction(action)) :
        print(nom(JA) + " vous n'avez pas entré une action correcte ! ")
        action = int(input("Que voulez vous faire dans ce tour ? \n0 : Rien \n1 : Mettre une carte en réserve \n2 : Déployer une unité \n3: Attaquer une cible\nAction : "))

    #Une fois sorti de la boucle, action est un entier compris entre 0 et 3.

    if action == 0 : #Aucune action 
        print(nom(JA)+" ne fait aucune action !")
    elif action == 1 : 
    # == Met en Reserve ==
        #Envoi une unité de sa main sur la reserve
        if nbCarteMain(main(JA)) >= 1 :

            print(descriptionMain(main(JA)))
            choix = int(input("Quelle carte voulez-vous envoyer en réserve ?"))
            
            Carte = extraireCarteMain(main(JA),choix) 
            envoiReserve(reserve(JA),Carte) 
            
            print("Votre carte est maintenant dans la réserve")
        else : #Si j'ai pas d'unité dans ma main je peux rien faire 
            print("Comment voulez-vous ajouter une carte à votre réserve si vous n'avez pas de carte dans votre main ?")


    elif action == 2 : #déploie une unité 
    # == Déployer une unité ==

    # 1 - Met une unité sur la champ de bataille 
    #   Si JA a une unité dans sa réserve : 
        if nbCarteReserve(reserve(JA)) >= 1 : 
            Carte = premierCarteReserve(reserve(JA))
        elif nbCarteMain(main(JA)) >= 1 : 
            print(descriptionMain(main(JA)))
            choix = int(input("Quelle carte voulez-vous envoyer en réserve ?"))
            Carte = extraireCarteMain(main(JA),choix)
        else : 
            print("Wesh t'as pas de carte à poser gros !")

    # La carte est placée sur le champ de bataille

    # 1.b - L'unité doit être placée sur le front ou derrière une unité déjà présente au front
        if nbCarteFront(front(champBataille(JA))) + nbCarteArriere(arriere(champBataille(JA))) == 0 : 
        #Si c'est la premiere unité:
            choix = int(input("Votre carte doit aller au front. A quelle position voulez vous la mettre. 1, 2 ou 3\n Choix : "))#avec int() on vérifie que l'utilisateur nous renvoie bien un int
            position = "F"+str(choix)
            envoyerFront(front(champBataille(JA)),Carte,position) 
        
        else : 
            choix = input("Où voulez-vous placer votre carte ?\nPosition : ")
            while(not(positionValide(choix,JA))):
                choix = input("Attention, vous avez entré une mauvaise position !\nOù voulez-vous placer votre carte ?\nPosition : ")
    # 1.c - Une unité (C2) peut être placée sur une carte placée (C1) : 

            if(choix[0]=="F"):
            
                if(not(estVidePosition(champBataille(JA),choix))):
                    #C1 va dans la reserve en fin de file 
                    CarteDejaPlacee = extraireFront(front(champBataille(JA)),choix)
                    envoiReserve(reserve(JA),CarteDejaPlacee) 
                envoyerFront(front(champBataille(JA)),Carte,choix)
                
            else : #si choix[0] == "A"
                if(not(estVidePosition(champBataille(JA),choix))):
                    #C1 va dans la reserve en fin de file 
                    CarteDejaPlacee = extraireArriere(arriere(champBataille(JA)),choix)
                    envoiReserve(reserve(JA),CarteDejaPlacee)
                envoyerArriere(arriere(champBataille(JA)),Carte,choix)

    else : #action == 3  #Attaque 
        # == Attaquer ==
            veutAttaquer = True
            touteHorizontale=touteHorizontale(champBataille(JA))
            while(not(touteHorizontale) and veutAttaquer):                
                # JA choisi une cible 
                positionCible = input("Quelle est la position de la cible à attaquer ?\nChoix (sous la forme A1,A2,A3,F1,F2,F3) : ")
                #Verification à faire :
                        #Vérifier qu'il y a bien une carte ? Vérfier que la position est bien du type A ou F + 1 2 ou 3 
                while(not(estPosition(positionCible)) or estVidePosition(champBataille(JoueurAdverse),positionCible)) :
                    print("Attention la coordonnée entrée n'est pas valide")
                    positionCible = input("Quelle est la position de la cible à attaquer ?\nChoix (sous la forme A1,A2,A3,F1,F2,F3) : ")

                Cible = obtenirCarte(champBataille(JoueurAdverse),positionCible)
                ciblePresente = True #La cible est dans le combat. Elle en sortira si elle est capturée ou tuée

                # JA choisi sa / ses cartes d'attaque (boucle pour chaque carte) 
                veutAttaquerCible = True
                while(not(touteHorizontale(champBataille(JA))) and veutAttaquerCible and ciblePresente) :
                    positionCarte = input("Quelle est la position de votre unité qui attaque ?")
                    while (estVidePosition(champBataille(JA),positionCarte) or not(estPosition(positionCarte)) or not(estVerticale(obtenirCarte(champBataille(JA),positionCarte)))) :
                        positionCarte = input("Il semblerait qu'il n'y ait pas de carte ici. Quelle est la position de votre unité qui attaque ?")
                          
                    Carte = obtenirCarte(champBataille(JA),positionCarte)
                    
                    if(estAPortee(Carte,Cible)):
                        # Attaque la cible 
                        # Elle passe en position offensive
                        changementMode(Carte)
                        
                        # = Resultat de l'attaque =   
                        # Si L'attaque de la carte = Defense cible et Degat == 0 :
                        if (pointAttaque(Carte) == pointDefense(Cible)) and pointDegat(Cible) == 0 :
                            # La cible est capturée
                            capture(Cible,JA)
                            if roleCarte(Cible) == "Roi" : 
                                finDePartieRoi = True 
                            ciblePresente = False #La cible quitte le combat 
                            # La carte va dans Royaume de JA = devient citoyen (Cartes gardent role dans royaume voir figure)
                            entrerRoyaume(royaume(JA),Carte)
                            # Sinon si Attaque C1 < Defense Cible - Degats déjà subits 
                        elif (pointAttaque(Carte) < pointDefense(Cible) - pointDegat(Cible)) : 
                            # La cible recoit autant de dégat que de point d'attaque de la carte de JA
                            # Degat += Attaque carte
                            setPointDegat(Cible,pointDegat(Cible)+pointAttaque(Cible))   
                            
                            # Elle reste en place et pourra etre rattaquée 
                        else : 
                            # La carte va au cimetière (RIP)
                            entrerCimetiere(cimetiere(JA), Carte)
                            ciblePresente = False #La cible quiite le combat  
                            # Si une unité se trouve derrière elle, elle prend sa place
                            if verifArriere(champBataille(JoueurAdverse),positionCible) :
                                avancerCarte(champBataille(JA),positionCible) 
                        # Il faut vérifier si le champ de bataille adverse est vide
                        # Si le champ est vide:
                            if champEstVide(JoueurAdverse) : 
                                print("Attention il semblerait que le champ de bataille de "+ nom(JoueurAdverse) +" soit vide !")

                                #Si il y a deux unités dans la réserve : 
                                if (nbCarteReserve(reserve(JoueurAdverse))) >= 2 :
                                    print("Super il y a assez de cartes dans la réserve !")
                                    deploiementCarte(JoueurAdverse,2,0)
                                else:
                                    if nbCarteReserve(reserve(JoueurAdverse)) == 1 :
                                        if nbCarteRoyaume((JoueurAdverse)) >= 1 :
                                            #on demande une carte de la reserve et une carte de sa main 
                                            deploiementCarte(JoueurAdverse,1,1)
                                        else :
                                            print("Le royaume s'effrondre")
                                            effronde(royaume(JoueurAdverse))
                                            finDePartieEff = True

                                    elif nbCarte(reserve(JoueurAdverse)) == 0 :
                                        if nbCarte(main(JoueurAdverse)) >= 2 :
                                            #On demande deux carte de sa main
                                            deploiementCarte(JoueurAdverse,0,2)
                                        else : 
                                            print("Le royaume s'effrondre")
                                            effronde(royaume(JoueurAdverse))
                                            finDePartieEff = True
                    else :
                        
                        print("Attention, la cible n'est pas à la portée de votre carte !!")

                    veutAttaquerCible = demandeAttaquerCible(JA) 
                    
            #        #            #Sinon Si on peut compléter: 
            #        #                #On utilise une (ou aucune) carte de la reserve et on complète avec les cartes de son royaume
            #        #                # Impossible de poser la seconde carte sur la premiere
            #        #            #Sinon : 
            #        #                #Le royaume s'effondre
            #        #                
            #        # = FIN Resultat de l'attaque =
                    
                touteHorizontale=touteHorizontale(champBataille(JA))
                if(not(touteHorizontale)): 
                    print("Vous pouvez encore attaquer")
                    veutAttaquer = demanderAttaquer(JA)

            #
            # 

# == FIN de l'attaque ==
# ==== FIN de la phase ACTION ====


    # ==== PHASE Developpement ==== 
    #    # Si sa main >= 6 cartes :                      
    #        # JA doit ajouter au royaume une carte de sa main
    #    # Sinon 
    #        # JA peut ajouter au royaume une carte de sa main

    if(nbCarteMain(main(JA))>=6 or demandeDevelop(JA)):
      
        print(descriptionMain(main(JA)))
        choix = int(input(nom(JA) + ", quelle carte voulez-vous envoyer au royaume ?"))
        Carte = extraireCarteMain(main(JA),choix)
        entrerRoyaume(royaume(JA),Carte) 

    # ==== FIN PHASE DEVELOPPEMENT ====
    
#FIN DU TOUR
            
    #Condition de fin de partie : 
        #Soit l'effondrement : Si un joueur n'a plus de quoi rajouter des unités sur le CHAMP DE BATAILLE
              
        #Soit l'execution : Si le roi d'un joueur est capturé
   
        #Soit Fin de la guerre : Aucun joueur n'a de pioche
    if(nbCartePioche(pioche(JA)) == 0 and nbCartePioche(pioche(JoueurAdverse)) == 0):
        finDePartiePioche = True
        
    print("Fin du tour")
    
              
# Changement de joueur actif (JA)
    changeJoueurCourant(Partie)
    
if finDePartiePioche : 
    if nbCarteRoyaume(royaume(JA)) > nbCarteRoyaume(royaume(JoueurAdverse)) :
        print("Bravo " + nom(JA) + ", vous avez remporté cette partie !!")
    elif  nbCarteRoyaume(royaume(JA)) < nbCarteRoyaume(royaume(JoueurAdverse)) :
        print("Bravo " + nom(JoueurAdverse) + ", vous avez remporté cette partie !!")
    else : 
        print("Egalité !!")