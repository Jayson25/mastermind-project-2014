#This program neables the player to play.
#This program is brought you by Jayson Galante and Issa Nader.
import os

from initialisations import *
from tourDeJeu import *

couleur, longueur_suite, nb_essai = parametres_intitials() #launch subprogram and makes values of this subprogram useable for other purposes.

suite = iniatialisation_fonctions(couleur, longueur_suite)

essai = 1 #counter of tries.

while True:
    
    suite
    
    print("\ntry N° ", essai, ":\n")
    
    player = proposition_joueur(couleur, longueur_suite)
    count_good, count_bad = comparaison(suite, player)
    affichage_compteur(count_good, count_bad)
    print("\n")
    
    #Now we have to do the conditions in order that the game have an end.
    
    if player == suite: #end's condition for a winning game.
        
        print("\n\nYOU WON, THE RESULT WAS: " ), affichage_resutat(suite)
        
        break
        
    elif essai == nb_essai: #end's condition for a losing game.
        
        print("I'M SORRY YOU HAVE LOST, THE RESULT WAS:",  end = ' '),affichage_resutat(suite) 
        
        break
        
    essai += 1
    
   
  




