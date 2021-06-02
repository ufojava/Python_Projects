'''
Description: Tombola Raffle Draw

Written By: Ufuoma Okoro
'''

#Library 
import os
import sys
from pyfiglet import figlet_format
import time
import random
import pandas as pd

#Colour palette
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Background colour
colour_blue_bg = "\33[44m"
colour_violet_bg = "\33[45m"

#Function to slow character release
def Slow_Display(in_word):

    #Define slow print
    display_slow = os.sys.stdout

    for letter in in_word:

        display_slow.write(f"{colour_green}{letter}{colour_end}")
        display_slow.flush()
        time.sleep(0.05)

    return ""

#Function to speak
def Speak_Text(in_text):

    if (os.name == "posix"):

        os.system(f"say {in_text}")

    elif (os.name == "Linux"):

        os.system(f"espeak {in_text}")

    




#Function to create GCU Banner with clear screen
def GCU_Banner():

    if (os.name == "nt"):

        #Windows based system
        os.sytem("cls")
        print(f'''{colour_yellow}{figlet_format("Marina Tombola")}{colour_end}''')

    else:

        #Linux based system
        os.system("clear")
        print(f'''{colour_yellow}{figlet_format("Marina Tombola")}{colour_end}''')


#Funciton list the numbers
def Generate_Raffle_Number(in_no_attendees):

    attendees_adjustment = (in_no_attendees + 1)

    gen_raffle_list = list(range(1,attendees_adjustment))

    return gen_raffle_list




class Raffle_Attendees:

    def __init__(self,in_name,in_number):

        self.in_name = in_name
        self.in_number = in_number

    def Attendee_Draw_Details(self):

        temp_attendee_list = []

        temp_attendee_list.append(self.in_name)
        temp_attendee_list.append(self.in_number)

        return temp_attendee_list

    
    #Save Results
    def Save_Raffle_Results(self,in_name,in_number):

        pass


raffle_draw_list = []


#Header
GCU_Banner()



while True:

    try:

        #Main program starts here
        number_of_attendees = int(input("Input the number of attendees: "))

        break

    except:

        print()
        input(f"{colour_red}Invalid entry!!! Press Enter key to continue{colour_end}")

        


#Create raffle numbers
raffle_numbers = Generate_Raffle_Number(number_of_attendees)

#Raffer Number picker (Winner)
raffle_pick_winner = random.choice(raffle_numbers)

#Monitor name entered
name_checker = []

for attendee in range(len(raffle_numbers)):
    
    #GCU Banner
    GCU_Banner()

    while True:

        try:

            GCU_Banner()
            #Input attendee name
            attendee_name = input("Input name: ").capitalize()

            if not (attendee_name in name_checker):

                break

            else:


                print(f'''

                {colour_yellow}{name_checker}{colour_end}

                ''')
                
                input(f"{colour_red}Attendee name exist!!! Press Enter key to enter another name{colour_end}")
        except:

            pass
    
    #Add name to the list
    name_checker.append(attendee_name)


    #Generate number from list
    get_random_number = random.choice(raffle_numbers)

    #Remove allocated number from the list
    raffle_numbers.remove(get_random_number)

    
    #Test display
    attendee_name_raffle_number = f"{attendee_name}  {get_random_number}"

    #Clear screen and display the banner
    GCU_Banner()

   
    print(figlet_format(attendee_name_raffle_number,font="banner"))
    

   
    #Create an obeject with the name and random number
    create_attendee_obj = Raffle_Attendees(attendee_name, get_random_number)

    #Return object from class appended to the raffle list
    raffle_draw_list.append(create_attendee_obj.Attendee_Draw_Details())

    print(''' 
    ''')

    input(f"{colour_violet_bg}Press Enter key to enter next player{colour_end}")

    print(''' 
    ''')

input(f"{colour_yellow}Press Enter Key to reveal Winning Number{colour_end}")

#Inset GCU Header
GCU_Banner()

print(f'''{figlet_format("...and the winning number is:",font="digital")}''')
print()

display_winning_number = f"{str(raffle_pick_winner)}"

Slow_Display(figlet_format(display_winning_number,font="banner"))
print()


input(f"{colour_yellow}Press Enter Key to display the winner{colour_end}")

GCU_Banner()

for winner in raffle_draw_list:

    if (winner[1] == raffle_pick_winner):

        reveal_winner = f"{winner[0], winner[1]}"

        temp_list = []
        #Add name
        temp_list.append(winner[0])
        temp_list.append(str(winner[1]))

        




        print(f'''{figlet_format("And the winner is.....",font="digital")}''')


        ''' 
        ******** WINNER DISPLAY NOTES ********
        The line below:
        1. Format the list usint the Join function the list (Temp_list)
        2. Then use the Slow display function to display
        
        '''
        Slow_Display(figlet_format(" ".join(temp_list),font="banner"))





print()

input("Press enter to contine")

''' 
Need to add the wining number and title to the lists
1. Raffle list is: raffle_draw_list
2. Raffle number is: raffle_pick_winner

'''

def Add_Winning_Num_To_List(in_winning_number):

    raffle_title = "Winning Number"

    winner_list = [raffle_title,in_winning_number]

    return winner_list

#Create winner object
create_winner_number_obj = Add_Winning_Num_To_List(raffle_pick_winner)

#Append to the Raffle list
raffle_draw_list.append(create_winner_number_obj)



''' 
This section will faciliate the saving of the output file to csv file
Also have the user enter the file name to make for flexibility
A funciton will be used to implement this

'''

#Funciton to Display and or save record
def Display_Save_Results(in_results):

    #Import Library
    import pandas as pd

    #Create dataframe columns
    dataframe_columns = ["Name","Draw"]


    #Create dataframe
    result_data = pd.DataFrame(in_results,columns=dataframe_columns)

    #Clear banner
    GCU_Banner()

    def Report_Menu():

        #Report Menu
        print(''' 
        
        1. Display Results
        2. Save Results
        3. Exit Program

        ''')

        #Iput Option

        while True:

            try:

                in_report_option = input("Input an option: ")

                if (in_report_option == "1" or in_report_option == "2" or in_report_option == "3"):

                    break
                else:

                    input(f"{colour_red}Invalid option!!! Press Enter Key to try again{colour_end}")
            except:

                pass

        #Retun option

        if (in_report_option == "1"):

            return "1"

        elif (in_report_option == "2"):

            return "2"

        elif (in_report_option == "3"):

            return "3"



    #Execute option
    if (Report_Menu() == "1"):

        #Clear Screen
        GCU_Banner()

        #Print raw data for testing purpose
        print(result_data.to_string(index=False))

    elif (Report_Menu() == "2"):

        pass

    elif (Report_Menu() == "3"):

        pass


#Call funciton
Display_Save_Results(raffle_draw_list)











    








