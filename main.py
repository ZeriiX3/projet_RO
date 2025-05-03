# Project Théorie des Graphes: Ordonnancement
# Professeur: Noureddine BENTHAMI
# Mars 2025

# Par Bastien Peltier, Nathan Pégé, Sébastien XU, Maxence Durand, Matthieu BACHELERIE

# Import
from fonction import *
import copy
import os

"""
if not os.path.exists("trace"):
    os.makedirs("trace")"""


def main():

    start = True
    while start != False:

        print_blue("\n===== Recherche Opérationnelle =====")

        # Affichage utilisateur
        num = choix_tableau()

        if num == False:
            start = False
            print_blue("\nMerci de votre utilisation, à bientôt !")

        else:
            # Lecture des fichiers txt
            n, tabC, tabD = lire_proposition(f'graphe/flot {num}.txt')
            afficher_proposition(n, tabC, tabD)


            # Vérifie si c'est un graphe d'ordonnancement valide


            op = True
            while op != False:

                # Demande à l'utilisateur l'action qu'il veut effectuer
                choice = choix_action(num)
                if choice == False:
                    op = False
                else :
                #Affichage selon les choix
                    if choice == 1:
                        print("ACTION1")
                    if choice == 2:
                        print("ACTION1")
                    if choice == 3:
                        print("ACTION1")
                    if choice == 4:
                        print("ACTION1")
                    if choice == 5:
                        print("ACTION1")

            else:
                print_red("\nLe graphe ne respecte pas les propriétés nécessaires.")
                print_light_green("Veuillez choisir un autre tableau de contraintes.")

# Lancement du programme
main()
