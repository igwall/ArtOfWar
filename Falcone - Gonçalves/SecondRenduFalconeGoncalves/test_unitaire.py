#coding:utf-8
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
        
#==== ==== TEST PARTIE ==== ====# 
def testCreerPartie(JoueurTest1,JoueurTest2):
    print("# Test 1:")
    Partie = creerPartie(JoueurTest1,JoueurTest2)

    if joueurCourant(Partie) == JoueurTest1 and joueurAdverse(Partie) == JoueurTest2:
        print("Votre fonction creerPartie() a pris en considération vos deux joueurs, elle fonctionne correctement." )
    else: 
        print("La fonction creerPartie ne fonctionne pas correctement")
    
# ==  Test sur les joueur ==#



#==== ==== TEST JOUEUR ==== ====#
def testJoueurAdverse(Partie):
    print("# Test 2:")
    if joueurAdverse(Partie) == JoueurTest2:
        print("Test du Joueur Adverse fonctionnel, la fonction retourne le bon joueur adverse")
    else:
        print("La fonction joueurAdverse() ne renvoi pas correctement le joueur adverse du Joueur Courant")
        
        
def testChangeJoueurCourant(Partie):
    print("# Test 3:")
    joueurCourant = joueurCourant(Partie)
    changeJoueurCourant(Partie)
    nouveauJoueurCourant = joueurCourant(Partie)
    if (nouveauJoueurCourant == joueurAdverse(joueurCourant)):
        print("La fonction changeJoueurActif() fonctionne correctement !")
    else: 
        print("La fonction changeJoueurCourant() n'a pas correctement changée le joueur Courant")

        
        
#==== ==== TEST LIES AU JOUEUR ==== ====#

def testNomJoueur(Joueur):
    print("# Test 4:")
    if nom(Joueur) == "Joueur1":
        print("La fonction nom() affiche correctement le nom du joueur")
    else:
        print("Erreur, la fonction nom() ne renvoi pas la bonne valeur")



#==== ==== TEST ELEMENTS CREES ==== ====#
def testCreerRoyaume():
    print("# Test 5:")
    royaume  = creerRoyaume()
    if nbCarteRoyaume(royaume) == 0:
        print("La fonction de création de Royaume fonctionne correctement")
    else: 
        print("La fonction de création de Royaume ne fonctionne pas")
    
    

def testCreerReserve():
    print("# Test 6:")
    Reserve = creerReserve()
    if nbCarteReserve(Reserve) == 0:
        print("La fonction de création de Reserve fonctionne correctement")
    else: 
        print("La fonction de création de Reserve ne fonctionne pas")
        
        
        

def testCreerPioche():
    print("# Test 7:")
    if nbCartePioche(creerPioche(1)) == 20:
        print("La création de pioche fonctionne correctement")
    else:
        print("La création de pioche n'est pas fonctionnel...")
        
        
def testCreerMain():
    print("# Test 8:")
    if nbCarteMain(creerMain(1)) == 1: #Il y a un roi dans la main 
        print("La fonction de création retourne bien une main vide")
    else:
        print("La fonction de création ne retourne pas une main vide")
        

        

def testAjouterCarteMain(Main):
    print("# Test 9:")
    if nbCarteMain(Main) == 1:
        print("La fonction d'ajout de carte a correctement ajoutée la carte.")
    else:
        print("La fonction d'ajout de carte ne fonctionne pas, la carte n'a pas été ajoutée correctement.")
    
# ==== ==== TEST PIOCHE ==== ====#
        
def testPiocher(pioche):
    print("# Test 10:")
    prePioche = nbCartePioche(pioche)
    piocher(pioche)
    postPioche = nbCartePioche(pioche)
    if prePioche == postPioche: 
        print("La fonction ne retire pas la carte comme souhaité")
    elif prePioche == postPioche+1: 
        print("La fonction retire correctement la carte")
    else: 
        print("Erreur, le nombre de carte prePioche et postPioche est anormal.")


