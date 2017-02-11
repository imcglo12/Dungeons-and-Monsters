#This is the continuation of the character creating process
#Player will select race, class, and "roll" for attributes:
# Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma

#Imported Libraries
import MenuSelection as ms
import os.path

#function to select race
def race(character_name):
    char_file = open(os.path.abspath("Characters/" + character_name), 'a')
    count = 10
    print("\n\n Choosing your race is important since it will enable you to use some")
    print("abilities but also disable others. Human's are the most balanced")
    print("of all of the races")
    while count > 0:
        sel = input("\n What race would you like to be?\n\n"\
                     "   1) Human\n"\
                     "   2) Elf\n\n"\
                     "      >>> ")
        
        count = ms.check_2(sel, count)
        race = ''
        if count == 0:
            if int(sel) == 1:
                race = "Human"
            if int(sel) == 2:
                race = "Elf"
                
            char_file.write("\nRace: %s" % (race))
            char_file.close()

        else:
            break
        
    return race


#Function to select class
def class_sel(race, character_name):
    char_file = open(os.path.abspath("Characters/" + character_name), 'a')
    count = 10
    print("\n\n Classes is basically the specialization of any character.")
    print("Each class also requires a minimum number of stat points.")
    print("(e.g. Paladins require high charisma, Rogues require high")
    print("dexterity)")
    while count > 0:
        sel = input("\n What class would you like your %s to be?\n\n"\
                     "   1) Paladin\n"\
                     "   2) Rogue\n\n"\
                     "      >>> " % (race))
        
        count = ms.check_2(sel, count)

        if count == 0:
            if int(sel) == 1:
                class_sel = "Paladin"
            if int(sel) == 2:
                class_sel = "Rogue"
                
            char_file.write("\nClass: %s" % (class_sel))
            char_file.close()
        else:
            break
    return

    
