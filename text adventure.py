#textadventure
##### VARIABLES #####
##### TO DO LIST #####
#create algothrin that takes integer from p_txt str and place == ###
#make valid player variable
#add automatic scrolling
#create inventory
#add text wrap
#else statment if no answer/invalid, re asks question.

import time


def invalid_txt():
    """
    Sorry what was that? (watch your spelling)
    PLEASE START OVER
    """
pass


def g_txt():
    """
    ##########
    ###GAME###
    ##########
    """
pass

game_voice = g_txt.__doc__

def v_txt():
    """
    ##############
    ###VILLAGER###
    ##############
    """

blank = " "

npc_villager = v_txt.__doc__

error = g_txt.__doc__ + invalid_txt.__doc__

##### GAMEPLAY #####
play_game = input("WOULD YOU LIKE TO GO ON AN ADVENTURE? (yes/no)    ")
if play_game.lower().strip() == "yes":
    print (game_voice)
    hero_name = input("HERO, WHAT SHOULD WE CALL YOU?       ")

    print(blank)
    hero_home = input("WHERE ARE YOU FROM?     ")
    print(blank)
    print("THUS, THE WORLD WILL KNOW YOU AS THE GREAT HERO " + format(hero_name).upper() + " FROM " + format(hero_home).upper() + "!!!")
    print(blank)
    print("After a long journey you find yourself at the edge of a quiet town and there is a man standing near the gate.")
    print("Before you can say anything", "the stranger approaches you...")
    print (npc_villager)
    
    y_response = input("Exscuse me sir, are you the hero that we sent for? (yes/no)   ")
    if y_response.lower().strip() == "yes":
        print (npc_villager)
        print("Praise the heavens, our prayers have been answered!")
        print("Thank you", format(hero_name), "for coming to our rescue!")
        print("Ever since last harvest, children in the area keep disapeering late at night.")
        print("Can you please search the nearby area, maybe you can find some clues around town.")
        print (game_voice)
        print("PICK WHERE TO INSPECT")
        def start(): #second cycle infinetly repeats it self
           location = input("TOWNCENTER MARKET (towncenter/market)       ")
        location = input("TOWNCENTER MARKET (towncenter/market)       ")
        print(blank)
        
    elif y_response.lower().strip() == "no":
        print (game_voice)
        print("Your adventure ends, and the stranger goes home with his head down.") #printing script after this line/ end game here
        exit
        
    else:
        print(error)
        exit
        
        #####TOWNCENTER STORY LINE#####
    if location.lower().strip() == "towncenter":
        print (game_voice)
        print("YOU FIND YOURSELF, IN THE HEART OF THE CITY")
        print(blank)
        
        tc_location = input("TALK TO BEGGER - WALK AROUND (talk/walk)   ")
        if tc_location.lower().strip() == "talk":
            print (npc_villager)
            print("Exscue me out sider could you spare some coin?")
            print (game_voice)
            
            tc_action1 = input("ASK ABOUT MISSING CHILDREN  GIVE BEGGAR A COIN (talk/give)     ")
            if tc_action1.lower().strip() == "talk":
                print(blank)
                print("PLAYER: Have you heard about the children that have gone missing recently?")
                
            elif tc_action.lower().strip() == "give":
                print(blank)
                print (npc_villager)
                print(blank)
                
                beggar_action = input("Thank you so much! You don't look like you're from here. Where are you from? (truth/lie)       ")
                if beggar_action.lower().strip() == "truth":
                    print(blank)
                    print("My name is " + format(hero_name).title() + ", i'm from " + format(hero_home).title() + ".")
                    print("I was hired by the townsfolk, to investigate the missing children in the town...")
                    print(blank)
                    
                elif beggar_action.lower().strip() == "lie":
                    print(blank)
                    
                else:
                    print(error)
                    exit
                    
            else:
                print(error)
                exit
                
        elif tc_location.lower().strip() == "walk":
            print (game_voice)
            print("YOU GO FOR A WALK AROUND THE TOWN CENTER, A FEW PEOPLE WALK BY, YOU FIND NOTHING")
            
        else:
            print(error)
            
        while location :
            start()
            break
        
    else:
        print(error)
        exit