def testAjouterPioche(pioche):
    print("# Test 11:")
    prePioche = nbCartePioche(pioche)
    carte = piocher(pioche)
    postPioche = nbCartePioche(pioche)
    if prePioche == postPioche+1: 
        ajouterCartePioche(pioche,carte)
        if nbCartePioche(pioche) == prePioche:
            print("La fonction d'ajoute de carte fonctionne correctement !")
        else: 
            print("La carte n'a pas été ajoutée correctement")
    else: 
        print("Erreur, le nombre de carte prePioche et postPioche est anormal.")
        
        
def testEstVideChamp(champ):
    print("# Test 12:")
    if estVide(champ):
        print("La fonction estVide(champ) fonctionne correctement")
    else:
        print("La fonction n'est pas correcte.")
        
def testNbCarteChampBataille(champ) : 
    print("# Test 13:")
    if nbCarteChampBataille(champ) == 0:
        print("La fonction nbCarteChampBataille() fonctionne correctement !")
    else:
        print("La fonction nbCarteChampBataille() ne fonctionne pas correctement.")



def testEnvoyerFront(front,carte,position):
    print("# Test 14:")
    envoyerFront(front,carte,position)
    if estVidePosition(front,position):
        print("La carte ne s'est pas ajoutée correctement ")
    elif positionCarte(carte) == position: 
        print("L'ajout de la carte au front s'est fait correctment !")
    else: 
        print("Erreur sur l'ajout au front, il n'est pas vide mais la position de la carte n'est pas celle indiquée en ajout. ERREUR dans la fonction positioncarte()")
        
def testObtenirCarte(front,champ,position):
    print("# Test 15:")
    carte = extraireFront(front,position)
    envoyerFront(front,carte,position)
    cartepose = obtenirCarte(champ,position)
    if carte == cartepose:
        print("La fonction obtenirCarte() fonctionne correctement !")
    else:
        print("La fonction obtenirCarte() ne renvoi pas la carte comme convenu.")
        
        
def testEnvoyerArriere(arriere,carte,position):
    print("# Test 16:")
    envoyerArriere(arriere,carte,position)
    if estVidePosition(front,position):
        print("La carte ne s'est pas ajoutée correctement ")
    elif positionCarte(carte) == position: 
        print("L'ajout de la carte à l'arriere s'est fait correctment !")
    else: 
        print("Erreur sur l'ajout à l'arriere, il n'est pas vide mais la position de la carte n'est pas celle indiquée en ajout. ERREUR dans la fonction positioncarte()")

def testNbCarteFront(front):
    print("# Test 17:")
    if nbCarteFront(front) == 1:
        print("La fonction nbCarteFront() fonctionne correctement")
    else: 
        print("La fonction nbCarteFront() est incorrecte.")

def testNbCarteArriere(front):
    print("# Test 18:")
    if nbCarteFront(front) == 1:
        print("La fonction nbCarteArriere() fonctionne correctement")
    else: 
        print("La fonction nbCarteArriere() est incorrecte.")

def testExtraireFront(front,position):
    print("# Test 19:")
    carte = extraireFront(front,position)
    if estVidePosition(front,position):
        print("La carte ajoutée précédement a bien été extraite, la fonction extraireFront() fonctionne !")
        envoyerFront(front,carte,position)
        
    else:
        print("La carte ajoutée précédement n'a pas été extraite, la fonction extraireFront() ne fonctionne pas.")

def testExtraireArriere(arriere,position):
    print("# Test 20:")
    carte = extraireArriere(arriere,position)
    if estVidePosition(arriere,position):
        print("La carte ajoutée précédement a bien été extraite, la fonction extraireArriere() fonctionne !")
        envoyerArriere(arriere,carte,position)
        #On renvoi la carte a sa position pre-test
    else:
        print("La carte ajoutée précédement n'a pas été extraite, la fonction extraireFront() ne fonctionne pas.")
        
def testVerifArriere(champ,position):
    print("# Test 21:")
    if verifArriere(champ,position):
        print("La fonction verifArriere fonctionne correctement !")
    else:
        print("La fonction verifArriere ne fonctionne pas correctement.")
        
