#This will be for creating new characters

#imports
import os.path


    
class NewCharacter(object):

    def __init__(
             self, c_p, s_p, e_p, g_p, p_p,\
             paralyzation_poison_death_magic,\
             rod_staff_wand,\
             petrification_polymorph,\
             breath_weapon, spell,\
             body_armor, head_gear, shield,\
             character_name, char_class, age, sex,\
             height, weight, hair, eyes, skin,\
             hit_points, experience, max_press,\
             open_doors, bend_bars__lift_gates,\
             surprise, system_shock, max_henchman,\
             loyalty_base, reaction_adjustment,\
             death_max, deaths_to_date, resurrection_survival,\
             strength, dexterity, constitution, inteligence,\
             wisdom, charisma, armor_class_base, armor_class
             ):

             self.c_p = c_p
             self.s_p = s_p
             self.e_p = e_p
             self.g_p = g_p
             self.p_p = p_p
             self.paralyzation_poison_death_magic = paralyzation_poison_death_magic
             self.rod_staff_wand = rod_staff_wand
             self.petrification_polymorph = petrification_polymorph
             self.breath_weapon = breath_weapon
             self.spell = spell
             self.body_armor = body_armor
             self.head_gear = head_gear
             self.shield = shield
             self.character_name = character_name
             self.char_class = char_class
             self.age = age
             self.sex = sex
             self.height = height
             self.weight = weight
             self.hair = hair
             self.eyes = eyes
             self.skin = skin
             self.hit_points = hit_points
             self.experience = experience
             self.max_press = max_press
             self.open_doors = open_doors
             self.bend_bars__lift_gates = bend_bars__lift_gates
             self.surprise = surprise
             self.system_shock = system_shock
             self.max_henchman = max_henchman
             self.loyalty_base = loyalty_base
             self.reaction_adjustment = reaction_adjustment
             self.death_max = death_max
             self.deaths_to_date = deaths_to_date
             self.resurrection_survival = resurrection_survival
             self.strength = strength
             self.dexterity = dexterity
             self.constitution = constitution
             self.inteligence = inteligence
             self.wisdom = wisdom
             self.charisma = charisma
             self.armor_class_base = armor_class_base
             self.armor_class = armor_class
    
        
    def coins(self):
        
        coins = {
                    "c.p.": 0,
                     "s.p.": 0,
                     "e.p.": 0,
                     "g.p.": 0,
                     "p.p.": 0,
                     }
        
        coins['c.p.'] = self.c_p
        coins['s.p.'] = self.s_p
        coins['e.p.'] = self.e_p
        coins['g.p.'] = self.g_p
        coins['p.p.'] = self.p_p

        f = open(os.path.abspath("Characters/" + self.character_name), 'a')
        f.write("\n")
        for key in coins:
            f.write(key + ": " + str(coins[key]) + "\n")
        f.write("\n")
        f.close()

        return
    

    def saving_throws(self):
    
        saving_throws = {
                             "Paralyzation/Poison/Death Magic": 0,
                             "Rod/Staff/Wand": 0,
                             "Petrification/Polymorph": 0,
                             "Breath Weapon": 0,
                             "Spell": 0,
                             }

        saving_throws["Paralyzation/Poison/Death Magic"] = self.paralyzation_poison_death_magic
        saving_throws["Rod/Staff/Wand"] = self.rod_staff_wand
        saving_throws["Petrification/Polymorph"] = self.petrification_polymorph
        saving_throws["Breath Weapon"] = self.breath_weapon
        saving_throws["Spell"] = self.spell
        
        f = open(os.path.abspath("Characters/" + self.character_name), 'a')
        f.write("\n")
        for key in saving_throws:
            f.write(key + ": " + str(saving_throws[key]) + "\n")
        f.write("\n")
        f.close()
        
        return
    

    def armor_worn(self):
        
        armor_worn = {
                            "Body Armor": '',
                            "Head Gear": '',
                            "Shield": '',                    
                            }

        armor_worn["Body Armor"] = self.body_armor
        armor_worn["Head Gear"] = self.head_gear
        armor_worn["Shield"] = self.shield
        
        f = open(os.path.abspath("Characters/" + self.character_name), 'a')
        f.write("\n")
        for key in armor_worn:
            f.write(key + ": " + str(armor_worn[key]) + "\n")
        f.write("\n")
        f.close()
        
        return


    def char_personal(self):
        
        char_personal = {
                                "Character Name": '',
                                "Class": '',
                                "Age": 0,
                                "Sex": '',
                                "Height": '',
                                "Weight": 0,
                                "Hair": '',
                                "Eyes": '',
                                "Skin": '',
                                "Hit Points": 0,
                                "Experience": 0
                                }

        char_personal["Character Name"] = self.character_name
        char_personal["Class"] = self.char_class
        char_personal["Age"] = self.age
        char_personal["Sex"] = self.sex
        char_personal["Height"] = self.height
        char_personal["Weight"] = self.weight
        char_personal["Hair"] = self.hair
        char_personal["Eyes"] = self.eyes
        char_personal["Skin"] = self.skin
        char_personal["Hit Points"] = self.hit_points
        char_personal["Experience"] = self.experience
        
        f = open(os.path.abspath("Characters/" + self.character_name), 'a')
        f.write("\n")
        for key in char_personal:
            f.write(key + ": " + str(char_personal[key]) + "\n")
        f.write("\n")
        f.close()
        
        return

    
    def char_misc(self):
        
        char_misc = {
                                "Max Press": 0,
                                "Open Doors": 0,
                                "Bend Bars/Lift Gates": 0,
                                "Surprise": 0,
                                "System Shock": 0,
                                "Max # Henchman": 0,
                                "Loyalty Base": 0,
                                "Reaction Adjustment": 0,
                                "DEATH Max #": 0,
                                "Deaths to date": 0,
                                "Resurrection Survival": 0
                                }

        char_misc["Max Press"] = self.max_press
        char_misc["Open Doors"] = self.open_doors
        char_misc["Bend Bars/Lift Gates"] = self.bend_bars__lift_gates
        char_misc["Surprise"] = self.surprise
        char_misc["System Shock"] = self.system_shock
        char_misc["Max # Henchman"] = self.max_henchman
        char_misc["Loyalty Base"] = self.loyalty_base
        char_misc["Reaction Adjustment"] = self.reaction_adjustment
        char_misc["DEATH Max #"] = self.death_max
        char_misc["Deaths to date"] = self.deaths_to_date
        char_misc["Resurrection Survival"] = self.resurrection_survival
        
        f = open(os.path.abspath("Characters/" + self.character_name), 'a')
        f.write("\n")
        for key in char_misc:
            f.write(key + ": " + str(char_misc[key]) + "\n")
        f.write("\n")
        f.close()
        
        return


    def char_stats(self):
        
        char_stats = {
                                "Strength": 0,
                                "Dexterity": 0,
                                "Constitution": 0,
                                "Inteligence": 0,
                                "Wisdom": 0,
                                "Charisma": 0,
                               "Armor Class Base": 0,
                               "Armor Class": 0
                             }

        char_stats["Strength"] = self.strength
        char_stats["Dexterity"] = self.dexterity
        char_stats["Constitution"] = self.constitution
        char_stats["Inteligence"] = self.inteligence
        char_stats["Wisdom"] = self.wisdom
        char_stats["Charisma"] = self.charisma
        char_stats["Armor Class Base"] = self.armor_class_base
        char_stats["Armor Class"] = self.armor_class
        
        f = open(os.path.abspath("Characters/" + self.character_name), 'a')
        f.write("\n")
        for key in char_stats:
            f.write(key + ": " + str(char_stats[key]) + "\n")
        f.write("\n")
        f.close()
        
        return






    


