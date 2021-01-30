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

def Generate_Computer_Lotto_Numbers():


    #Create random number between 1 and 59
    computer_random_six_number_two = random.randint(59, size=(6))
    player_lotto_numbers_pick = []
    computer_lotto_numbers = []

    #Create computer number list
    for comp_gen_number in computer_random_six_number_two:
        computer_lotto_numbers.append(comp_gen_number)

    #Create set from the array
    computer_gen_lotto_numbers_set = set(computer_lotto_numbers) #Computer generated numbers

    #Return set Set
    return computer_gen_lotto_numbers_set




#Keep the display for 3 seconds before priting the computer generated numbers
time.sleep(3.0) 

print('''
********** Weekly Lotto Draw ***************

''')

#Displat the computer genrated numbers
computer_joined_numbers = " " . join(str(Generate_Computer_Lotto_Numbers()))
print(f"Lotto Numbers: {computer_joined_numbers}")
print()



def Player_Number_Picker():



   


    max_num_pick = 6 #Maximum number of pick
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

        player_joined_numbers = " ".join(str(player_lotto_numbers_pick))
        print(f"Picked: {player_joined_numbers}")
        print()
        player_lotto_pick = int(input(f"Pick {pick_description} number between 1 and 59: "))
        print()

        #Check number input between 1 and 59
        while (player_lotto_pick < 1 or player_lotto_pick > 59 ):
            print("Inavlid number range!!! Input number between 1 and 59 ")
            print()
            player_lotto_pick = int(input(f"Pick {pick_description} number: "))


        #Append the pick to the list
        player_lotto_numbers_pick.append(player_lotto_pick)

    

    os.system("clear")

    #Display the final picked numbers
    print(f"Picked Numbers: {player_joined_numbers}")



    '''
    This section will process the computer random numbers and picked numbers

    '''

    

    player_lotto_numbers_pick_set = set(player_lotto_numbers_pick) #Player picked numbers

    #Match numbers between Computer generated numbers and player numbers

    number_match = set.intersection(computer_gen_lotto_numbers_set, player_lotto_numbers_pick_set)



'''
Main progran begins from here

'''

#Call Player Picker  function

#Player_Number_Picker()