def testEstVidePosition(champ,position):
    print("# Test 22:")
    positionBis = "A1"
    if not(estVidePosition(champ,position)) and estVidePosition(champ,positionBis):
        print("La fonction estVidePosition fonctionne correctement")
    elif estVidePosition(champ,position) :
        print("La fonction estVide ne fonctionne pas, une carte devrait se trouver en A2, verifier la fonction envoyerArriere() ou la fonction estVidePosition.")
    else:
        print("La fonction estVidePosition ne fonctionne vraiment pas du tout !")
    

def testAvancerCarte(champ,position):
    print("# Test 23:")
    carte = obtenirCarte(champ,position)
    avancerCarte(champ,position)
    cartebis = obtenirCarte(champ,"F2")
    carteter = obtenirCarte(champ,"A2")
    if roleCarte(carte) == roleCarte(cartebis):
        print("La fonction avancerCarte() fonctionne. La carte a correctement été envoyée au front")
    elif carte == carteter :
        print("La carte n'a pas bougée ou a été dupliquée sans modifier sa position")
    else :
        print("La fonction avancerCarte() ne fonctionne pas.")
        
def testEnvoiReserve(reserve,carte):
    print("# Test 24:")
    envoiReserve(reserve,carte)
    if nbCarteReserve(JoueurTest1) == 0:
        print("La fonction d'envoi dans la reserve ne fonctionne pas correctement")
    elif nbCarteReserve(JoueurTest1) == 1:
        print("La fonction envoiReserve() fonctionne correctement !")
    else:
        print("La fonction envoiReserve ne fonctionne pas ! elle a plus d'une carte, elle ne devrait en avoir qu'une seule !")
    
def testPremiereCarteReserve(reserve,carte):
    print("# Test 25:")
    premCarte = premiereCarteReserve(reserve)
    if roleCarte(premCarte) == roleCarte(carte):
        print("La fonction premiere carte reserve fonctionne correctement !")
    else:
        print("La fonction premiere carte reserve ne fonctionne pas correctement !")

    
def testEntrerRoyaume(royaume,carte):
    print("# Test 26:")
    entrerRoyaume(royaume,carte)
    if nbCarteRoyaume(royaume) == 0:
        print("La fonction entrerRoyaume() n'a pas ajoutée la carte, le royaume est vide.")
        print("La fonction nbCarteRoyaume() ne fonctionne peut etre pas...")
    elif nbCarteRoyaume(royaume) == 1:
        print("La fonction entrerRoyaume() a bien ajoutée une carte !")
    
def testExtraireRoyaume(royaume,role):
    print("# Test 27:")
    if nbCarteRoleRoyaume(royaume,role) == 1:
        print("La fonction nbCarteRoleRoyaume() fonctionne correctement !")
        carteExtraire = extraireRoyaume(royaume,role)
        if role == roleCarte(carteAjoutee):
            print("La fonction extraireRoyaume extrait bien une carte du role passé en paramètre !")
        else:
            print("La fonction n'a pas extraite une carte du role placé en paramètre.")
            
    elif nbCarteRoleRoyaume(royaume,role) == 0:
        print("Il y a un soucis dans la fonction entrerRoyaume(), la fonction nbCarteRoleRoyaume retourne 0, elle devrait retourner 1")
    else:
        print("La fonction nbCarteRoleRoyaume ne fonctionne pas. Vérifier également le test d'entree dans le royaume.")
    
def testEffondre(royaume):
    print("# Test 28:")
    royaume = effondre(royaume)
    if estEffondre(royaume):
        print("Le royaume est effectivement effondré")
    else:
        print("La fonction d'éffondrement OU de vérification d'éffondrement ne fonctionne pas correctement, vérifier effondre() et estEffondre() ")
    
def testChangementMode(carte):
    print("# Test 29:")
    if estVerticale(carte):
        changementMode(carte)
        if estVerticale(carte):
            print("La fonction changementMode() ne fonctionne pas.")
        if not(estVerticale(carte)):
            print("La fonction changementMode() fonctionne correctement")
    else:
        changementMode(carte)
        if estVerticale(carte):
            print("La fonction changementMode() fonctionne correctement")
        if not(estVerticale(carte)):
            print("La fonction changementMode() ne fonctionne pas.")
            
        