#####MARKET STORY LINE#####
    if location.lower().strip() == "market":
        print("YOU FIND YOURSELF, IN A PART OF TOWN FILLED WITH TENTS AND PEOPLE")
        print(blank)
        
        mkt_interaction = input("TALK TO VENDORS - WALK AROUND (talk/walk)   ")
        if mkt_interaction.lower().strip() == "talk":
            print(blank)
            print("YOU APPROACH THE BLACKSMITH")
            print (npc_villager)
            
            bs_interaction1 = input("Afternoon, my lord, anything I can help you with? (question/see goods)      ")
            print()
            if bs_interaction1.lower().strip() == "question":
                print(blank)
                print("PLAYER: Anything strange happening in the town?") #add player name above
                print (npc_villager)
                print("Some of the kids have been disapearing recently, maybe 2-3, but if you ask me i think they are run aways.")
                print(blank)
                
                bs_interaction2 = input("Need something else sir? (yes/no)   ")
                print(blank)
                if bs_interaction2.lower().strip() == "yes":
                    print(blank)
                    
                    bs_interaction3 = input("Would you like to see my wares? (yes/no)     ")
                    if bs_interaction3.lower().strip() == "yes":
                
                        print (npc_villager)
                        
                        bs_interaction4 = input("All I have in stock is a wooden sword... Would you like to purchase it? (yes/no)     ")
                        print(blank)
                        
                        if bs_interaction4.lower().strip() == "yes":
                            print (game_voice)
                            print("YOU HAND COINS TO THE MAN, AND A SWORD IS ADDED TO YOUR INVENTORY") # add inventory feature
                            #loop back to where would you like to go
                        elif bs_interaction4.lower().strip() == "no":
                            print(blank)
                            print("PLAYER: Thank you for all the help, have a great day!")
                            
                    elif bs_interaction3.lower().strip() == "no":
                        print(blank)
                        print("PLAYER: Thank you for all the help, have a great day!")
                        
                elif bs_interaction2.lower().strip() == "no":
                    print(blank)
                    print("PLAYER: Thank you for all the help, have a great day!")
                    
            elif bs_interaction1.lower().strip() == "see goods":
                print(blank)
                
                bs_interaction3 = input("Would you like to see my wares? (yes/no)     ")
                if bs_interaction3.lower().strip() == "yes":
                    print (npc_villager)
            
                    bs_interaction4 = input("All I have in stock is a wooden sword... Would you like to purchase it? (yes/no)     ")
                    print(blank)
                    
                    if bs_interaction4.lower().strip() == "yes":
                        print (game_voice)
                        print("YOU HAND COINS TO THE MAN, AND A SWORD IS ADDED TO YOUR INVENTORY") # add inventory feature
                        print()
                        
        elif mkt_interaction.lower().strip() == "walk":
            print (game_voice)
            print("YOU START TO WALK AROUND, YOU NOTICE SOMEONE IS FOLLOWING YOU")
            print(blank)
            
            market_action = input("KEEP WALKING OR GO TURN INTO THE ALLEY? (walk/turn)      ")
            print(blank)
            
            if market_action.lower().strip() == "walk":
                print (game_voice)
                print("YOU KEEP WALKING, AT DISTANCE CITY GUARD BEGINS TO APPROACH YOU, THE HOODED STRANGER DISAPPEARS...")
                print(blank)
                
            elif market_action.lower().strip() == "turn":
                print (game_voice)
                print("YOU TURN THE CORNER, THE HOODED MAN PULLS OUT A KNIFE.")
                print("YOU HAVE NO WEAPONS TO DEFEND YOUR SELF.")
                print("THE HOODED MAN KILLS YOU.")
                print("YOU ARE DEAD, ADVENTURE OVER")
                
            else:
                print(error)
                exit
                
        else:
            print(error)
            exit
            
else:
    print(blank)
    print("Hope you play some other time!")
    exit

    









