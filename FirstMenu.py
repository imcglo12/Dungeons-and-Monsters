#This function will display the initial menu options

#Imports
import MenuSelection as ms

#The function
def main_menu():
    count_1 = 10
    while count_1 > 0:
        option_1 = input("\n\n Please choose an option below\n\n"\
                          "   1) Create New Character\n"\
                          "   2) Continue Game\n\n"\
                          "      >>> ")
        count_1 = ms.check_2(option_1, count_1)
        
    return option_1
