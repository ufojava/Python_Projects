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

#Process player roll dice
process_player_roll_dice = Roll_Dice(process_player_input.player_firstname,process_player_input.player_lastname)


#Function to play game
def School_Run():

    #Variables
    
    
    educaiton_university = 4
    player_bank = []

    #Function for secondary education
    def Secondary_Education():

        #Variable
        education_secondary = 6
        secondary_player_bank = []

        print()
        for secondary in range(education_secondary):
            os.system("clear")

            print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)

            my_dice_roll = process_player_roll_dice.Roll()
            print()
            print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
            print()

            input("Secondary - Press any key to continue...")
        


    #Function for Primary education
    def Primary_Education():

        #Variable
        education_primary = 6
        primary_player_bank = []

        print()
        for primary in range(education_primary):
            os.system("clear")
            print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)

            my_dice_roll = process_player_roll_dice.Roll()
            print()
            print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
            print()

            input("Primary - Press any key to continue...")

            if (my_dice_roll == 3):

                #Check if the bank count equals 2
                if (len(primary_player_bank) == 2):

                    print(f"Congratulations!! You have 2 3 dice rolled in bank so you automatilcally advance to next education level ")


                    #Ask player if they wish to bank 
                    bank_question = input("3 allows you to bank or move one step y /n: ")

                    if( bank_question == "y" or bank_question == "Y"):

                        #Bank
                        print('''You have chosen to bank your dice roll 3
                        You need 2 of dice rolled 3 to make an express pass to the primary education
                        
                        ''')
                        primary_player_bank.append(my_dice_roll)
                        print(f"You currently have {len(bank_question)} of 3 dice roll in the bank")

                    else:
                        print()
                        print(f"{colour_green}You have chosen not to bank so you move one step{colour_end}")

            
            elif (my_dice_roll == 6):

                print("Congratulations!!! You have rolled 6 so you advance to the next education level")
                print()
                input("Primary - Press any key to progress...")

                #Call Secondary funtion
                Secondary_Education()

                #Breaks out of the Nursary loop
                break

            elif (my_dice_roll == 0):

                print("Sorry you rolled 0, so you will remain where you are")

            elif (my_dice_roll == 1):

                print()
                print("Well done!! You have passed your exams, you move one step to Nursary year 2")




    #Function for Nursary education
    def Nursary_Education():

        #Variables
        education_nursary = 3
        nursary_player_bank = []

        print()
        for nursary in range(education_nursary):

            os.system("clear")
            print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)

            #My dice roll
            my_dice_roll = process_player_roll_dice.Roll()
            print()
            print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
            print()

            if (my_dice_roll == 3):

                #Check if the bank count equals 2
                if (len(nursary_player_bank) == 2):

                    print(f"Congratulations!! You have 2 3 dice rolled in bank so you automatilcally advance to next education level ")


                    #Ask player if they wish to bank 
                    bank_question = input("3 allows you to bank or move one step y /n: ")

                    if( bank_question == "y" or bank_question == "Y"):

                        #Bank
                        print('''You have chosen to bank your dice roll 3
                        You need 2 of dice rolled 3 to make an express pass to the primary education
                        
                        ''')
                        nursary_player_bank.append(my_dice_roll)
                        print(f"You currently have {len(bank_question)} of 3 dice roll in the bank")

                    else:
                        print()
                        print(f"{colour_green}You have chosen not to bank so you move one step{colour_end}")

            
            elif (my_dice_roll == 6):

                print("Congratulations!!! You have rolled 6 so you advance to the next education level")
                print()
                input("Primary - Press any key to progress...")

                #Call primary function
                Primary_Education()

                #Breaks out of the Nursary loop
                break

            elif (my_dice_roll == 0):

                print("Sorry you rolled 0, so you will remain where you are")

            elif (my_dice_roll == 1):

                print()
                print("Well done!! You have passed your exams, you move one step to Nursary year 2")



            print()
            input("Nursary - press any key to continue...")


    #Education start at Nusary
    Nursary_Education()
        

        
        



print(process_player_roll_dice.player_lastname, process_player_roll_dice.player_lastname,process_player_roll_dice.Roll())

School_Run()




