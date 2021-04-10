'''
Description: Game to predict if a computer will randomly present you with a higher or lower number

1. You enter a number
2. Select if computer number will be higher, lower or equal
3. Player will be given 1 goes
4. Correct Score 10
5. Incorrect score 0
6. Percent progress
7. Number correct
8. Output stats to csv which will hold the leader board

Side Note: Iwill be using a class to execute this program

'''

#Import libraries
import os
import csv

#Colour pallete
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"


#Class to include function that will produce an object for saving
class Predict:

    

    def __init__(self,firstname,lastname):

        self.firstname = firstname
        self.lastname = lastname


    def Player_Input(self):

        #Take in player input, Number and operator

        while True:

            try:
                player_number = int(input("Input a number between 1 and 99: "))

                #Check if number is between 1 and 99
                if (player_number > 0 and player_number < 100):

                    break

            except:

                pass
        
        #Select geuss option
        print(f'''

        {colour_green}1. Your number will be greater than computer?{colour_end}

        {colour_yellow}2. You number will be lower than the computer?{colour_end}
        
        ''')

        while True:

            try:
                player_guess_option = input("Input your guess option: ")

                #Check input
                if (player_guess_option == "1" or player_guess_option == "2"):

                    break
            except:

                pass
    


        #Test results
        return player_number, player_guess_option

    def Computer_Random(self):

        #Import Library
        import random


        get_computer_number = random.randint(1, 99)

        #Return the computer generated random number
        return get_computer_number


#Call Class to play game
get_player_game = Predict(input("Input your firstname: "), input("Input your lastname: "))

#Get player number and option
player_input_number_option = get_player_game.Player_Input()


#Get Computer number
computer_number = get_player_game.Computer_Random()


#Test Player Computer output

print(get_player_game.firstname, get_player_game.lastname, player_input_number_option[0],player_input_number_option[1])

print(computer_number)





