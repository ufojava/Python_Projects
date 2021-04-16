'''
Description: Game to predict if a computer will randomly present you with a higher or lower number

1. You enter a number
2. Select if computer number will be higher, lower or equal
3. Player will be given 1 goes
4. Correct Score 10
5. Incorrect score 0
6. Percent progress
7. Create obeject with class to collect all the inormation
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

#Variable
player_scores = []
play_count = 10


#Class to include function that will produce an object for saving
class Predict:

    os.system("clear")
    print(f'''

    ***** THE PREDICT GAME *****

    The Goal!!!! Can you guess if the computer's number will be higher or lower than your number
    
    ''')

    def __init__(self,firstname,lastname):

        self.firstname = firstname
        self.lastname = lastname


    def Game_Play(self):

        #Import library
        import random

        #Variable
        maximum_play_count = 3
        get_firstname = self.firstname
        get_lastname = self.lastname

        #Guess input controls
        guess_number_count = 0
        guess_number_description = [f"{self.firstname}, this is your first guess",f"{self.firstname}, this is your second guess",f"{self.firstname}, this is your third guess"]

        #Variables
        player_correct_guess = 0
        percentage_correct = 0

        #Take in player input, Number and operator

        
            
            
        for play_number in range(maximum_play_count):

            while True:
                
                os.system("clear")
                print("Time to input your number !!! ")
                print()
                

                try:

                    player_number = int(input(f"{self.firstname} input a number between 1 and 3: "))

                    #Check if number is between 1 and 99
                    if (player_number > 0 and player_number < 4):

                        break

                except:

                    pass
            
            #Select geuss option
            print(f'''

            {guess_number_description[guess_number_count]}

            {colour_green}1. Computer number will be greater than your number?{colour_end}

            {colour_yellow}2. Computer number will be lower than your number?{colour_end}

            {colour_blue}3. Computer number will be equal to your number?{colour_end}
            
            ''')

            while True:

                try:
                    player_guess_option = input(f"{self.firstname} input your guess option: ")

                    #Check input
                    if (player_guess_option == "1" or player_guess_option == "2" or player_guess_option == "3"):

                        guess_number_count += 1

                        break
                except:

                    pass
            
            #Get random computer number
            get_computer_number = random.randint(1, 3)


            #******** COMPARE COMPUTER / PLAYER NUMBER SECTION ***********


            #Define prediction 
            predict_greater = (get_computer_number > player_number)
            predict_equals = (get_computer_number == player_number)
            predict_lower = (get_computer_number < player_number)

            #Return messages
            higher_message = f"{self.firstname}, you have guessed correctly - HIGHER. Computer: {get_computer_number} Your number: {player_number}"
            equal_message = f"{self.firstname}, you have predicted correctly - EQUAL. Computer: {get_computer_number} Your number: {player_number}"
            lower_message = f"{self.firstname}, you have predicted correctly - LOWER Computer: {get_computer_number} Your number: {player_number}"
            incorrect_guess_message = f"Sorry {self.firstname}, you have guessed incorrectly Computer: {get_computer_number} Your number: {player_number}"


            #Check guess option
            if (player_guess_option == "1" and predict_greater):

                #Add 1 to player score
                player_correct_guess += 1

                #Calculate percentage correct
                percentage_correct = int(player_correct_guess / maximum_play_count * 100)

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{colour_green}{higher_message}{colour_end}. {colour_yellow}{percentage_correct}% Correct{colour_end}")
                print()
                input("Press Enter key to continue ...")
            
            elif (player_guess_option == "2" and predict_lower):

                #Add 1 to player score
                player_correct_guess += 1

                #Calculate percentage correct
                percentage_correct = int(player_correct_guess / maximum_play_count * 100)

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{colour_green}{lower_message}{colour_end}. {colour_yellow}{percentage_correct}% Correct{colour_end}")
                print()
                input("Press Enter key to continue ...")

            elif (player_guess_option == "3" and predict_equals):

                #Add 1 to player score
                player_correct_guess += 1

                #Calculate percentage correct
                percentage_correct = int(player_correct_guess / maximum_play_count * 100)

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{colour_green}{equal_message}{colour_green}. {colour_yellow}{percentage_correct}% Correct{colour_end}")
                print()
                input("Press Enter key to continue ...")

            else:

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{colour_red}{incorrect_guess_message}{colour_end}. {colour_yellow}{percentage_correct}% Correct{colour_end}")
                print()
                input("Press any key to continue ...")

        #End of the Play For Loop

        return get_firstname,get_lastname,player_correct_guess,percentage_correct




    


#Call Class to play game
get_player_game = Predict(input("Input your firstname: ").capitalize(), input("Input your lastname: ").capitalize())


#Get the player attributes from game play
get_play_attributes = get_player_game.Game_Play()




#Collect all the data for record history
class Collect_Player_Scores:

    def __init__(self,in_firstname,in_lastname,correct_guess_count):

        self.in_firstname = in_firstname
        self.in_lastname = in_lastname
        self.correct_guess_count = correct_guess_count

    def Work_Results(self):


        #Variables
        get_correct_guess_count = self.correct_guess_count
        maximum_play = 10
        correct_score = 10
        incorrect_score = 0


#Print attributes     
print(get_play_attributes[0],get_play_attributes[1],get_play_attributes[2],get_play_attributes[3])
        

