'''
Description: Game to predict if a computer will randomly present you with a higher or lower number

1. You enter a number
2. Select if computer number will be higher, lower or equal
3. Player will be given 1 goes
4. Correct Score 10
5. Incorrect score 0
6. Percent progress
7. Computer player score
8. Create loop for player to play again
9. Output stats to csv which will hold the leader board
10. Get highest score players

Side Note: I will be using a class to execute this program

'''

#Import libraries
import os
import csv
import datetime
import sys
import pandas as pd


#Colour pallete
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"
colour_beige = "\33[36m"
colour_violet = "\033[35m"

#Background Colours
colour_violet_bg = "\33[45m"
colour_blue_bg = "\33[44m"

#Variable
play_count = 10


#Class to include function that will produce an object for saving
class Predict:

    os.system("clear")
    

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
        player_score = 0

        #Take in player input, Number and operator

        
            
            
        for play_number in range(maximum_play_count):

            while True:
                
                os.system("clear")
                print(f"{colour_blue_bg}Time to input your number !!!{colour_end}")
                print()
                

                try:

                    player_number = int(input(f"{self.firstname} input a number between {colour_yellow}1{colour_end} and {colour_yellow}3{colour_end}: "))

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
                    player_guess_option = input(f"{colour_blue_bg}{self.firstname}{colour_end} input your guess option: ")

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
            higher_message = f"{self.firstname}, you have guessed {colour_yellow}correctly{colour_end} - {colour_yellow}HIGHER{colour_end}. Computer: {colour_yellow}{get_computer_number}{colour_end} Your number: {colour_yellow}{player_number}{colour_end}"
            equal_message = f"{self.firstname}, you have predicted {colour_yellow}correctly{colour_end} - {colour_yellow}EQUAL{colour_end}. Computer: {colour_yellow}{get_computer_number}{colour_end} Your number: {colour_yellow}{player_number}{colour_end}"
            lower_message = f"{self.firstname}, you have predicted {colour_yellow}correctly{colour_end} - {colour_yellow}LOWER{colour_end} Computer: {colour_yellow}{get_computer_number}{colour_end} Your number: {colour_yellow}{player_number}{colour_end}"
            incorrect_guess_message = f"Sorry {self.firstname}, {colour_red}you have guessed{colour_end} {colour_yellow}incorrectly{colour_end} Computer: {colour_yellow}{get_computer_number}{colour_end} Your number: {colour_yellow}{player_number}{colour_end}"


            #Check guess option
            if (player_guess_option == "1" and predict_greater):

                #Add 1 to player score
                player_correct_guess += 1


                #Compute player score
                if (play_number == 0 and player_score == 0):

                    player_score += 50

                elif (play_number == 1 and player_score == 0):

                    player_score += 50

                elif (play_number == 1 and player_score == 50):

                    player_score += 150

                elif (play_number == 2 and player_score == 200):

                    player_score += 200

                elif ((play_number == 2 and player_score == 0) or (play_number == 2 and player_score == 50)):

                    player_score += 50

                #Calculate percentage correct
                percentage_correct = int(player_correct_guess / maximum_play_count * 100)

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{higher_message}. {colour_yellow}{percentage_correct}% Correct{colour_end} {colour_blue}Score: {player_score}{colour_end}")
                print()
                input(f"{colour_violet_bg}Press Enter key to continue ...{colour_end}")
            
            elif (player_guess_option == "2" and predict_lower):

                #Add 1 to player score
                player_correct_guess += 1

                #Compute player score
                if (play_number == 0 and player_score == 0):

                    player_score += 50

                elif (play_number == 1 and player_score == 0):

                    player_score += 50

                elif (play_number == 1 and player_score == 50):

                    player_score += 150

                elif (play_number == 2 and player_score == 200):

                    player_score += 200

                elif ((play_number == 2 and player_score == 0) or (play_number == 2 and player_score == 50)):

                    player_score += 50

                #Calculate percentage correct
                percentage_correct = int(player_correct_guess / maximum_play_count * 100)

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{lower_message}. {colour_yellow}{percentage_correct}% Correct{colour_end} {colour_blue}Score: {player_score}{colour_end}")
                print()
                input(f"{colour_violet_bg}Press Enter key to continue ...{colour_end}")

            elif (player_guess_option == "3" and predict_equals):

                #Add 1 to player score
                player_correct_guess += 1

                #Compute player score
                if (play_number == 0 and player_score == 0):

                    player_score += 50

                elif (play_number == 1 and player_score == 0):

                    player_score += 50

                elif (play_number == 1 and player_score == 50):

                    player_score += 150

                elif (play_number == 2 and player_score == 200):

                    player_score += 200

                elif ((play_number == 2 and player_score == 0) or (play_number == 2 and player_score == 50)):

                    player_score += 50

                #Calculate percentage correct
                percentage_correct = int(player_correct_guess / maximum_play_count * 100)

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{equal_message}. {colour_yellow}{percentage_correct}% Correct{colour_end} {colour_blue}Score: {player_score}{colour_end}")
                print()
                input(f"{colour_violet_bg}Press Enter key to continue ...{colour_end}")

            else:

                os.system("clear")
                print(f"{self.firstname} your option was {player_guess_option}")

                print()
                print(f"{incorrect_guess_message}. {colour_yellow}{percentage_correct}% Correct{colour_end} {colour_blue}Score: {player_score}{colour_end} ")
                print()
                input(f"{colour_violet_bg}Press Enter key to continue ...{colour_end}")

        #End of the Play For Loop

        return get_firstname,get_lastname,player_correct_guess,percentage_correct,player_score


