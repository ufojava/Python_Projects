'''
Synopsis: This is where I will perform unit testing



'''

#Test menu system

picked_menu_option = 0

import os

def Lotto_Menu():

    os.system("clear") #Clear screen
    menu_option = int(input('''

    ******* Weekly Lotto Menu *********

    1. Pick Lotto Numbers

    2. Lucky Dip

    : '''
    ))

    if (menu_option == 1):
        
        return 1 #This option is for manaully picked number
    
    elif (menu_option == 2):
        
        return 2 #This option is for the lucky dip

    else:
        print("Invalid selection !!!")
        return 0 #Invalid selection

picked_menu_option = Lotto_Menu()

print(picked_menu_option)

#Print horizontal

my_horizontal_list = ["Ovie","Ufuoma","Igho","Bami","Tobo","Dafe","Jero"]


print('''
The results .....


''')

print(" " . join(my_horizontal_list))



