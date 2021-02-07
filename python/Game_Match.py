'''
Synopsis: Game to match player 6 number input to the computer generated 20 numbers

Written By: Ufo Okoro

Department: CodeBase

'''

#Import Libraries
import os
from numpy import random, sort

#Variables

#Player number Array / List
player_numbers = []

#Function to generate and sort 10 numbers in range  0 - 20
def Gen_Computer_Numbers():

    number_range = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    #Use numpy permutation to generate the number
    generate_computer_numbers = random.permutation(number_range) [:10]

    #No w sort the numbers
    sort_comp_gen_num = sort(generate_computer_numbers)

    #Now return the array list
    return sort_comp_gen_num


def Get_Player_Numbers():

    #Player input counter
    player_counter = 0

    #Input Player Numbers
    input_player_numbers = []

    os.system("clear")
    print('''
    ******* Match *********

    Your goal is to match 3 numbers from the 10 computer genrated numbers to win a prize !!!

    Input number between 1 and 20
    ''')

    while (player_counter != 6):
        player_counter += 1

        #To change the input description
        if (player_counter < 2):

            #Take player input
            player_input = int(input(f"Play count is {player_counter}. Enter number: "))

            #Error Check - Ensure then input in not grater than 20
            while(player_input > 20):

                print()
                player_input = int(input(f"Invalid number !!! Enter number between 1 and 20: "))

            #Add the number to player list
            input_player_numbers.append(player_input)

        elif (player_counter >= 2):

            #Take player input
            player_input = int(input(f"Play count is {player_counter}. Next: "))

            #Error Check - Ensure then input in not grater than 20
            while(player_input > 20):

                print()
                player_input = int(input(f"Invalid number !!! Enter number between 1 and 20: "))

            #Add the number to player list
            input_player_numbers.append(player_input)

        #Sort player input numbers
        sort_player_numbers = sort(input_player_numbers)

    #Return player input numbers
    return sort_player_numbers



#Call Function Gen_Com;puter_Numbers and assign to variable
computer_numbers = Gen_Computer_Numbers()

#Call Function for player input numbers
player_numbers = Get_Player_Numbers()

#Function to convert Computer and Player numbers for matching
def Match_Numbers(in_computer_numbers,in_player_numbers):

    #Convert Computer numbers
    get_computer_numbers = set(in_computer_numbers)

    #Convert Player numbers
    get_player_numbers = set(in_player_numbers)

    #Match numbers
    matched_numbers = set.intersection(get_computer_numbers,get_player_numbers)

    return matched_numbers

#Main program starts here
#Clear screen to describe the function of the gamne

os.system("clear")
print('''
Match Game Results:

''')
print(f"Computer generated numbers: {computer_numbers}")
print()
print(f"Player input numbers: {player_numbers}")
get_matched_numbers = Match_Numbers(computer_numbers,player_numbers)
total_number_of_matches = len(get_matched_numbers)
print()

if (total_number_of_matches == 1):

    print(f"{total_number_of_matches} match  {get_matched_numbers}")

elif (total_number_of_matches > 1):

    print(f"{total_number_of_matches} matches  {get_matched_numbers}")

else:

    print(f"No matches found, better luck next time")