def testTouteHorizontale(champ,carte):
    print("# Test 30:")
    redresseCartes(champ)
    if touteHorizontale(champ):
        print("Erreur, les cartes sont sencés être redréssées mais la fonction touteHorizontale() dit quelles sont toutes horizontales !")
    else:
        print("La fonction touteHorizontale() fonctionne correctement")
        print("La fonction redresesCartes() ne fonctionne pas.")
            
        
def testCapture(carte,Joueur):
    print("# Test 31:")
    role = roleCarte(carte)
    capture(carte,Joueur)
    if nbCarteRoleRoyaume(royaume(Joueur),role) == 1:
        print("La fonction capture() fonctionne correctement !")
    else:
        print("La fonction capture() ne foctionne pas !")
    
def testSetPositionCarte(carte,pos):
    print("# Test 32:")
    positionBase = positionCarte(carte)
    carteDeplacee = setPositionCarte(carte,pos)
    if positionCarte(carteDeplacee) == positionBase:
        print("La fonction setPositionCarte() ne fonctionne pas")
    elif positionCarte(carteDeplacee) == pos:
        print("La fonction setPositionCarte() fonctionne correctement")
    else:
        print("La fonction setPositionCarte() ne fonctionne pas, la carte ne concerve pas sa position et ne prend pas en compte sa nouvelle position.")
    
# ==== ==== Programme principal ==== ====#
nom1 = "Joueur1"
nom2 = "Joueur2"
#Création des joueur
JoueurTest1 = creerJoueur(1,nom1)
JoueurTest2 = creerJoueur(2,nom2)
testNomJoueur(JoueurTest1)
#Creation de la partie
testCreerPartie(JoueurTest1,JoueurTest2)
Partie = creerPartie(JoueurTest1,JoueurTest2)

testJoueurAdverse(Partie)

testCreerRoyaume()
testCreerReserve()
testCreerPioche()
testCreerMain()

#Teste la fonction piocher(pioche)
testPiocher(pioche(JoueurTest1))


#Test d'ajout d'une carte dans la pioche 

carte = piocher(pioche(JoueurTest1))
testAjouterPioche(pioche(JoueurTest1))

#On revient à la pioche de base



#Test d'ajout de la carte dans la main du joueur 
testAjouterCarteMain(main(JoueurTest1))

#Ajout de cartes à la main du Joueur 1 pour la suite des test
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))

#Ajout de cartes à la main du Joueur 2 pour la suite des test
ajouterCarteMain(main(JoueurTest2),piocher(pioche(JoueurTest2)))
ajouterCarteMain(main(JoueurTest2),piocher(pioche(JoueurTest2)))
ajouterCarteMain(main(JoueurTest2),piocher(pioche(JoueurTest2)))
ajouterCarteMain(main(JoueurTest2),piocher(pioche(JoueurTest2)))
ajouterCarteMain(main(JoueurTest2),piocher(pioche(JoueurTest2)))

#On ajoute des cartes au champ de bataille
testEstVideChamp(champBataille(JoueurTest1))
testNbCarteChampBataille(champBataille(JoueurTest1))

# ===== ==== Test d'ajout une carte au front au Joueur1
# == On test d'abbord d'etraire une carte de la main 
                      
indice = 1
# = On extrait la carte
carte = extraireCarteMain(main(JoueurTest1),indice)
# == On essai d'ajouter une carte au front 
positionFront1 = "F1"
testEnvoyerFront(front(champBataille(JoueurTest1)),carte,positionFront1)
# La carte doit désormais etre présente sur le champ. 
# On ajoute une carte sur le front adverse : 
      
# ===== ==== Test d'ajout une carte au front au Joueur2

indice = 1
carte = extraireCarteMain(main(JoueurTest2),indice)
# == On essai d'ajouter la carte extraite au front 
positionFront2 = "F3"
testEnvoyerFront(front(champBataille(JoueurTest2)),carte,positionFront2)

