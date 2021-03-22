'''
Description: Number matching game which will be designed using Python Classes

1. Computer will generate 6 numbers
2. Player will enter 6 numbers
3. Sets (Intersects) will be used to match the numbers
4. Prize money

Written By: Ufuoma Okoro


'''
#Import libraries
import os
import sys
from datetime import date
from numpy import sort

#Set colour pallet
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Variables

player_details_list = [] #List to hold user identity details
player_age_limit = 18
played_numbers = []

#Function to clear screen
def Clear_Screen():

    os.system("clear")


#Class to create player object and numbers
class Player:

    def __init__(self,player_firstname,player_lastname,player_dob_dd,player_dob_mm,player_dob_yyyy):

        self.player_firstname = player_firstname
        self.player_lastname = player_lastname
        self.player_dob_dd = player_dob_dd
        self.player_dob_mm = player_dob_mm
        self.player_dob_yyyy = player_dob_yyyy

    
    #Function to calculate age restriction
    def Calc_Age_Restriction(self):

        #Import libraries
        from datetime import date

        #Variables
        today_date = date.today()
        days_in_year = 365.2425


        get_age_day = self.player_dob_dd
        get_age_month = self.player_dob_mm
        get_age_year = self.player_dob_yyyy

        #Date of birth
        player_dob = date(get_age_year,get_age_month,get_age_day)

        player_age = int((today_date - player_dob).days / days_in_year)

        return player_age








#Funtion to get player details
def Get_Player_Details():

    temp_player_details = []

    input_description = ["Input your firstname: ", "Input your lastname: ", "Input your day of birth dd: ", "Input your month of birth mm: ", "Input your year of birth yyyy: "]


    for input_questions in input_description:
        Clear_Screen()

        input_player_details = input(f"{colour_yellow}{input_questions}{colour_end}")

        #Check for date of birth
        if (input_questions == "Input your day of birth dd: " or input_questions == "Input your month of birth mm: " or input_questions == "Input your year of birth yyyy: "):

            while not (input_player_details.isdigit()):

                input_player_details = input(f"{colour_red}{input_questions}{colour_end}")
            
            #Convert input to integer
            convert_dob_to_integer = int(input_player_details)

            #Append the details to the player
            temp_player_details.append(convert_dob_to_integer)

        else:


            #Append the details to the player
            temp_player_details.append(input_player_details)

        
    #Return staff details
    return temp_player_details

#Function to play numbers
def Play_Numbers():


    #Player Number List
    player_numbers = []

    #Player question input list
    player_number_questions = ["First","Second","Third","Fourth","Fifth","Sixth"]

    for question_number in player_number_questions:

        Clear_Screen()
        print(f"{colour_green}********** Your Numbers ***************{colour_end}")
        print()
        print(f'''
            1. Enter 1 number between 1 and 60 and press enter
            2. you will be allowed to enter 6 numbers

        ''')
        #Display numbers
        print(f"{colour_red}Numbers played: {player_numbers}{colour_end}")
        print()

        get_player_number = input(f"{colour_blue}Input {question_number} number:{colour_end} ")

        

        #Check the input is digit
        while not (get_player_number.isdigit()):

            get_player_number = input(f"{colour_red}Invalid input!!! Input must be a number. Input {question_number} number:{colour_end} ")
            
        #Convert input into an integer
        convert_player_input = int(get_player_number)

        #Check number input
        while not (convert_player_input >= 1 and convert_player_input <= 60):

            player_input = input("Invalid number range. Enter number between 1 and 60: ")

            convert_player_input = int(player_input)


        #Append number to player number list
        player_numbers.append(convert_player_input)
        

    #Return player numbers
    return player_numbers


#Get computer random numbers
def Computer_Numbers():


    #Import library
    import random
   
    #Generate random number
    generate_numbers = random.sample(range(60),6)

    return generate_numbers















#********** MAIN PROGRAM STARTS HERE ****************

#Get player input data
player_details_list = Get_Player_Details()

#Create object from input data
player_object = Player(player_details_list[0], player_details_list[1], player_details_list[2], player_details_list[3], player_details_list[4])



#Check player age
get_player_age = player_object.Calc_Age_Restriction()

if (get_player_age >= player_age_limit):

    Clear_Screen()
    print(f"{colour_green}You are {get_player_age} and are allowed to play{colour_end}")
    print()

    #Print object
    print(player_object.player_firstname,player_object.player_lastname,player_object.player_dob_dd,player_object.player_dob_mm,player_object.player_dob_yyyy)
    print()
    input(f"{colour_blue}Press any key to continue...{colour_end}")

    #Play numbers
    played_numbers = Play_Numbers()

    #Get computer numbers
    computer_numbers = Computer_Numbers()

    #Create player and computer sets
    player_numbers_set = set(played_numbers)
    computer_numbers_set = set(computer_numbers)

    Clear_Screen()
    #Display played numbers
    print("********* Numbers Played **********")
    print()
    print(f"Player:   {sort(played_numbers)}")
    print()
    print(f"Computer: {sort(computer_numbers)}")


else:
    Clear_Screen()
    print(f"{colour_red}You are {get_player_age}. You must be 18 or above to play!!!{colour_end}")
    print()
    sys.exit()


    


