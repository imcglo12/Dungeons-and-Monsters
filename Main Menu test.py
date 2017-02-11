#The Main Menu and/or Main Program that will call the other programs as needed

#Here's a space for loading needed libraries and programs
import RandomDiceNumbers as rdn
import CharacterCreation as cc
import MenuSelection as ms
import os.path
import CharacterNameTest as cnt
import FirstMenu as fm
import CharacterClasses as ccs
import CharacterStats as cs

#files to open
cg = open("created_games", 'r+')


#Welcome screen
print(" Welcome to the exciting world of...\n")
print(" |=========================================================|")
print(" ||=======================================================||")
print(" ||                                                       ||")
print(" || DDDD   U  U  N   N   GGGG  EEEEE   OOO   N   N   SSS  ||")
print(" || D   D  U  U  NN  N  G      E      O   O  NN  N  S     ||")
print(" || D   D  U  U  N N N  G  GG  EEEE   O   O  N N N   SSS  ||")
print(" || D   D  U  U  N  NN  G  GG  E      O   O  N  NN      S ||")
print(" || DDDD   UUUU  N   N   GG G  EEEEE   OOO   N   N   SSS  ||")
print(" ||                                                       ||")
print(" ||=======================================================||")
print(" |=========================================================|")



#The main program
counter = 10
while counter > 0:
    option_1 = fm.main_menu()

    #naming the new character
    count_2 = 10
    while count_2 > 0:
        if int(option_1) == 1:
            print("\n\n What would you like to name your new character?")
            character_name = input(" (Type 'back' to return to the main screen)\n\n"\
                                   "      >>> ")
            
            #testing to see if the character name and file already exist
            count_2 = cnt.char_name(character_name, count_2)
            
        #forces break if player types 'back'
        if count_2 == 999:
            break

        elif count_2 == 0:
            break

        #Character creating process
        elif count_2 == 1:
            race = cc.race(character_name) #choosing race
            if race == '':
                break
            else:
                cc.class_sel(race, character_name) #choosing class

                

        #If option_1 == 2, we will look for saved files and continue
        #where the player left off.
        if int(option_1) == 2:
            content = []
            for lines in cg.readlines():
                content.append(lines)
            for i in content:
                print ("   " + i.strip())
                cg.close()  #just closing it for now until I can do things with it later
                            #will need to do some file reading here to get all of the
                            #characters information
            count_2 = 0
    

    