testObtenirCarte(front(champBataille(JoueurTest1)),champBataille(JoueurTest1),positionFront2)
                      
                      
# ===== ==== Test d'ajout une carte à l'arriere au Joueur1
# == On extrait d'abbord une carte de la main 
indice = 1
carte = extraireCarteMain(main(JoueurTest1),indice)
# == On essai d'ajouter une carte à l'arriere 
positionArriere = "A2"
testEnvoyerArriere(arriere(champBataille(JoueurTest1)),carte,positionArriere)
# La carte doit désormais etre présente sur le champ. 
# On ajoute une carte sur le Arriere adverse : 
      
# ===== ==== Test d'ajout une carte a l'arriere au Joueur2


indice = 1
carte = extraireCarteMain(main(JoueurTest2),indice)

# == On essai d'ajouter une carte au Arriere 
positionArriere = "A2"
testEnvoyerArriere(arriere(champBataille(JoueurTest2)),carte,positionArriere)
# = La carte est à l'arriere en diagonale droite de celle au front
# = Test qui vérifie que le front devant la carte que l'on viens d'ajouter est vide (ce qui doit etre le cas !):

# On vérifie le nombre de carte à l'arriere et à l'avant: 
testNbCarteFront(front(champBataille(JoueurTest1)))
testNbCarteArriere(front(champBataille(JoueurTest1)))

# Test de l'extraction d'une carte du front du Joueur1, elle est remise à sa place à la fin du test:
positionExtraire1 = "F1"
testExtraireFront(front(champBataille(JoueurTest1)),positionExtraire1)
                      
# Test de l'extration d'une carte de l'arriere du Joueur1, elle est remise à sa place à la fin du test (position F3):

testExtraireArriere(arriere(champBataille(JoueurTest1)),positionArriere)



# Verifie qu'aucune carte n'est présente derriere celle ajoutée précédement. Doit retourner True car aucune carte n'est effectivement présente en A1
testVerifArriere(champBataille(JoueurTest1),positionExtraire1)

# Test pour voir si la fonction estVidePosition fonctionne correctement. 
# Elle vérifie une position vide et une position prise pour plus de robustesse. 
testEstVidePosition(champBataille(JoueurTest1),positionArriere)


carteFront = extraireCarteMain(main(JoueurTest1),2)
envoyerFront(front(champBataille(JoueurTest1)),carteFront,"F3")
       
testAvancerCarte(champBataille(JoueurTest1),"F2")

#On fait avancer la carte située en A2 vers F2. On doit vérifier que la carte en F2 atterie bien dans la reserve

# ==== ==== On test des envois dans la reserve !
# ==== ==== On se rajoute quelques petites cartes avant !
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))
ajouterCarteMain(main(JoueurTest1),piocher(pioche(JoueurTest1)))

# On envoi dans la reserve
carteReserve = extraireCarteMain(main(JoueurTest1),3)
testEnvoiReserve(reserve(JoueurTest1),carteReserve)
# On teste que la carte ai bien été envoyée et que la fonction premiereCarteReserve fonctionne correctement. 
testPremiereCarteReserve(reserve(JoueurTest1),carteReserve)
                      
#On va en envoyer une ou deux dans le Royaume maintenant ! 

carteRoy = extraireCarteMain(main(JoueurTest2),1)
role = roleCarte(carteRoy)
testEntrerRoyaume(royaume(JoueurTest1),carteRoy)
testExtraireRoyaume(royaume(JoueurTest1),role)
                      
#Test d'effondrement d'un royaume :
testEffondre(royaume(JoueurTest1))

#Test de estVerticale() et de changementMode()
carteModifMode = obtenirCarte(champBataille(JoueurTest1),"F1")
testChangementMode(carteModifMode)

#Test de touteHorizontale() et donc de redresseCartes:
testTouteHorizontale(champBataille(JoueurTest1),carteModifMode)
                      
#Test de la capture :
carteCapture = obtenirCarte(champBataille(JoueurTest1),"F1")
testCapture(carteCapture,JoueurTest2)

#Test de la fonction setPositionCarte
# A la position F2 se trouve la carte qui était en A2 et qui s'est vue avancée
carteModifPosition = obtenirCarte(champBataille(JoueurTest1),"F2")
#On envoi la carte en A3
testSetPositionCarte(carteModifPosition,"A3")