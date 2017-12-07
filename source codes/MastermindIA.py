#This program is brought you by Galante Jayson and Issa Nader.

#this sub program is a function.

#this loop is for the player to choose which suite the IA has to guess.

print("choose a list where the IA has to guess!")

from tourDeJeu import proposition_joueur
player = proposition_joueur(6, 4)
            
#This sub program is the algorithm of Minimax that choose the most appropriate list and less risky.  
def choisirIA(S, possibles, résultats, essai): #this sub program still doesn't work because of the misunderstanding of the mini project's guide written by the full professor.
    

    if essai == 1:
        return c
    
    else:
    
        for index, res in enumerate(résultats):
            min(résultats)
        
        for index, x in enumerate(possibles):
            max(tuple(possibles))
          
        if essai ==1:
            S.remove((1,1,2,2))
                    
        else:     
            S.remove(c)
        
        
        
def procedure():
    global c
    essai = 1 #initiate the first try.
    S = []
    possibles = []
    résultats = []

    #first let's start to create t-uples for possible colours inside.

    for element1 in range(1,7):# first element of the t-uple.
        for element2 in range(1,7):# second element of the t-uple.
            for element3 in range(1,7):# third element of the t-uple.
                for element4 in range(1,7):# fourth element of the t-uple.
                    S.append((element1, element2, element3, element4))# assemble the four elements in order.

    possibles = S #initiate immutable list.

    for good in range(1,5): #same structure as above.
        for bad in range(1,5):
            résultats.append((good, bad))
      
    while True:
        print("\nessai N°: ", essai)
        
        if essai == 1:
            c = [1,1,2,2]
            
        if essai > 1:
            import random
            c = list(random.choice(S)) #choose randomly a element inside S.
        
        from tourDeJeu import comparaison #we will reuse the comparison from the player game. 
        count_good, count_bad = comparaison(player, c)#We will compare the IA proposition to the list to guess.
        
        compare = (count_good, count_bad) #normaly compare would become a element res in résultats but we didn't achieve this goal.
        
        print("".join(str(i) for i in c))
        
        if c == player:
            print("this IA did it!\nthe result was:", end=' '), player
            break
            
        essai += 1
procedure()