# mastermind GUI.
#This program is brought you by Jayson Galante and Issa Nader.

import pygame, sys, time
from pygame.locals import *
import pygame.mixer

pygame.init()
pygame.mixer.init() #initialisation for music and sounds.

fpsclock = pygame.time.Clock() #in order to limit processing use, we use a fps limit.

display = pygame.display.set_mode((1795, 1020), FULLSCREEN) #displays in full screen.
caption = pygame.display.set_caption("The MasterMind")

icon = pygame.image.load("master .ico").convert_alpha() #modifies the format of an image to fit the window icon.
pygame.display.set_icon(icon)#replace the old icon snake to the new one.

def jouer():  

    #this sub program enables to draw the game platform.    
        
    def plateau_de_jeu():

        #loads the sprites.
        
        global pop, close, reduce, speaker, mute, erase ,new_game, undo, test_line, green, blue, violet, yellow, red, orange, bien_place, mal_place, ng, u, tl, r ,o ,y ,g ,b ,v, cl  #global is used to have a global use of these variables in the whole MastermindGUI.
    
        plateau = pygame.image.load('fond.png')   #image for the platform. 
        button = pygame.image.load('buttons.png') #sprites for the buttons.
        color = pygame.image.load('billes.png')   #sprites for the colours to choose.
        comparateur = pygame.image.load('comparateur.png') #sprites for the result of a try by the number of well placed elements or good colour but in muddle.
        icons = pygame.image.load('icons.png')
        
        erase = plateau.subsurface(222, 813, 117, 61 ) #takes an element of the proposal board in order to blit on a colour for erase effect(procedure below).
        
        # buttons skins.
        #subsurface(): takes an element in an image.
        
        new_game = button.subsurface(379, 131, 184, 65) #new game button sprite.
        undo = button.subsurface(379, 215, 184, 65) #undo button sprite.
        test_line = button.subsurface(379,305,184,65) #test line button sprite.
    
        #icons skins
        
        close = icons.subsurface(93, 227, 45, 47)
        speaker = icons.subsurface(277, 227, 45, 47)
        mute = icons.subsurface(369, 227, 45, 47)
        pop = plateau.subsurface(1740, 950, 45, 47) # renew the zone where the blit of the speaker is in order to apply mute if the player wants to mute.
        
        #guessing colours.

        green = color.subsurface(466, 70, 79, 71) #green colour sprite.
        blue = color.subsurface(364, 70, 79, 71)  #blue colour sprite.
        violet = color.subsurface(156, 70, 79, 71) #violet colour sprite.
        yellow = color.subsurface(572, 70, 79, 71) #yellow colour sprite.
        red = color.subsurface(50, 70, 79, 71) #red colour sprite.
        orange = color.subsurface(258, 70, 79, 71) #orange colour sprite.
        
        #skin for testers

        mal_place = comparateur.subsurface(3,4,22, 22) #good placed witness sprite.
        bien_place = comparateur.subsurface(33,4,22, 22) #bad placed witness sprite.

        #displays 
    
        display.blit(plateau, (0,0)) 
    
        ng = display.blit(new_game, (1240, 305))
        u = display.blit(undo,(1240, 385))
        tl = display.blit(test_line,(1240, 469))
        r = display.blit(red,(918,920)) #we assign display as a variable in order in do in further procedure do interactions in order to choose a colour only in this zone.
        o = display.blit(orange,(1008,920))
        y = display.blit(yellow,(1098,920))
        g = display.blit(green,(1188,920))
        b = display.blit(blue,(1278,920))
        v = display.blit(violet,(1368,920))
        
        cl = display.blit(close, (1750, 0))#close button is necessary for FULLSCREEN.
        
        display.blit(speaker, (1740, 950))
        
