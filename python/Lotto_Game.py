'''
Title: Lottery Game

***** Instructions ******

Generate randome 6 number for draw
Enter pick 6 numbers
Store the 6 number in a list / Array]
Compare both arrays for similar numbers
Award prizes money for  3 4,5,6


Written By: Ufuoma Okoro

Department Home Office

'''

#Import modules
from numpy import random
from numpy import sort
import os
import time

player_name = ""

def Generate_Computer_Lotto_Numbers():


    #Create random number between 1 and 59
    computer_random_six_number_two = random.randint(59, size=(6))
    computer_lotto_numbers = []

    #Create computer number list
    for comp_gen_number in computer_random_six_number_two:
        computer_lotto_numbers.append(comp_gen_number)

    #Create set from the array
    computer_gen_lotto_numbers_set = set(computer_lotto_numbers) #Computer generated numbers

    #Return set Set
    return computer_gen_lotto_numbers_set

#Run the computer function to genrate number
get_computer_numbers = Generate_Computer_Lotto_Numbers()
display_computer_joined_numbers = " " . join(str(get_computer_numbers))






#Function to take input selection from player
def Player_Number_Picker():



    max_num_pick = 6 #Maximum number of pick
    player_lotto_numbers_pick = []
    pick_counter = 0
    pick_description = " "



    #User input description
    input_first = "First"
    input_second = "Second"
    input_third = "Third"
    input_fourth = "Fourth"
    input_fifth = "Fifth"
    input_sixth = "Sixth"




    for count in range(max_num_pick):

        #Start pick counter
        pick_counter += 1
        if (pick_counter == 1):
            pick_description = input_first
        elif (pick_counter == 2):
            pick_description = input_second
        elif (pick_counter == 3):
            pick_description = input_third
        elif (pick_counter == 4):
            pick_description = input_fourth
        elif (pick_counter == 5):
            pick_description = input_fifth
        elif (pick_counter == 6):
            pick_description = input_sixth


        #Enter loto number
        os.system("clear")

        #Display the players picked numbers
        display_player_joined_numbers = " ".join(str(player_lotto_numbers_pick))
        print(f"Picked: {display_player_joined_numbers}")


        print()
        #Input player numbers
        player_lotto_pick = int(input(f"Pick {pick_description} number between 1 and 59: "))
        print()

        #Check number input between 1 and 59
        while (player_lotto_pick < 1 or player_lotto_pick > 59 ):
            print("Inavlid number range!!! Input number between 1 and 59 ")
            print()
            player_lotto_pick = int(input(f"Pick {pick_description} number: "))


        #Append the pick to the list
        player_lotto_numbers_pick.append(player_lotto_pick)

    #Create player set from the list
    player_lotto_numbers_pick_set = set(player_lotto_numbers_pick) #Player picked numbers

    #Return the player picked list
    return player_lotto_numbers_pick_set

    

#Funciton to process Player and Computer sets
def Process_Lotto_Matches(in_computer_numbers,in_player_numbers):

    number_matches = set.intersection(in_computer_numbers,in_player_numbers)

    return number_matches

#Function to create space
def Create_Line_Space(num_of_lines):

    for space in range(int(num_of_lines)):
        print()


def Process_Words(in_word):

    #Define how to slow word using os.system.stdout
    slow_input_word = os.sys.stdout

    for in_letter in in_word:

        slow_input_word.write(in_letter)
        slow_input_word.flush()
        time.sleep(.1)
    return ""




def Game_Introduction():

    #Read dictionary for greetings
    get_greetings = open("Greeting_Words.txt")

    #Variables

    #Input questions
    player_name_question = "What is your name? "
    player_how_do_you_do_question = "How are you doing? "

    Create_Line_Space(2)
    input_player_name = input(f"{Process_Words(player_name_question)}")
    Create_Line_Space(2)
    input_player_how_do_you_do = input(f"{Process_Words(player_how_do_you_do_question)}")
    Create_Line_Space(2)

    #Check player well being
    if(input_player_how_do_you_do in get_greetings.read()):

        Process_Words("Glad you are doing well")
    else:

        Process_Words("Oh! sorry you are not doin so well")

    return input_player_name


def Calc_Prize_Money(in_number_match):

    #Variable prize mone
    one_num_match = (in_number_match == 1)
    two_num_match = (in_number_match == 2)
    three_num_match = (in_number_match == 3)
    four_num_match = (in_number_match == 4)
    five_num_match = (in_number_match == 5)
    six_num_match = (in_number_match == 6)

    #Apportion prize money in GB Pounds
    if (one_num_match):

        return 10.00

    elif (two_num_match):

        return 20.00

    elif (three_num_match):

        return 400.00

    elif (four_num_match):

        return 5000.00

    elif (five_num_match):

        return 25000.00

    elif (six_num_match):

        return 150000.00
        
    else:

        return 0.00





'''
Main progran begins from here

'''

#Game Introduction
player_name = Game_Introduction()






#Call player functions to display playe lotto numbers
get_player_numbers = Player_Number_Picker()
player_joined_numbers = " " . join(str(get_player_numbers))

#Funciton to retreive matching numbers between player imput and computer generated numbers
get_lotto_number_matches = Process_Lotto_Matches(get_computer_numbers,get_player_numbers)


#Clear screen do display player lotto numbers
os.system("clear")
print('''
****** Player Lotto Numbers **********
''')

print(f"Player Numbers: {player_joined_numbers}")


print('''
****** Computer Generated Lotto Numbers ********
''')

#Keep the display for 3 seconds before priting the computer generated numbers
time.sleep(3.0) 

#Display the computer genrated numbers

print(f"Lotto Numbers: {display_computer_joined_numbers}")
print()



#Sleep before process below begin
time.sleep(3.0)

#Get proze money
if (len(get_lotto_number_matches) == 1):

    print(f"Congratulations !!! {player_name}, you have {len(get_lotto_number_matches)} match and have won £{Calc_Prize_Money(len(get_lotto_number_matches))}")

elif (len(get_lotto_number_matches) > 1):

    print(f"Congratulations !!! {player_name}, you have {len(get_lotto_number_matches)} matches and have won £{Calc_Prize_Money(len(get_lotto_number_matches))}")

else:

    print(f"Sorry {player_name}, you have had no matches and have won £{Calc_Prize_Money(len(get_lotto_number_matches))}")

print()


