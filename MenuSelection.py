def check_1(option, count):
    #See if they typed 'back'
    if option.lower() == "back":
        count = 999

    elif option == '1':
        option = int(option)
        count = 0

    #Check for incorrect selections
    elif option.isalpha() or int(option) < 0 or int(option) > 1:
        print ("\n     You must select an option using a numeric")
        count -= 1
        if count == 0:
            print ("\n     I'm sorry, you've made too many attempts. You are now exiting the game.")
    else:
        count = 0

    return count


def check_2(option, count):
    #See if they typed 'back'
    if option.lower() == "back":
        count = 999

    elif option == '1':
        option = int(option)
        count = 0
    elif option == '2':
        option = int(option)
        count = 0
    elif option == '\r':
        count = 0

    #Check for incorrect selections
    elif option.isalpha() or int(option) < 0 or int(option) > 2:
        print ("\n     You must select an option using a numeric")
        count -= 1
        if count == 0:
            print ("\n     I'm sorry, you've made too many attempts. You are now exiting the game.")
    else:
        count = 0

    return count


def check_3(option, count):
    #See if they typed 'back'
    if option.lower() == "back":
        count = 999

    elif option == '1':
        option = int(option)
        count = 0
    elif option == '2':
        option = int(option)
        count = 0
    elif option == '3':
        option = int(option)
        count = 0

    #Check for incorrect selections
    elif option.isalpha() or int(option) < 0 or int(option) > 3:
        print ("\n     You must select an option using a numeric")
        count -= 1
        if count == 0:
            print ("\n     I'm sorry, you've made too many attempts. You are now exiting the game.")
    else:
        count = 0

    return count