def new_char(char_name, c_p, s_p, e_p, g_p, p_p,\
             paralyzation_poison_death_magic,\
             rod_staff_wand,\
             petrification_polymorph,\
             breath_weapon, spell,\
             body_armor, head_gear, shield,\
             character_name, char_class, age, sex,\
             height, weight, hair, eyes, skin,\
             hit_points, experience, max_press,\
             open_doors, bend_bars__lift_gates,\
             surprise, system_shock, max_henchman,\
             loyalty_base, reaction_adjustment,\
             death_max, deaths_to_date, resurrection_survival,\
             strength, dexterity, constitution, inteligence,\
             wisdom, charisma, armor_class_base, armor_class):

    
    char_name = NewCharacter(
             c_p, s_p, e_p, g_p, p_p,\
             paralyzation_poison_death_magic,\
             rod_staff_wand,\
             petrification_polymorph,\
             breath_weapon, spell,\
             body_armor, head_gear, shield,\
             character_name, char_class, age, sex,\
             height, weight, hair, eyes, skin,\
             hit_points, experience, max_press,\
             open_doors, bend_bars__lift_gates,\
             surprise, system_shock, max_henchman,\
             loyalty_base, reaction_adjustment,\
             death_max, deaths_to_date, resurrection_survival,\
             strength, dexterity, constitution, inteligence,\
             wisdom, charisma, armor_class_base, armor_class)

    char_name.char_personal()
    char_name.armor_worn()
    char_name.saving_throws()
    char_name.coins()
    char_name.char_misc()
    char_name.char_stats()
    
    
    return
