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

    #Clear screen
    os.system("clear")

    print(f'''
    {colour_green}**************** SCHOOL RUN ***************{colour_end}

    ''')

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




    #Function University education
    def University_Education(in_secondary_score):

        #Variable
        power_arm_university = "\U0001F4AA"
        educaiton_university = 4
        university_player_bank = []
        university_year = []
        university_score = 0
        university_year_counter = 0
        secondary_result = in_secondary_score

        print()
        for university in range(educaiton_university):

            #Add 1 to counter
            university_year_counter += 1
            os.system("clear")

            print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Secondary Score: {secondary_result}{colour_end}")

            print()
            print(f"{colour_green}University:{colour_end} {colour_yellow}{university_year}{colour_end}")

            my_dice_roll = process_player_roll_dice.Roll()
            print()

            input("University - Press any key to continue...")

            if (my_dice_roll == 3):

                #Check if the bank count equals 2
                if (len(university_player_bank) == 2):

                    #Reset year count
                    university_year = []
                    for add_arm in range(3):
                        university_year.append(power_arm_university)

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Secondary Score: {secondary_result}{colour_end}")
                    print()

                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()
                    print(f"{colour_green}University:{colour_end} {colour_yellow}{university_year}{colour_end}")
                    print()

                    print(f"Congratulations!! You have rolled 3 twice, so you advance to the next level")

                    input("Press any key to continue...")
                    
                    #Exam Score
                    university_score = 30
                    cumilative_university_score = university_score + secondary_result


                #Ask player if they wish to bank 
                bank_question = input("3 allows you to bank or move one step y /n: ")

                if( bank_question == "y" or bank_question == "Y"):

                    #Reset year count
                    university_year = []

                    #Add three power arms to the nursary
                    for add_arm in range(3):
                        university_year.append(power_arm_university)

                    university_player_bank.append(my_dice_roll)
                    input(f"You currently have {len(bank_question)} in the bank. Press any key to continue...")

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Secondary Score: {secondary_result}{colour_end}")
                    print()
                    print(f"{colour_green}University:{colour_end} {colour_yellow}{university_year}{colour_end}")
                    print()
        
                    
                    

                else:
                    #Add single power arm to year
                    university_year.append(power_arm_university)

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Secondary Score: {secondary_result}{colour_end}")
                    print()
                    print(f"{colour_green}University:{colour_end} {colour_yellow}{university_year}{colour_end}")
                    print()
                    print(f"{colour_green}You have chosen not to bank so you move one step{colour_end}")

                    

            
            elif (my_dice_roll == 6):

                #Reset year count
                university_year = []
                
                #Add six power arm to year
                for add_arm in range(6):

                    university_year.append(power_arm_secondary)

                #Clear Screen
                os.system("clear")

                print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Secondary Score: {secondary_result}{colour_end}")
                print()
                print(f"{colour_green}University:{colour_end} {colour_yellow}{university_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                print("Congratulations!!! You have rolled 6 so you advance to the next education level")
                print()
                input("University - Press any key to progress...")


                #Exam Score
                university_score = 60
                cumilative_university_score = university_score + secondary_result
                

            elif (my_dice_roll == 0):

                print("Sorry you rolled 0, so you will remain where you are")

            elif (my_dice_roll == 1):

                university_year.append(power_arm_university)

                os.system("clear")
                print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Secondary Score: {secondary_result}{colour_end}")
                print()
                print(f"{colour_green}University:{colour_end} {colour_yellow}{university_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")

                print()
                print("Well done!! You have passed your exams, you move one step")
                

 

            print()
            input("University - press any key to continue...")

            #Progress to University to education if 3 stars attained
            if (len(university_year) >= 4 and university_year_counter == 4):

                #Exam Score
                university_score = 10
                cumilative_university_score = university_score + secondary_result
            
            else:

                print()
                print("Your education ends here")

        

    #Function for secondary education
    def Secondary_Education(in_primary_score):

        #Variable
        power_arm_secondary = "\U0001F4AA"
        education_secondary = 6
        secondary_player_bank = []
        secondary_year = []
        secondary_year_counter = 0
        secondary_score = 0
        primary_result = in_primary_score

        print()
        for secondary in range(education_secondary):

            #Add 1 to counter
            secondary_year_counter += 1
            os.system("clear")

            print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Primary Score: {primary_result}{colour_end}")

            print()
            print(f"{colour_blue}Secondary:{colour_end} {colour_yellow}{secondary_year}{colour_end}")

            my_dice_roll = process_player_roll_dice.Roll()
            print()

            if (my_dice_roll == 3):

                #Check if the bank count equals 2
                if (len(secondary_player_bank) == 2):

                    #Reset year count
                    secondary_year = []
                    for add_arm in range(3):
                        secondary_year.append(power_arm_secondary)

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Primary Score: {primary_result}{colour_end}")
                    print()

                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()
                    print(f"{colour_blue}Secondary:{colour_end} {colour_yellow}{secondary_year}{colour_end}")
                    print()
                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()

                    print(f"Congratulations!! You have rolled 3 twice, so you advance to the next level")

                    input("Press any key to continue...")
                    
                    #Exam Score
                    secondary_score = 30
                    cumilative_secondary_score = secondary_score + primary_result
                    
                    #Call Function University Education
                    University_Education(cumilative_secondary_score)

                    #Brake loop
                    break

                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                #Ask player if they wish to bank 
                bank_question = input("3 allows you to bank or move one step y /n: ")
                print()

                if( bank_question == "y" or bank_question == "Y"):

                    #Reset year count
                    secondary_year = []

                    #Add three power arms to the nursary
                    for add_arm in range(3):
                        secondary_year.append(power_arm_secondary)

                    secondary_player_bank.append(my_dice_roll)
                    input(f"You currently have {len(bank_question)} in the bank. Press any key to continue...")

                    '''
                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Primary Score: {primary_result}{colour_end}")
                    print()
                    print(f"{colour_blue}Secondary:{colour_end} {colour_yellow}{secondary_year}{colour_end}")
                    print()
                    '''
        
                    
                    

                else:
                    #Add single power arm to year
                    secondary_year.append(power_arm_secondary)

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Primary Score: {primary_result}{colour_end}")
                    print()
                    print(f"{colour_blue}Secondary:{colour_end} {colour_yellow}{secondary_year}{colour_end}")
                    print()
                    print(f"{colour_green}You have chosen not to bank so you move one step{colour_end}")

                    

            
            elif (my_dice_roll == 6):

                #Reset year count
                secondary_year = []
                
                #Add six power arm to year
                for add_arm in range(6):

                    secondary_year.append(power_arm_secondary)

                #Clear Screen
                os.system("clear")

                print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Primary Score: {primary_result}{colour_end}")
                print()
                print(f"{colour_blue}Secondary:{colour_end} {colour_yellow}{secondary_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()

                print("Congratulations!!! You have rolled 6 so you advance to the next education level")
                print()
                input("Secondary - Press any key to progress...")


                #Exam Score
                secondary_score = 60
                cumilative_secondary_score = secondary_score + primary_result
                
                #Call Function University Education
                University_Education(cumilative_secondary_score)

                #Breaks out of the Nursary loop
                break

            elif (my_dice_roll == 0):

                print("Sorry you rolled 0, so you will remain where you are")

            elif (my_dice_roll == 1):

                secondary_year.append(power_arm_secondary)

                os.system("clear")
                print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Cumilative Primary Score: {primary_result}{colour_end}")
                print()
                print(f"{colour_blue}Secondary:{colour_end} {colour_yellow}{secondary_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                print("Well done!! You have passed your exams, you move one step")
                



            print()
            input("Secondary - press any key to continue...")

            #Progress to University to education if 3 stars attained
            if (len(secondary_year) >= 6 and secondary_year_counter == 6):

                #Exam Score
                secondary_score = 10
                cumilative_secondary_score = secondary_score + primary_result
                
                #Call Function University Education
                University_Education(cumilative_secondary_score)

                #Break loop
                break
            
            else:

                print()
                print("Your education ends here")
        


    #Function for Primary education
    def Primary_Education(in_nusary_result):

        #Variable
        power_arm_primary = "\U0001F4AA"
        education_primary = 6
        primary_player_bank = []
        primary_year = []
        nursary_result = in_nusary_result
        primary_score = 0
        primary_year_counter = 0

        print()
        for primary in range(education_primary):

            #Add to counter
            primary_year_counter += 1
            os.system("clear")
            print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Nusrary Exam Result: {nursary_result}{colour_end}")
            print()
            print(f"{colour_red}Primary:{colour_end} {colour_yellow}{primary_year}{colour_end}")

            my_dice_roll = process_player_roll_dice.Roll()
            

            #input("Primary - Press any key to continue...")

            if (my_dice_roll == 3):

                #Check if the bank count equals 2
                if (len(primary_player_bank) == 2):

                    #Reset year count
                    primary_year = []
                    for add_arm in range(3):
                        primary_year.append(power_arm_primary)

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Nusrary Exam Result: {nursary_result}{colour_end}")
                    print()

                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()
                    print(f"{colour_blue}Primary:{colour_end} {colour_yellow}{primary_year}{colour_end}")
                    print()
                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()

                    print(f"Congratulations!! Congratulations!! You have rolled 3 twice, so you advance to the next level")

                    input("Press any key to continue...")
                    #Call funciton to primary education

                    #Exam Score
                    primary_score = 30
                    cumilative_primary_score = primary_score + nursary_result
                    Secondary_Education(cumilative_primary_score)

                    #Brake loop
                    break
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                #Ask player if they wish to bank 
                bank_question = input("3 allows you to bank or move one step y /n: ")

                if( bank_question == "y" or bank_question == "Y"):

                    #Reset year count
                    primary_year = []

                    #Add three power arms to the nursary
                    for add_arm in range(3):
                        primary_year.append(power_arm_primary)

                    primary_player_bank.append(my_dice_roll)
                    print()
                    input(f"You currently have {len(bank_question)} in the bank. Press any key to continue...")
                

                else:
                    #Add single power arm to year
                    primary_year.append(power_arm_primary)

                    #Clear Screen
                    os.system("clear")

                    print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Nusrary Exam Result: {nursary_result}{colour_end}")
                    print()
                    print(f"{colour_blue}Primary:{colour_end} {colour_yellow}{primary_year}{colour_end}")
                    print()
                    print(f"{colour_green}You have chosen not to bank so you move one step{colour_end}")

                    

            
            elif (my_dice_roll == 6):

                #Reset year count
                primary_year = []
                
                #Add six power arm to year
                for add_arm in range(6):

                    primary_year.append(power_arm_primary)

                #Clear Screen
                os.system("clear")

                print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Nusrary Exam Result: {nursary_result}{colour_end}")
                print()
                print(f"{colour_blue}Primary:{colour_end} {colour_yellow}{primary_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                print("Congratulations!!! You have rolled 6 so you advance to the next education level")
                print()
                input("Primary - Press any key to progress...")


                #Exam Score
                primary_score = 60
                cumilative_primary_score = primary_score + nursary_result
                Secondary_Education(cumilative_primary_score)

                #Breaks out of the Nursary loop
                break

            elif (my_dice_roll == 0):

                print()
                print("Sorry you rolled 0, so you will remain where you are")

            elif (my_dice_roll == 1):

                primary_year.append(power_arm_primary)

                os.system("clear")
                print(f"{process_player_roll_dice.player_firstname} {process_player_roll_dice.player_lastname} {colour_yellow}Nusrary Exam Result: {nursary_result}{colour_end}")
                print()
                print(f"{colour_blue}Primary:{colour_end} {colour_yellow}{primary_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                print("Well done!! You have passed your exams, you move one step")
                



            print()
            input("Primary - press any key to continue...")

            #Progress to primary to education if 3 stars attained
            if (primary_year_counter == 6 and len(primary_year) >= 6):

                #Exam Score
                primary_score = 10
                cumilative_primary_score = primary_score + nursary_result
                Secondary_Education(cumilative_primary_score)
            
            else:

                print()
                print("Your education ends here")




    #Function for Nursary education
    def Nursary_Education():

        #Variables
        power_arm_nursary = "\U0001F4AA"
        education_nursary = 3
        nursary_player_bank = []
        nursary_year = []
        nursary_year_counter = 0

        nursary_exam_score = 0

        print()
        for nursary in range(education_nursary):

            os.system("clear")
            print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)
            print()
            print(f"{colour_blue}Nursary:{colour_end} {colour_yellow}{nursary_year}{colour_end}")

            #My dice roll
            my_dice_roll = process_player_roll_dice.Roll()
            print()

            #Counter years
            nursary_year_counter += 1

            if (my_dice_roll == 3):

                #Check if the bank count equals 2
                if (len(nursary_player_bank) == 2):

                    #Reset year count
                    nursary_year = []
                    for add_arm in range(3):
                        nursary_year.append(power_arm_nursary)

                    #Clear Screen
                    os.system("clear")

                    print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)
                    print()

                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()
                    print(f"{colour_blue}Nursary:{colour_end} {colour_yellow}{nursary_year}{colour_end}")
                    print()
                    print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                    print()

                    print(f"Congratulations!! Congratulations!! You have rolled 3 twice, so you advance to the next level")

                    input("Press any key to continue...")

                    #Exam score
                    nursary_exam_score = 30
                    #Call funciton to primary education
                    Primary_Education(nursary_exam_score)

                    #Brake loop
                    break

                
                
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                #Ask player if they wish to bank 
                bank_question = input("3 allows you to bank or move one step y /n: ")
                print()

                if( bank_question == "y" or bank_question == "Y"):

                    #Reset year count
                    nursary_year = []

                    #Add three power arms to the nursary
                    for add_arm in range(3):
                        nursary_year.append(power_arm_nursary)

                    nursary_player_bank.append(my_dice_roll)
                    input(f"You currently have {len(bank_question)} in the bank. Press any key to continue...")
                    '''
                    #Clear Screen
                    os.system("clear")

                    print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)
                    print()
                    print(f"{colour_blue}Nursary:{colour_end} {colour_yellow}{nursary_year}{colour_end}")
                    print()
                    '''
                    
                    

                else:
                    #Add single power arm to year
                    nursary_year.append(power_arm_nursary)

                    #Clear Screen
                    os.system("clear")

                    print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)
                    print()
                    print(f"{colour_blue}Nursary:{colour_end} {colour_yellow}{nursary_year}{colour_end}")
                    print()
                    print(f"{colour_green}You have chosen not to bank so you move one step{colour_end}")

                    

            
            elif (my_dice_roll == 6):

                #Reset year count
                nursary_year = []

                #Add six power arm to year
                for add_arm in range(6):

                    nursary_year.append(power_arm_nursary)

                #Clear Screen
                os.system("clear")

                print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)
                print()
                print(f"{colour_blue}Nursary:{colour_end} {colour_yellow}{nursary_year}{colour_end}")
                print()

                print("Congratulations!!! You have rolled 6 so you advance to the next education level")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                input("Nursary - Press any key to progress...")

                #Exam Score
                nursary_exam_score = 60


                #Call primary function
                Primary_Education(nursary_exam_score)

                #Breaks out of the Nursary loop
                break

            elif (my_dice_roll == 0):

                print("Sorry you rolled 0, so you will remain where you are")

            elif (my_dice_roll == 1):

                nursary_year.append(power_arm_nursary)

                os.system("clear")
                print(process_player_roll_dice.player_firstname, process_player_roll_dice.player_lastname)
                print()
                print(f"{colour_blue}Nursary:{colour_end} {colour_yellow}{nursary_year}{colour_end}")
                print()
                print(f"{colour_green}You rolled dice number: {my_dice_roll}{colour_end}")
                print()
                print("Well done!! You have passed your exams, you move one step to Nursary year 2")
                



            print()
            input("Nursary - press any key to continue...")

            #Progress to primary to education if 3 stars attained
            if (nursary_year_counter == 3 and len(nursary_year) >= 3):

                #Exam Score
                nursary_exam_score = 10

                Primary_Education(nursary_exam_score)

                #break loop 
                break
            
            else:

                print()
                print("Your education ends here")


    #Education start at Nusary
    Nursary_Education()
        

        
        



print(process_player_roll_dice.player_lastname, process_player_roll_dice.player_lastname,process_player_roll_dice.Roll())

School_Run()