#Class to export results
class Export_Results:


    #Initialise all inputs
    def __init__(self,res_firstname,res_lastname,res_percentage,res_score,res_date):

        self.res_firstname = res_firstname
        self.res_lastname = res_lastname
        self.res_percentage = res_percentage
        self.res_score = res_score
        self.res_date = res_date


    #Save file to csv file
    def Save_Result(self):

        #Import library
        
        file_exist = os.path.isfile("predict.csv")



        get_firstname = self.res_firstname
        get_lastname = self.res_lastname
        get_percentage = self.res_percentage
        get_score = self.res_score
        get_date = self.res_date

        result_list = [get_firstname,get_lastname,get_percentage,get_score,get_date]

        #Check if file exist
        if (file_exist):


            #Create new file 
            with open("predict.csv", "a+", newline="") as saved_results:

                #Define writer
                result_writer = csv.writer(saved_results, delimiter=",")

                #Write data to csv file
                #result_writer.writeheader() #Write header
                result_writer.writerow(result_list)

            saved_results.close()

        else:

            #Appned to file
            with open("predict.csv", "w", newline="") as saved_results:

                #Define writer
                result_header = ["Firstname","Lastname","Percentage","Score","Date"]
                result_writer = csv.writer(saved_results, delimiter=",")

                result_writer.writerow(result_header) #Write header
                result_writer.writerow(result_list)

            saved_results.close()




#******* MANIN PROGRAM STARTS HERE ***********