# display procedures.

    #this procedure show number of good or / and bad placed for each end of a try.
    
    def disp_result(count_good, count_bad):
    
        good_list = [1 for i in range(count_good)] #1 represents the display for the number of good placed.
    
        bad_list = [2 for i in range(count_bad)] #2 represents the display for the number of bad placed.
    
        display_res = good_list + bad_list #makes a list of 1 and 2 (see above for their utility).
    
        for index, indice in enumerate(display_res): 
    
            if display_res[index] == 1: #display white point each times index contains 1.
            
                    display.blit(bien_place, ((981+ 35*index), ( 915 - 85 * essai)))

            if display_res[index] == 2: #display white point each times index contains 2.
            
                    display.blit(mal_place, ((981+ 35*index), ( 915 - 85 * essai)))
                    
                    
 
    # this procedure enables a number of tries in progress and can erase colours on this line that corresponds to the number of tries.
 
    def erase_colour(essai):
    
        #we describe for each tries what the program do after the player clicks on undo.
    
        if essai == 1:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 813)) #erase the colour of the element for been erased(more info in tl) .  
            
        if essai == 2:
            if len(player) > 0:
                display.blit(erase, (45 +  177 * len(player), 730))
        
        if essai == 3:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 647))
            
        if essai == 4:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 560))
            
        if essai == 5:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 478))
            
        if essai == 6:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 394))
            
        if essai == 7:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 310))
        
        if essai == 8:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 226))
            
        if essai == 9:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 142))
            
        if essai == 10:
            if len(player) > 0:
                display.blit(erase, (45 + 177 * len(player), 60))
   
#gaming procedure in order the game to be played.
    
    def play(): 
        global essai, save
        
        FPS = 30 #prevent full memory and processing eating.
        clock = pygame.time.Clock()
        
        essai = 1
        
        from initialisations import iniatialisation_fonctions        
        suite = iniatialisation_fonctions(6, 4) #like in MastermindConsole the computer random a list to guess.
        
        global player
        
        player = [] #list for player's proposition like in MastermindConsole.
        plateau_de_jeu()
        
        pygame.mixer.music.load('main2.mp3')
        pygame.mixer.music.play(-1)
        
        
        while True:

            pos = pygame.mouse.get_pos() #taking click events every time.
            
            for event in pygame.event.get():
                    
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                    if 1740+45 > pos[0] > 1740 and 950+47>pos[1]>950 : #pos[0]: x coordinate of the mouse, pos[1]: y coordinate of the mouse.
                    
                        if pygame.mixer.music.get_busy(): #if the music is playing. 
                            pygame.mixer.music.stop()
                            display.blit(pop, (1740, 950)) #removes speaker icon before applying mute icon.
                            display.blit(mute, (1740, 950)) 
                            
                        else:
                            pygame.mixer.music.play()
                            display.blit(pop, (1740, 950))
                            display.blit(speaker, (1740, 950))
                            
                    if cl.collidepoint(pos):
                        pygame.quit()
                        sys.exit()

                    if r.collidepoint(pos): #if player clicks on red.
                        player.append(1)    
                        
                    if o.collidepoint(pos): #if player clicks on orange.
                        player.append(2)    
                        
                    if y.collidepoint(pos): #if player clicks on yellow.
                        player.append(3)    
                        
                    if g.collidepoint(pos): #if player clicks on green.

                        player.append(4)   
                        
                    if b.collidepoint(pos): #if player clicks on blue.
                        player.append(5)    
                        
                    if v.collidepoint(pos): #if player clicks on violet.
                        player.append(6)   
 
                    if tl.collidepoint(pos):
                        
                        if len(player) == 4 and player != suite: #condition to prevent unfinished list in the test. 
                            
                            from tourDeJeu import comparaison 
                            count_good, count_bad = comparaison(suite, player)
                            
                            disp_result(count_good, count_bad)
                           
                            del player[:] #clears elements inside player.
                            
                            essai += 1 #progress of tries.
                            
                        if essai > 10:
                        
                            resultat()
                            
                            lose_sound = pygame.mixer.Sound('loser.wav') #loser's sound.
                            lose_sound.play()
                            
                            lose = pygame.image.load('lose.png') #blit sprite of a losing game.
                            display.blit(lose, (1250, 550))
                            
                            pygame.mixer.music.stop() #stops the background music.
                            
                        if suite == player:
                        
                            resultat()
                            
                            win_sound1 = pygame.mixer.Sound('win1.wav') #winner's sound effect.
                            win_sound1.play()
                            
                            win = pygame.image.load('win.png') #blit sprite of a wining game.
                            display.blit(win, (1250, 480))
                            
                            win_sound2 = pygame.mixer.Sound('win2.wav') #fireworks' sound effect.
                            win_sound2.play()
                            
                            pygame.mixer.music.stop()
                        
                    if u.collidepoint(pos): #if player clicks on undo.
                        if player != suite or essai <= 10: #for aesthetic problem.
                            erase_colour(essai)
                            try:
                                del player[-1] #we erase the last element of the list.
                
                            except IndexError:
                                pass
            
                    if ng.collidepoint(pos):
                        jouer() #restart the sub program
                   
            
            if len(player) <= 4 and essai <= 10:  #condition for the display of the player's grid display.      
                for index, indice in enumerate(player):
                    try:
                        if player[index] == 1:
                            display.blit(red, ((230 + 180*index), (891 - 84 * essai))) #displays red on the board if player clicks on red.
                
                        elif player[index] == 2:
                            display.blit(orange, ((230 + 180*index), (891 - 84 * essai))) #displays orange on the board if player clicks on orange.
                
                        elif player[index] == 3:
                            display.blit(yellow, ((230 + 180*index), (891 - 84 * essai))) #displays yellow on the board if player clicks on yellow.
                
                        elif player[index] == 4:
                            display.blit(green, ((230 + 180*index), (891 - 84 * essai))) #displays green on the board if player clicks on green.
                
                        elif player[index] == 5:
                            display.blit(blue, ((230 + 180*index), (891 - 84 * essai))) #displays blue on the board if player clicks on blue.
                
                        elif player[index] == 6:
                            display.blit(violet, ((230 + 180*index), (891 - 84 * essai))) #displays violet on the board if player clicks on violet.
                
                    except IndexError:
                        pass
            
            
            def resultat(): #whether the play wins or loses, the game displays the solution of the game.
                for index, indice in enumerate(suite):
        
                    if suite[index] == 1:
                        display.blit(red, ((448 + 110*index), (925)))
                
                    elif suite[index] == 2:
                        display.blit(orange, ((448 + 110*index), (925)))
                    
                    elif suite[index] == 3:
                        display.blit(yellow, ((448 + 110*index), (925)))
                
                    elif suite[index] == 4:
                        display.blit(green, ((448 + 110*index), (925)))
                
                    elif suite[index] == 5:
                        display.blit(blue, ((448 + 110*index), (925)))
                
                    elif suite[index] == 6:
                        display.blit(violet, ((448 + 110*index), (925)))
                
            if len(player) > 4: #prevents the player's list to be out of the limit.
                del player[4] 
                
            pygame.display.update() #refresh the game.    
            clock.tick(FPS) #see above
                        
    play() # activates the sub program.          

            
        
        
        
