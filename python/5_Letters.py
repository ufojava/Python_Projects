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
from pyfiglet import Figlet


#Create Colour pallete - Foreground
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Create Colour pallete - Background
colour_violet_bg = "\33[45m"
colour_blue_bg = "\33[44m"

#Initialize Figlet
game_header = Figlet(font= "slant")



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

print(f'''
{colour_yellow}
{game_header.renderText("REVEAL")}
{colour_end}

{colour_green}How to play Reveal{colour_end}

1. Two letters of a 5 letter word will be revealed
2. You have four attemps to form the 5 letter word

{colour_green}Help!!!{colour_end}

3. If you have difficulty inputing a letter to form the 5 letter word, you could take your single partial reveal
4. You could take the partial reveal at any point if not taken

''' )
input(f"{colour_violet_bg}Press Enter key to begin playing{colour_end}")

Clear_Screen()

print(f'''
{colour_yellow}
{game_header.renderText("REVEAL")}
{colour_end}

{colour_green}Input your names:{colour_end}

1. Firstname
2. Lastame
''')

#Input player infomation
get_player_information = Player_Info(input("Enter your firstname: ").capitalize(),input("Enter your lastname: ").capitalize(),Load_Dictionary())


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


        #Create Letter list
        letter_list = [random_word[random_letter_reveal[2]],random_word[random_letter_reveal[3]],random_word[random_letter_reveal[4]]]

        

        play_counter = 3
        play_description_counter = 0
        play_description = ["first","second","third","fourth"]
        help_counter = 0

        #Format the colours to the default reveal letters
        first_reveal_letter = f"{colour_green}{random_word[random_letter_reveal[0]]}{colour_end}"
        second_reveal_letter = f"{colour_green}{random_word[random_letter_reveal[1]]}{colour_end}"

        #Other letters that make up the word
        third_reveal_letter = f"{colour_green}{random_word[random_letter_reveal[2]]}{colour_end}"
        fourth_reveal_letter = f"{colour_green}{random_word[random_letter_reveal[3]]}{colour_end}"
        fifth_reveal_letter = f"{colour_green}{random_word[random_letter_reveal[4]]}{colour_end}"


        #Insert the values into a list
        letters_reveals = [first_reveal_letter,second_reveal_letter]


        


        for play in range(play_counter):
            
            #Clear screen
            #Clear_Screen()

            if (play == 0):


                print(f'''
                {colour_yellow}
                {game_header.renderText("REVEAL")}
                {colour_end}

                {colour_blue_bg}Hello {player_firstname}{colour_end}
                
                This is your first attempt to input a letter to guess the five letter word.

                {colour_yellow}Help !!!!{colour_end}

                You will be presented with an oportunity to take a single partial reveal of the word when asked.
                
                ''' )
            else:

                print(f'''
                {colour_yellow}
                {game_header.renderText("REVEAL")}
                {colour_end}

                {colour_blue_bg}{player_firstname}{colour_end}
                
                Continue to play by guessing your letters!!!

                {colour_yellow}Remember !!!{colour_end}

                If you have not taken your partial reveal, then you can take it if prompted.


                ''' )


            #Clear Screen
            Clear_Screen()
            
            
            print(f'''
            {colour_yellow}
            {game_header.renderText("REVEAL")}
            {colour_end}
            
            {colour_blue}{player_firstname}{colour_end}, below are the  two letters of the 5 letter word:

            {colour_green}Remember your partial reveal help if you have not taken it..{colour_end}

            ''')
            print(" ".join(letters_reveals))
            print()

            #Get help
            while not (help_counter > 0):

                #Error check the help needed input
                try:
                    Clear_Screen()
                    print(f'''{colour_yellow}{game_header.renderText("REVEAL")}{colour_end}''')
                    print(f'''

                    Below are the 2 letters from the random word. Any clues!!! 
                    You can get one time help at any point in the game.
                    
                    ''')

                    print(" ".join(letters_reveals))
                    print()

                    help_needed = input(f"{colour_blue}{player_firstname}{colour_end} do you need a little help with the word? y/n: ")
                    print()

                    if (help_needed == "y" or help_needed == "Y" or help_needed == "n" or help_needed == "N"):

                        break
                except:

                    pass
            
            if (help_needed == "y" or help_needed == "Y"):

                temp_reveal_word = random_word[0:3]

                print(f"{colour_blue}{temp_reveal_word}{colour_end}")
                print()

                #Help is now spent
                help_counter += 1

                #Increse counter by one
                play_counter += 1
                

                input(f"{colour_violet_bg}Press Enter to continue{colour_end}")
                print()
                help_needed = "n"



            
            #Test letter choice input
            while True:

                try:

                    Clear_Screen()
                    print(f'''{colour_yellow}{game_header.renderText("REVEAL")}{colour_end}''')
                    print(f'''
                    
                    Have a go !!!
                    
                    ''')

                    print(" ".join(letters_reveals))
                    print()
                    

                    guess_letter = input(f"{player_firstname} input your {play_description[play_description_counter]} guess: ").capitalize()

                    if (guess_letter != ""):

                        break
                except:

                    pass


            if (guess_letter in random_word):

                print()
                input(f"Correct guess: {colour_blue}{guess_letter}{colour_end} Press Enter key to continue..")
                print()

                for letter in letter_list:

                    if (letter == guess_letter):
                        
                        print(letter_list)
                        #Remove from list
                        letter_list.remove(letter)
                        print()
                        print(letter_list)
            
                    
                        #Colour the letter
                        guessed_letter = f"{colour_green}{letter}{colour_end}"

                        letters_reveals.append(guessed_letter)

                        Clear_Screen()
                        print(" ".join(letters_reveals))

                        print()
                        #Offer help should the player need it
                        

                #Update play description counter 
                play_description_counter += 1
            

            else:

                print()
                input(f"Incorrect guess: {colour_red}{guess_letter}{colour_end} Press Enter key to continue...")
                print()

                #Update play description counter 
                play_description_counter += 1

        #Guess second letter
        Clear_Screen()
            

        print(f"{colour_green}[{random_word}]{colour_end}")
        print()

        input("Press Enter key to continue")

    
        

#Play game
Play_Game(get_player_information.Process_Player_Information()[0], get_player_information.Process_Player_Information()[1], get_player_information.Process_Player_Information()[2]).Begin_Play()








