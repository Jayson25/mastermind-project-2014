#This sub program enables the player to play.
#This program is brought you by Galante Jayson and Issa Nader.

def proposition_joueur(couleur, longueur_suite):
    
    while True:
        try:
            joueur = int(input("Enter your answer: "))
            
            while joueur <= 0: #prevent null or negative input.
                print("Error, number of your input has to be higher than 0!")
                joueur = int(input("Enter your answer: "))
            
            break #stops loop if list's conditions complete (integer, starts from 1).
        
        except UnboundLocalError: # replace this errors into warning like below 
            print("Error, you can only use integers!")
    
    
    player = [int(i) for i in str(joueur)] # for splitting the proposal, convert to string first 
     
    for index, indice in enumerate(player): #analysis element element, index in a list individually
        try:
            while len(player) != longueur_suite or player[index] > couleur: #two conditions: player must respect length list and colour limit of initialisations.py 
        
                print("\nError, your answer must have the same length of the list to guess or your elements must be inside the interval of colours!")
        
                while True:
                    try:
                        joueur = int(input("Enter your answer: "))
            
                        while joueur <= 0:
                            print("\nError, number of your input has to be higher than 0!")
                            joueur = int(input("\nEnter your answer: "))
            
                        break
        
                    except(ValueError, UnboundLocalError):
                        print("\nError, you can only use integers!")
                        
                player = [int(i) for i in str(joueur)] #creates new list and prevent of getting stuck in the loop. 
                
        except IndexError: #prevents index out of range
            continue #ignore error


    return player
    
    

def comparaison(suite, player):
    #len(), used to show the length of the list into integer.
    compare = [] #list intersection of suite and player.
    
    for indice in player: #we compare an element of player if we can also find this element in suite.
    
        if indice in suite:
        
            compare.append(indice) #if the test is positive, we add the element into compare.
    
    count_good = len([index for index, indice in zip(suite, player) if index == indice])#counter for element in good place. zip() assembles elements of multiple lists in same index. Used to compare two elements in the same index.

    count_bad = len(compare) #counter for element in bad place.
    
    count_bad = count_bad - count_good 
    
    if len(set(player)) == 1:
        count_bad = 0
    
    if len(set(player)) == 2 and count_good == 2: #for example [1,1,2,2] if they are 2 good items in the exact order, two are useless.
        count_bad = 0
    
    return (count_good, count_bad)#display counters from comparison's sub-program.
    
    
 
def affichage_compteur(count_good, count_bad):
        
    print(count_good, " well placed, and ", count_bad, "bad placed")#display counters from comparison's sub-program.

        
        
def affichage_resutat(suite):

    print("".join(str(i) for i in suite)) #display only if player wins or loses game. "".join(): regroup elements from a list in a string where "" means without spaces (Only works with string).

   
