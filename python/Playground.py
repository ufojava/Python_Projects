'''
Descripton: Code testbed / playground


'''

import random


#Various ways to loop
def Player_Input():

        #Take in player input, Number and operator

        while True:

            try:
                player_number = int(input("Input a number between 1 and 99: "))

                if (player_number > 0 and player_number < 100):

                    break
            
            except:


                pass

#Player_Input()

#Produce random number between 2 numbers
def Computer_Random():


   get_Computer_Number = random.randint(1, 99)

   print(f"The Computer numner is {get_Computer_Number}")



Computer_Random()


    












   