def Play_Predict():


    #Collate results
    play_results = []

    run_program = "y"

    #Take player name
    get_player_game = Predict(input("Input your firstname: ").capitalize(), input("Input your lastname: ").capitalize())

    while (run_program == "y" or run_program == "Y"):



        #Get the player attributes from game play
        get_play_attributes = get_player_game.Game_Play()

        #Clear Screen
        os.system("clear")



        def Set_Result_Colour(in_score):

            #Variable Score Zero
            guess_zero = f"{colour_red}[3]{colour_end}"
            percetage_zero = f"{colour_red}[100%]{colour_end}"
            score_zero = f"{colour_red}[400]{colour_end}"

            #Variable Score One
            guess_one = f"{colour_beige}[3]{colour_end}"
            percetage_one = f"{colour_beige}[100%]{colour_end}"
            score_one = f"{colour_beige}[400]{colour_end}"

            #Variable Score Two
            guess_two = f"{colour_violet}[3]{colour_end}"
            percetage_two = f"{colour_violet}[100%]{colour_end}"
            score_two = f"{colour_violet}[400]{colour_end}"

            #Variable Score Three
            guess_three = f"{colour_green}[3]{colour_end}"
            percetage_three = f"{colour_green}[100%]{colour_end}"
            score_three = f"{colour_green}[400]{colour_end}"


            #Return result colour
            if (in_score == 0):

                return guess_zero,percetage_zero,score_zero

            elif (in_score == 1):

                return guess_one,percetage_one,score_one

            elif (in_score == 2):

                return guess_two,percetage_two,score_two

            elif (in_score == 3):

                return guess_three,percetage_three,score_three




        print("Your results:")

        #Add play results to list

        #Get updated time
        today_date_time = datetime.datetime.now()
        date_time_format = today_date_time.strftime("%d/%m/%y,%H:%M")
        


        #Print attributes     
        print(f'''
        
        {colour_blue_bg}{get_play_attributes[0]} {get_play_attributes[1]}. Time: {date_time_format}{colour_end}

        Correct Guess:      {colour_yellow}{get_play_attributes[2]} questions{colour_end} {Set_Result_Colour(get_play_attributes[2])[0]} 
        
        Percentage Correct: {colour_yellow}{get_play_attributes[3]}%{colour_end} {Set_Result_Colour(get_play_attributes[2])[1]}
        
        Score:              {colour_yellow}{get_play_attributes[4]}{colour_end} {Set_Result_Colour(get_play_attributes[2])[2]}
        
        ''')

        

        collate_player_result = Export_Results(get_play_attributes[0], get_play_attributes[1], get_play_attributes[3], get_play_attributes[4],date_time_format)

        #Append to player list
        play_results.append(collate_player_result)

        collate_player_result.Save_Result()

        #Test result
        for result in play_results:

            print(result.res_firstname,result.res_lastname,result.res_percentage,result.res_score,result.res_date)


        while True:

            try:

                #Get input to exit or play 
                play_again = input("Do you wish to play again? y/n: ")

                if (play_again == "y" or play_again == "Y" or play_again == "n" or play_again == "N"):

                    #Update run program
                    run_program = play_again
                    print()
                    input(f"{colour_violet_bg}Press Enter to continue...{colour_end}")
                    os.system("clear")

                    break
            except:

                pass


#Check leaderboard
def See_Leader_Board():

    #Import Library
    import os

    #Import csv file
    file_name = "predict.csv"
    data_frame = pd.read_csv(file_name)
    

    #Game File Store
    game_file_store = os.path.isfile("predict.csv") 

    #Check for file store
    if (game_file_store):



        #Option to perform filtered search of all data
        print('''

        Historical Data Sub Menu
        1. Historical data by player name
        2. All Historical Data
        3. Highest score player(s)

        ''')

        #Ensure the input is 1 or 2
        while True:

            try:

                in_option = input("Input option: ")
                if (in_option == "1" or in_option == "2" or in_option == "3"):
                    break
            except:
                pass

        
        #Plyaer chooses option 1
        if (in_option == "1"):

            leaderboard_search = input("Input your first or your lastname: ").capitalize()

            #Pass through Pandas library (Search first or last names)
            search_filter_firstname = data_frame.loc[(data_frame["Firstname"] == leaderboard_search) | (data_frame["Lastname"] == leaderboard_search)]

            
            #Clear screen
            os.system("clear")
            print(f'''

            {colour_yellow}*********** SEARCH RESULTS ************{colour_end}

            ''')

            print(search_filter_firstname)


            input("Press Enter to continue...")

        #Player chooses option 2
        elif (in_option == "2"):


            #Clear Screen
            os.system("clear")

            print(f"{colour_yellow}******** Hsitorical Game Data *********{colour_end}")
            print()

            print(data_frame)
        
            print()
            input("Press Enter key to continue...")

        elif (in_option == "3"):

            os.system("clear")
            input("Place Holder!!!! Press enter to continue")

            

    

        #Call Main mneu
        Main_Menu()
        
        
    else:

        print()
        input(f"{colour_red}No historic data available !!!. Press Enter key for main menu{colour_end}")

        #Call Main Menu
        Main_Menu()




#Call Main Program


#Main Menu Function
def Main_Menu():

    #Clear screen
    os.system("clear")


    print(f'''

    {colour_yellow}***** THE PREDICT GAME *****{colour_end}

    The Goal!!!! Can you guess if the computer's number will be higher or lower than your number


    MENU

    1. Check Leader Board

    2. Play Game

    3. Exit

    ''')

    while True:

        try:


            input_option = input("Make an option: ")

            if (input_option == "1" or input_option == "2" or input_option == "3"):

                break
        
        except:

            pass

    if (input_option == "1"):

        See_Leader_Board()

    elif (input_option == "2"):

        Play_Predict()

    elif (input_option == "3"):

        sys.exit()


#Call menu
Main_Menu()



        

