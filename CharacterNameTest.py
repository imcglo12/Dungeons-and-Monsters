#This is to test to see if a character name is already in use.
#If it is, it will prompt as to whether or not to replace the name
#    and therefore the file

#Import needed libraries
import MenuSelection as ms
import os.path
import CharacterStats as cs
import CharacterClasses as ccs

#the function
def char_name(character_name, count):
                
    #If the name already exists
    if character_name.lower() == 'back':
        count = 999
        
    elif count != 999:
        if os.path.exists("Characters/" + character_name):
            while count > 0:
                option = input("\n\n This character already exists. Would you like to replace?\n\n"\
                               "   1) Yes\n"\
                               "   2) No\n\n"\
                               "      >>> ")
                count = ms.check_2(option, count)

                if count == 999:
                    break
            
            if count == 999:
                pass
                
            #if player wants to replace the character
            elif int(option) == 1:
                count_2 = 10
                while count_2 > 0:

                    option_2 = input("\n\n ARE YOU SURE YOU WANT TO REPLACE THIS CHARACTER?\n"\
                                   "   1) YES\n"\
                                   "   2) NO\n\n"\
                                   "      >>> ")
                    count_2 = ms.check_2(option_2, count_2)

                    if count_2 == 999:
                        count = 999
                        break

                    elif count_2 == 0:
                        count = 1
                
                if count_2 == 999:
                    count = 999
                    pass
                    
                #if player is absolutely sure they want to delete the character    
                elif int(option_2) == 1:
                    f = open(os.path.abspath("Characters/" + character_name), 'w')
                    ccs.new_char(character_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, character_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0,0)
                    f.close()
    
                #if player says "NO"    
                elif int(option_2) == 2:
                    count = 0
    
            #If player does not wish to replace the character    
            elif int(option) == 2:
                count = 0
                
        #If the name doesn't exist
        else:
            #update the "created_games" file
            cg = open("created_games", "a")
            cg.write(character_name + "\n")
            cg.close()
            #create a new file by the name of the character
            f = open(os.path.abspath("Characters/" + character_name), 'w')
            f.write("Name: %s" % (character_name))
            f.close()
            count = 1
            
    return count
        
