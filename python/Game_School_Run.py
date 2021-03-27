'''
Description: Game School Run

This project is a game that will take the player through school life

The progression will depend on the role of a dice which as 4 movement [0,1,3,6]

0 - No movement
1 - Normal progression
3 - No movement and bank or 1 movement
6 - super move to next education

Total game time is 5 mins countdown

If timed out, then you are classed as not competing your education and your reward will be Salary after

Category
	• Nursery Salary no salary
	• Primary minimum wage
	• Secondary a little more than minimum wage
University higher wage

'''

#Import library
import os

#Set colour pallete
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"


def Player_Details_Input():

    while True:

        try:

            take_player_firstname, take_player_lastname = input("Enter your First and Last names: ").split()

            return take_player_firstname, take_player_lastname
        except:

            pass


#Get player name
get_player_input = Player_Details_Input()

#Create object for player name
class Player_Name:

    def __init__(self,player_firstname,player_lastname):

        self.player_firstname = player_firstname
        self.player_lastname = player_lastname


#Class to roll dice
class Roll_Dice:

    def __init__(self,player_firstname,player_lastname):

        self.player_firstname = player_firstname
        self.player_lastname = player_lastname

    
    #Roll Dice
    def Roll(self):

        import random

        #Get player names
        get_player_firstname = self.player_firstname
        get_player_lastname = self.player_lastname

        #Possible Dice Numbers
        dice_numbers = [0,1,3,6]

        #Roll dice
        player_roll_dice = random.choice(dice_numbers)

        return player_roll_dice


#Process player details
process_player_input = Player_Name(get_player_input[0].capitalize(), get_player_input[1].capitalize())


#print(process_player_input.player_firstname, process_player_input.player_lastname)

process_player_roll_dice = Roll_Dice(process_player_input.player_firstname,process_player_input.player_lastname)

#Get player name and rolled dice
print()
print(process_player_roll_dice.player_firstname,process_player_roll_dice.player_lastname,process_player_roll_dice.Roll())



