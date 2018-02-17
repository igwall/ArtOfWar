#coding:utf-8
import os
import time
from package.carte import *
from package.cdb import *
from package.cimetiere import *
from package.joueur import *
from package.main import *
from package.pioche import *
from package.reserve import *
from package.royaume import *
from package.deckGen import *

def annonceJoueur(joueur) :
    annonceJoueurInt(get_ident(joueur))

def annonceJoueurInt(num):
    print("-- Joueur "+str(num)+", préparez vous --")
    time.sleep(5)
    os.system('clear')
    print("--- Joueur "+str(num)+" ---\n\n")


def main():
    os.system('clear')
    print("Bienvenue dans ArtOfWar\n")
    deckGen = creerDeck()
    #On crée toutes les composantes nécessaires au jeu
    joueur1 = creer_joueur(1, creer_pioche(2,deckGen), creer_main(), creer_royaume(), creer_cdb(), creer_cimetiere(), creer_reserve())
    joueur2 = creer_joueur(2, creer_pioche(22,deckGen), creer_main(), creer_royaume(), creer_cdb(), creer_cimetiere(), creer_reserve())
    #---

    #On mélange les deux pioches avant la mise en place
    melanger_pioche(get_pioche(joueur1))
    melanger_pioche(get_pioche(joueur2))
    #---

    #On crée les roi pour les joueurs
    roi1 = creer_carte(0,"roi1","def")
    ajouterCarte(deckGen,roi1)
    roi2 = creer_carte(1,"roi2","def")
    ajouterCarte(deckGen,roi2)
    #---

    #Début de la phase de mise en place
    #On place dans la main du joueur 1 son Roi ainsi que 3 cartes tirées au hasard
    placer_dans_main(roi1, get_main(joueur1))
    placer_dans_royaume(piocher_carte(get_pioche(joueur1)),get_royaume(joueur1))
    #La première carte pioché est placer directement dans le royaume
    placer_dans_main(piocher_carte(get_pioche(joueur1)),get_main(joueur1))
    placer_dans_main(piocher_carte(get_pioche(joueur1)),get_main(joueur1))
    #---

    #On place dans la main du joueur 2 son Roi ainsi que 3 cartes tirées au hasard
    placer_dans_main(roi2, get_main(joueur2))
    placer_dans_royaume(piocher_carte(get_pioche(joueur2)),get_royaume(joueur2))#La première carte pioché est placer directement dans le royaume
    placer_dans_main(piocher_carte(get_pioche(joueur2)),get_main(joueur2))
    placer_dans_main(piocher_carte(get_pioche(joueur2)),get_main(joueur2))
    #---

    #Le premier joueur choisit une carte de sa main et la place sur sa ligne de front
    #On affiche la main pour que le joueur connaisse les cartes qu'il a en main
    print("----- Initialisation du jeu --------")
    print("--- Joueur 1 ---\n\n")
    print(decrire_main(get_main(joueur1)))
    IDcarte_choisi = int(int(input("Choisir la carte à placer sur la ligne de front du joueur 1 : ")))
    carte_choisi = getCarte(deckGen, IDcarte_choisi)

    #FG Il manquait ici la main dans la fonction est_dans_main
    while not est_dans_main(carte_choisi,get_main(joueur1)) :
        IDcarte_choisi = int(input("Choisir la carte à placer sur la ligne de front du joueur 1 : "))
        carte_choisi = getCarte(deckGen, IDcarte_choisi)

    #On affiche le champ de bataille pour que le joueur connaisse les positions disponibles
    print(decrire_cdb(get_cdb(joueur1)))
    case_choisi = int(input("Quelle case de la ligne de front ? " ))
    while not est_position_utilisable(get_cdb(joueur1),case_choisi):
        case_choisi = int(input("Quelle case de la ligne de front ? " ))
    placer_dans_cdb(carte_choisi, get_cdb(joueur1), case_choisi)
    retirer_de_main(carte_choisi, get_main(joueur1))
    print("Très bien")
    print(decrire_cdb(get_cdb(joueur1)))
    #---

    #Initialisation du joueur 2
    annonceJoueurInt(2)

    #Le second joueur choisit une carte de sa main et la place sur sa ligne de front
    print(decrire_main(get_main(joueur2)))
    IDcarte_choisi = int(input("Choisir la carte à placer sur la ligne de front du joueur 2 : "))
    carte_choisi = getCarte(deckGen,IDcarte_choisi)

    while not est_dans_main(carte_choisi,get_main(joueur2)) :
        IDcarte_choisi = int(input("Choisir la carte à placer sur la ligne de front du joueur 2 : "))
        carte_choisi = getCarte(deckGen,IDcarte_choisi)

    print(decrire_cdb(get_cdb(joueur2)))
    case_choisi = int(input("Quelle case de la ligne de front ? "))
    while not est_position_utilisable(get_cdb(joueur2),case_choisi) :
        case_choisi = int(input("Quelle case de la ligne de front ? "))
    placer_dans_cdb(carte_choisi, get_cdb(joueur2), case_choisi)
    retirer_de_main(carte_choisi, get_main(joueur2))
    print("Très bien")
    print(decrire_cdb(get_cdb(joueur2)))
    #---


    #Mise en réserve du joueur 1
    annonceJoueurInt(1)

    #Le premier joueur choisit une carte de sa main et la place en réserve
    print(decrire_main(get_main(joueur1)))
    IDcarte_choisi = int(input("Choisir la carte à placer en réserve du joueur 1 : "))
    carte_choisi = getCarte(deckGen,IDcarte_choisi)

    #FG Il manquait ici la main dans la fonction est_dans_main
    while not est_dans_main(carte_choisi,get_main(joueur1)) :
        IDcarte_choisi = int(input("Choisir la carte à placer en réserve du joueur 1 : "))
        carte_choisi = getCarte(deckGen,IDcarte_choisi)

    placer_dans_reserve(carte_choisi, get_reserve(joueur1))
    retirer_de_main(carte_choisi, get_main(joueur1))
    #---

    print("Très bien")
    print(decrire_reserve(get_reserve(joueur1)))


    #Mise en réserve du joueur 2
    annonceJoueurInt(2)


    #Le second joueur choisit une carte de sa main et la place en réserve
    print(decrire_main(get_main(joueur2)))
    IDcarte_choisi = int(input("Choisir la carte à placer en réserve du joueur 2 : "))
    carte_choisi = getCarte(deckGen,IDcarte_choisi)

    while not est_dans_main(carte_choisi,get_main(joueur2)) :
        IDcarte_choisi = int(input("Choisir la carte à placer en réserve du joueur 2 : "))
        carte_choisi = getCarte(deckGen, IDcarte_choisi)

    placer_dans_reserve(carte_choisi, get_reserve(joueur2))
    retirer_de_main(carte_choisi, get_main(joueur2))

    print("Très bien")
    print(decrire_reserve(get_reserve(joueur2)))

    #---

    #Fin de la phase de mise en place
    #############################################################################################################################################

    joueur = joueur1 #Le joueur 1 commence le premier
    annonceJoueur(joueur)
    partie_fini = False

    #début de la boucle de jeu

    while not partie_fini :

    #Début de la phase conscription

    #--- Fin de la phase de conscription

    #Début de la phase de préparation
        mettre_en_position_def(get_cdb(joueur))

        #On vérifie si le joueur a encore des cartes dans sa pioche, dans le cas contraire la partie est fini et on sort de la boucle de jeu (Fin de la guerre)
        if pioche_vide(get_pioche(joueur)):
            partie_fini = True
            raison_fin = "f"
            joueur_sans_carte = joueur
            break

        placer_dans_main(piocher_carte(get_pioche(joueur)),get_main(joueur))
    #---Fin de la phase de préparation

    #Début de la phase d'action
        print(decrire_cdb(get_cdb(joueur)))
        print(decrire_royaume(get_royaume(joueur)))
        print(decrire_main(get_main(joueur)))
        print(decrire_reserve(get_reserve(joueur)))

        #On demande l'action et on vérifie si c'est une action qui existe
        action = input("Que souhaitez vous faire ? \n Actions possibles :\n -Ne rien faire (n) \n -Mettre en réserve (r) \n -Déployer unité (d) \n -Attaquer (a)\nChoix : ")
        action_valide = False
        if(action == "n" or action == "r" or action == "d" or action == "a" ) :
            action_valide = True
        while (action_valide==False) :
            print("L'action demandée n'existe pas, veuillez choisir une action qui existe")
            action = input("Que souhaitez vous faire ? \n Actions possibles :\n -Ne rien faire (n) \n -Mettre en réserve (r) \n -Déployer unité (d) \n -Attaquer (a)\nChoix : ")
            if(action == "n" or action == "r" or action == "d" or action == "a" ) :
                action_valide = True

        #Mise en réserve
        if action == "r" :
            print(decrire_main(get_main(joueur)))
            IDcarte_choisi = int(input("Quelle carte souhaitez vous envoyer en réserve ? "))
            carte_choisi = getCarte(deckGen, IDcarte_choisi)

            while not est_dans_main(carte_choisi,get_main(joueur)):
                IDcarte_choisi = int(input("Quelle carte souhaitez vous envoyer en réserve ? "))
                carte_choisi = getCarte(deckGen, IDcarte_choisi)

            placer_dans_reserve(carte_choisi, get_reserve(joueur))
            retirer_de_main(carte_choisi, get_main(joueur))

        #Déploiement d'unité
        if action == "d" :
            if not reserve_vide(get_reserve(joueur)):
                print(decrire_reserve(get_reserve(joueur)))
                carte_choisi = piocher_dans_reserve(get_reserve(joueur))
                print("A quelle position souhaitez vous placer votre carte ? ")
                print(decrire_cdb(get_cdb(joueur)))
                case_choisi = int(input("Position choisie : "))
                while not est_position_utilisable(get_cdb(joueur),case_choisi):
                    case_choisi = int(input("Position choisie : "))
                placer_dans_cdb(carte_choisi,get_cdb(joueur), case_choisi)

            else :
                #fonction_interface.plusDeCarteEnReserve(joueur)
                print("Vous n'avez plus de cartes en réserve, choisissez une carte de votre main ")
                print(decrire_main(get_main(joueur)))
                IDcarte_choisi = int(input("Quelle carte souhaitez vous envoyer sur le champ de bataille ? "))
                carte_choisi = getCarte(deckGen,IDcarte_choisi)

                while not est_dans_main(carte_choisi,get_main(joueur)):
                    IDcarte_choisi = int(input("Quelle carte souhaitez vous envoyer sur le champ de bataille ? "))
                    carte_choisi = getCarte(deckGen,IDcarte_choisi)

                print("A quelle position voulez-vous la placer ? ")
                print(decrire_cdb(get_cdb(joueur)))
                case_choisi = int(input("Position choisie : "))
                while not est_position_utilisable(get_cdb(joueur),case_choisi):
                    case_choisi = int(input("Position choisie : "))

                placer_dans_cdb(carte_choisi,get_cdb(joueur), case_choisi)
                retirer_de_main(carte_choisi,get_main(joueur))

        #Attaque
        if action == "a" : #Les points de défenses des cartes attaquées seront remis à leur valeur par défaut une fois la phase d'attaque terminé
            if joueur == joueur1:
                print("Champ de bataille du joueur 2 : ")
                print(decrire_cdbAdverse(get_cdb(joueur2)))
                print("Champ de bataille du joueur 1 : ")
                print(decrire_cdb(get_cdb(joueur1)))
            else :
                print("Champ de bataille du joueur 1 : ")
                print(decrire_cdbAdverse(get_cdb(joueur1)))
                print("Champ de bataille du joueur 2 : ")
                print(decrire_cdb(get_cdb(joueur2)))

            fin_attaque = False

            #On commence la boucle d'attaque, le joueur va faire attaquer ses cartes une par une
            while not fin_attaque :
                #On demande la carte qui va attaquer et on effectue les vérifications nécessaires dessus
                #elle doit être dans le cdb du joueur et en position défensive
                IDcarte_choisi = int(input("Avec quelle carte souhaitez vous attaquer ? "))
                carte_choisi = getCarte(deckGen,IDcarte_choisi)

                while not est_dans_cdb(carte_choisi,get_cdb(joueur)) or not est_en_posture_defensive(carte_choisi):
                    if not est_dans_cdb(carte_choisi,get_cdb(joueur)) :
                        IDcarte_choisi = int(input("Cette carte n'est pas dans le champ de bataille, veuillez en choisir une autre : "))
                    elif not est_en_posture_defensive(carte_choisi) :
                        IDcarte_choisi = int(input("Cette carte est déjà en position offensive, elle ne peut plus attaquer du tour, veuillez en choisir une autre : "))
                    carte_choisi = getCarte(deckGen,IDcarte_choisi)


                carte_choisi = getCarte(deckGen,IDcarte_choisi)


                #On demande la cible à attaquer et on effectue les vérifications dessus
                IDcible = int(input("Quelle carte adverse souhaitez vous attaquer ? (Il faut donner l'ID de la carte / Non pas sa position) : "))
                cible = getCarte(deckGen,IDcible)

                #Vérification de présence de la cible dans le cdb adverse et de portée
                if joueur == joueur1 :
                    est_a_portee = touche(carte_choisi, cible, get_cdb(joueur1), get_cdb(joueur2))
                    est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(joueur2))
                if joueur == joueur2 :
                    est_a_portee = touche(carte_choisi, cible, get_cdb(joueur2), get_cdb(joueur1))
                    est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(joueur1))

                while not est_a_portee or not est_dans_cdb_adverse :
                    if not est_dans_cdb_adverse :
                        IDcible = int(input("La cible n'est pas dans le cdb adverse, veuillez en choisir une autre :"))
                    elif not est_a_portee :
                        IDcible = int(input("La cible n'est pas à portée, veuillez en choisir une autre : "))
                    cible = getCarte(deckGen,IDcible)
                    print(cible)
                    print(get_cdb(joueur2))
                    if joueur == joueur1 :
                        est_a_portee = touche(carte_choisi, cible, get_cdb(joueur1), get_cdb(joueur2))
                        est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(joueur2))
                    if joueur == joueur2 :
                        est_a_portee = touche(carte_choisi, cible, get_cdb(joueur2), get_cdb(joueur1))
                        est_dans_cdb_adverse = est_dans_cdb(cible, get_cdb(joueur1))


                mettre_en_offensif(carte_choisi)
                if joueur == joueur1 :
                    attaquer(carte_choisi,cible,get_cdb(joueur),get_cdb(joueur2),get_main(joueur))
                if joueur == joueur2 :
                    attaquer(carte_choisi,cible,get_cdb(joueur),get_cdb(joueur1),get_main(joueur))


                #On test si la conscription est possible, si elle ne l'est pas alors on sort de la boucle de jeu (effondrement)
                cdb_vide = get_nombre_carte_cdb(get_cdb(joueur))==0
                nb_reserve = get_nombre_carte_reserve(get_reserve(joueur))
                nb_royaume = get_nombre_carte_royaume(get_royaume(joueur))
                if cdb_vide and (nb_reserve + nb_royaume)<2 :
                    partie_fini = True
                    raison_fin = "ef"
                    joueur_perdant = joueur
                    break
                #---Fin test conscription

                #On vérifie si l'on doit entrer en phase de conscription en fonction du nombre de cartes restantes sur le champ de bataille
                if get_nombre_carte_cdb(get_cdb(joueur))==0:
                    print("Vous n'avez plus de carte sur le champs de bataille, vous devez recruter de force deux unités")
                    if get_nombre_carte_reserve(get_reserve(joueur))==1:
                        #On choisit la position à laquelle on place la dernière carte provenant de notre réserve
                        print("Vous n'avez plus qu'une seule carte dans votre réserve")
                        print(decrire_reserve(get_reserve(joueur)))
                        print("A quelle position voulez-vous la placer ?")
                        print(decrire_cdb(get_cdb(joueur)))

                        case_choisi = int(input("Position choisie : "))
                        while not est_position_utilisable(get_cdb(joueur),case_choisi) :
                            case_choisi = int(input("Position choisie : "))
                        derniere_carte_reserve = piocher_dans_reserve(get_reserve(joueur))
                        placer_dans_cdb(derniere_carte_reserve, get_cdb(joueur), case_choisi)
                        #---

                        #On choisit la carte de notre royaume et sa position sur le champ de bataille
                        print("Quelle carte de votre royaume souhaitez vous placer sur le champ de bataille")
                        print(decrire_royaume(get_royaume(joueur)))

                        IDcarte_choisi = int(input("Carte choisie : "))
                        carte_choisi = getDeck(deckGen,IDcarte_choisi)
                        while not est_dans_royaume(carte_choisi,get_royaume(joueur)) :
                                carte_choisi = int(input("Carte choisie : "))
                        print("A quelle position voulez-vous la placer ? ")
                        print(decrire_cdb(get_cdb(joueur)))
                        case_choisi = int(input("Position choisie : "))
                        while not est_position_utilisable(get_cdb(joueur),case_choisi):
                            case_choisi = int(input("Position choisie : "))
                        placer_dans_cdb(carte_choisi,get_cdb(joueur), case_choisi)
                        retirer_du_royaume(get_royaume(joueur), carte_choisi)

                    if get_nombre_carte_reserve(get_reserve(joueur))>1:
                        #On choisit la carte de notre reserve et on indique la position à laquelle on souhaite la poser sur le champ de bataille
                        print("Les deux premières cartes de votre réserve vont être placées sur le champ de bataille")
                        print(decrire_reserve(get_reserve(joueur)))

                        case_choisi = int(input("A quelle position souhaitez vous placer la première carte de votre réserve ? : "))
                        while not est_position_utilisable(get_cdb(joueur),case_choisi) :
                            case_choisi = int(input("A quelle position souhaitez vous placer la première carte de votre réserve ? : "))
                        placer_dans_cdb(piocher_dans_reserve(get_reserve(joueur)),get_cdb(joueur),case_choisi)

                        case_choisi = int(input("A quelle position souhaitez vous placer la deuxième carte de votre réserve ? : "))
                        while not est_position_utilisable(get_cdb(joueur),case_choisi) :
                            case_choisi = int(input("A quelle position souhaitez vous placer la deuxième carte de votre réserve ? : "))
                        placer_dans_cdb(piocher_dans_reserve(get_reserve(joueur)),get_cdb(joueur),case_choisi)

                    else :
                        print("Vous n'avez plus de carte dans votre réserve, vous devez donc mobiliser deux cartes de votre royaume ")
                        print("Veuillez choisir la première carte de votre royaume que vous souhaitez placer sur le champ de bataille")
                        print(decrire_royaume(get_royaume(joueur)))

                        IDcarte_choisi = int(input("Carte choisie : "))
                        carte_choisi = getDeck(deckGen,IDcarte_choisi)
                        while not est_dans_royaume(carte_choisi) :
                                IDcarte_choisi = int(input("Carte choisie : "))
                                carte_choisi = getDeck(deckGen,IDcarte_choisi)

                        print("A quelle position voulez-vous la placer ?")
                        print(decrire_cdb(get_cdb(joueur)))
                        case_choisi = int(input("Position choisie : "))
                        while not est_position_utilisable(get_cdb(joueur),case_choisi):
                            case_choisi = int(input("Position choisie : "))
                        placer_dans_cdb(carte_choisi,get_cdb(joueur), case_choisi)
                        retirer_du_royaume(get_royaume(joueur), carte_choisi)

                        print("Vous n'avez plus de carte dans votre réserve, vous devez donc mobiliser deux cartes de votre royaume ")
                        print("Veuillez choisir la deuxième carte de votre royaume que vous souhaitez placer sur le champ de bataille")
                        print(decrire_royaume(get_royaume(joueur)))

                        IDcarte_choisi = int(input("Carte choisie : "))
                        carte_choisi = getDeck(deckGen,IDcarte_choisi)

                        while not est_dans_royaume(carte_choisi) :
                                IDcarte_choisi = int(input("Carte choisie : "))
                                carte_choisi = getDeck(deckGen,IDcarte_choisi)

                        print("A quelle position voulez-vous la placer ?")
                        print(decrire_cdb(get_cdb(joueur)))
                        case_choisi = int(input("Position choisie : "))
                        while not est_position_utilisable(get_cdb(joueur),case_choisi):
                            case_choisi = int(input("Position choisie : "))

                        placer_dans_cdb(carte_choisi,get_cdb(joueur), case_choisi)
                        retirer_du_royaume(get_royaume(joueur), carte_choisi)

                #On vérifie le nombre de points de défense restant à la carte attaquer et on agit en fonction
                if get_point_de_defense(cible) == 0 and not aEteTouche(cible): #Cas où la cible est capturée
                    if joueur == joueur1:
                        position = get_position_carte(cible,get_cdb(joueur2))
                        retirer_du_cdb(cible,get_cdb(joueur2))
                        avancer_unite(position,get_cdb(joueur2))
                        placer_dans_royaume(cible,get_royaume(joueur1))
                    else :
                        position = get_position_carte(cible,get_cdb(joueur1))
                        retirer_du_cdb(cible,get_cdb(joueur1))
                        avancer_unite(position,get_cdb(joueur1))
                        placer_dans_royaume(cible,get_royaume(joueur2))

                elif get_point_de_defense(cible) <= 0 : #Cas où la cible est détruite
                    if joueur == joueur1 :
                        position = get_position_carte(cible,get_cdb(joueur2))
                        retirer_du_cdb(cible,get_cdb(joueur2))
                        avancer_unite(position,get_cdb(joueur2))
                        placer_dans_cimetiere(cible,get_cimetiere(joueur2))
                    else :
                        position = get_position_carte(cible,get_cdb(joueur1))
                        retirer_du_cdb(cible,get_cdb(joueur1))
                        avancer_unite(position,get_cdb(joueur1))
                        placer_dans_cimetiere(cible,get_cimetiere(joueur1))


                #On vérifie maintenant si la carte capturé ou tuer est le roi adverse pour savoir si la partie est fini (exécution)
                #on sort uniquement de la boucle d'attaque il faut donc refaire la vérif après ce while pour sortir de la boucle de jeu (ligne 362)
                if get_point_de_defense(cible) <= 0 and est_roi(cible) and not aEteTouche(cible):
                    partie_fini = true
                    raison_fin = "ex"
                    if joueur == joueur1 :
                        joueur_perdant = joueur2
                    else :
                        joueur_perdant = joueur1
                    break

                #On veut maintenant savoir si le joueur continue à attaquer, on stoppe la phase d'attaque si toutes les cartes du joueur sont en positions offensives
                #ou si il n'a plus de cartes pouvant attaquer
                suite = "o"
                if joueur == joueur1 :
                    attaquePossible = possibilite_attaquer(get_cdb(joueur1),get_cdb(joueur2))
                else :
                    attaquePossible = possibilite_attaquer(get_cdb(joueur2),get_cdb(joueur1))

                if not attaquePossible:
                    suite = "n"
                else :
                    suite = input("Voulez vous continuer à attaquer ? (o\/n")
                    suite_valide = False
                    if suite == "n" or suite == "o" :
                        suite_valide = True
                    while not suite_valide :
                        print("Veuillez entrer 'o' ou 'n'")
                        suite = input("Voulez vous continuer à attaquer ? (o\/n")
                        if suite == "n" or suite == "o" :
                            suite_valide = True

                if suite == "n" :
                    fin_attaque = True
            #---Fin de la boucle d'attaque si fin_attaque == true, soit le joueur ne peut plus attaquer, soit il décide d'arrêter d'attaquer

            #On remet les points de défense des cartes de l'adversaire à leur état initial
            if joueur == joueur1:
                reinitialiser_carteJoueur(joueur2)
            else :
                reinitialiser_carteJoueur(joueur1)


        #On sort de la boucle de jeu si la partie est fini (exécution)
        if partie_fini:
            break
    #---Fin de la phase d'action




    #Début de la phase de développement
        print("Début de la phase de développement")
        print(decrire_main(get_main(joueur)))

        if get_nombre_carte_main(get_main(joueur))==6 :
            print("Vous êtes obligé de faire un développement car vous possédez plus de 6 cartes en main")
            idR = int(input("Quelles cartes voulez vous envoyer dans votre royaume"))
            R = getDeck(deckGen,idR)
            while not est_dans_main(R):
                print("Cette carte n'est pas dans votre main")
                idR = int(input("Choisissez une autre carte"))
                R = getDeck(deckGen,idR)
        else :
            Y= input("Voulez vous envoyer une carte de votre main dans le royaume? (o/n)")
            input_valide = False
            if Y == "o" or Y == "n" :
                input_valide = True
            while not input_valide :
                print("Veuillez entrer 'o' ou 'n'")
                Y = input("Voulez vous envoyer une carte de votre main dans le royaume? (o/n)")
                if Y == "o" or Y == "n" :
                    input_valide = True

        if Y == "o":
            idR = int(input("Quelles cartes voulez vous envoyer dans votre royaume"))
            R = getCarte(deckGen,idR)
            while not est_dans_main(R,get_main(joueur)):
                print("Cette carte n'est pas dans votre main")
                idR = int(input("Choisissez une autre carte"))
                R = getCarte(deckGen,idR)

            placer_dans_royaume(R, get_royaume(joueur))
            retirer_de_main(R,get_main(joueur))
    #---Fin de la phase de développement

        if joueur == joueur1 :
            joueur = joueur2
        else:
            joueur = joueur1

        annonceJoueur(joueur)
    #---Fin de la boucle de jeu

    if raison_fin == "ef" :
        print("Le royaume du joueur " + str(joueur_perdant) + "s'est effondré !  Fin de la partie ! ")
    elif raison_fin == "ex" :
        print("Le roi du joueur " + str(joueur_perdant) +"est mort !  Fin de la partie ! ")
    elif raison_fin == "f":
        nb_carte_royaume_joueur1 = get_nombre_carte_royaume(get_royaume(joueur1))
        nb_carte_royaume_joueur2 = get_nombre_carte_royaume(get_royaume(joueur2))
        print("Le joueur " + joueur_sans_carte + "n'a plus de carte dans sa pioche !  Fin de la guerre ! ")
        print("Le joueur 1 possède " + nb_carte_royaume_joueur1 + " dans son royaume")
        print("Le joueur 2 possède " + nb_carte_royaume_joueur2 + " dans son royaume")
        if nb_carte_royaume_joueur1 > nb_carte_royaume_joueur2 :
            print("Le joueur 1 remporte la partie ! ")
        elif nb_carte_royaume_joueur1 < nb_carte_royaume_joueur2 :
            print("Le joueur 2 remporte la partie ! ")
        else :
            print("Egalité ! ")



main()


