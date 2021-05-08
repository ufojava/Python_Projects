'''
Description: 5 Letter word game

1. Class - Personal  information Take student first, last names 
2. Class take in personal information and function process subjects:
3. Function to load csv file dictionary and save to a list
4. Pick a random word from dictioaary
5. List 2 letters from the 5 
6. Each time the player gets a reveal 20 points is taken from the maximum 100 points
7. Save player score

'''


#Library imports
import os
import csv
import pandas as pd
import sys
import datetime
import random


#Create Colour pallete - Foreground
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Create Colour pallete - Background
colour_violet_bg = "\33[45m"
colour_blue_bg = "\33[41m"


#Function to laod Dictionary
def Load_Dictionary():

    

    #Dictionary file
    dictionary_file = "5_Letter_Easy_Dic.csv"

    #Empty list for dcitionary
    word_list = []

    with open(dictionary_file, "r", ) as word_dictionary:

        dic_reader = csv.DictReader(word_dictionary)

        for word in dic_reader:

            word_list.append(word["Word"])

    
    #Pick random word form the list
    pick_word = random.choice(word_list)

    return pick_word


#Function to clear screen
def Clear_Screen():

    if (os.name == "nt"):

        os.system("cls")
    
    else:

        os.system("clear")


class Player_Info:

    def __init__(self,in_firstname,in_lastname,in_word):

        self.in_firstname = in_firstname
        self.in_lastname = in_lastname
        self.in_word = in_word #Run function to produce word

    
    #Test student information

    def Process_Player_Information(self):

        get_player_firstname = self.in_firstname
        get_player_lastname = self.in_lastname
        get_dic_word = self.in_word


        return get_player_firstname, get_player_lastname,get_dic_word


    

#Clear Screen
Clear_Screen()

#Input player infomation
get_player_information = Player_Info(input("Enter your firstname: ").capitalize(),input("Enter your lastname: ").capitalize(),Load_Dictionary())


'''
1. Need to produce randume numbers in range 0 to 5
2. The numbers will be used to reveal random word
3. Player will then be given the chance to guess letter or opt to reveal the next letter


'''


class Play_Game:


    def __init__(self,get_firstname,get_lastname,get_word):

        self.get_firstname = get_firstname
        self.get_lastname = get_lastname
        self.get_word = get_word

    
    
    def Begin_Play(self):

        player_firstname = self.get_firstname
        player_lastname = self.get_lastname
        random_word = self.get_word


        #Create random numbers to reveal word
        random_letter_reveal = random.sample(range(5), 5)

        #Clear Screen
        Clear_Screen()

        print(f'''

        {colour_yellow}
        ********* REVEAL ************

        1. Two letters of a 5 letter word will be revealed
        2. If you are unable to correctly enter the correct letter, you can opeted to REVEAL
        {colour_end}


        ''' )

        print(random_word[random_letter_reveal[0]],random_word[random_letter_reveal[1]])

        guess_first_letter = input("Enter your first letter: ").capitalize()

        if (guess_first_letter in random_word):

            print(f"Correet guess: {guess_first_letter}")
            

        else:

            print(f"Incorrect guess: {guess_first_letter}")
            

        print(random_word)
        print()

        input("Press Enter key to continue")

    
        

#Play game
Play_Game(get_player_information.Process_Player_Information()[0], get_player_information.Process_Player_Information()[1], get_player_information.Process_Player_Information()[2]).Begin_Play()








