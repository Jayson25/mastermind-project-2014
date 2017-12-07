#this prgram is used to initiate the game by using sub-programs.
#This program is brought you by Jayson Galante and Nader Issa.
#First, let's create a program that can make a function of parameters for conditions of the game chosen by the user.
def parametres_intitials():
 
 #for colour:
 
    while True:
            
        try:
    
            couleur = int(input("Choose the number of colours: ")) #prevent null and negative input.
            
            while couleur <= 0: # prevent negative input.
                print("Error, number of your input has to be higher than 0!")
                couleur = int(input("Choose the number of colours: "))
                
            while couleur > 9: #prevent conflict with length and colour because list making has for element maximum 9.
                print("Error, number of your input has to be lower or equal than 9!")
                couleur = int(input("Choose the number of colours: "))
                
            break #stops loop if list's conditions complete (integer, starts from 1).
            
        except ValueError: # replace this error into warning like below *.    
            print("Error, you can only use integers!")
            
# for list's length.
        
    while True:
        try: 
            longueur_suite = int(input("\nChoose the length of the list to guess: "))
            
            while longueur_suite <= 0:          
                print("Error, number of your input has to be higher than 0!")
                longueur_suite = int(input("Choose the length of the list to guess!"))
                
            break
        except ValueError:
            print("Error, you can only use integers!")
    
#for maximum tries.
        
    while True: 
        try:           
            nb_essai = int(input("\nNumber of tries: "))
                
            while nb_essai <= 0:          
                print("Error, number of your input has to be higher than 0!")
                nb_essai = int(input("Number of tries: "))
                 
            break
        except ValueError:
            print("Error, you can only use integers!")
    
            
    return (couleur, longueur_suite, nb_essai)
    
    
    
def iniatialisation_fonctions(couleur, longueur_suite):
    
    from random import randint # import randint function.
    
    suite = [randint(1,couleur) for i in range(longueur_suite)] #creates a list to guess with randint.
    return suite
    





    
    
    


  
    
    