def menu():

    def effex(): #unlike the different structure of the game above, we can use this procedure for button effects.
    
        pos = pygame.mouse.get_pos() #gets the cursor's position.
        
        if pygame.mouse.get_pressed(): #used whether button clicks or not, any buttons on the mouse, as long as the position is on the target below, a condition will complete the effects(see below). 
        
            if q.collidepoint(pos):
                    display.blit(quit_button, (1003,651))
                    
            if p.collidepoint(pos):
                    display.blit(play_button, (245,651))
                    
    while True: #same conditions as the game for the menu but only the display of the menu has a different code structure. In fact, it is inside the loop instead of before the loop because of the effect we want to do and it doesn't occurs technical difficulties because of the absence of new blit.
    
        menu = pygame.image.load('menu.png')
        boutons = pygame.image.load('menu_but.png')
        
        play_button = boutons.subsurface(248, 35, 506, 155)
        quit_button = boutons.subsurface(248, 247, 506, 155)
        
        display.blit(menu, (0,0))   
        
        p = display.blit(play_button, (245,651))
        q = display.blit(quit_button, (1003,651)) 
        
        effex()
        
        for event in pygame.event.get():
          
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
                pos = pygame.mouse.get_pos()
                
                if q.collidepoint(pos): #quit the game.
                    pygame.quit()
                    sys.exit()
                    
                if p.collidepoint(pos): #play the game.
                    return jouer() #closes the menu and open the game sub-program.
                    
        pygame.display.update()  

        
    
menu()