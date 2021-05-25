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

        display_slow.write(letter)
        display_slow.flush()
        time.sleep(0.05)

    print(''' 
    ''')




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

for attendee in range(len(raffle_numbers)):

    #GCU Banner
    GCU_Banner()

    
    #Input attendee name
    attendee_name = input("Input name: ")

    #Generate number from list
    get_random_number = random.choice(raffle_numbers)

    #Remove allocated number from the list
    raffle_numbers.remove(get_random_number)

    


    Slow_Display(f"{attendee_name}, {get_random_number}")



    #Create an obeject with the name and random number
    create_attendee_obj = Raffle_Attendees(attendee_name, get_random_number)

    #Return object from class appended to the raffle list
    raffle_draw_list.append(create_attendee_obj.Attendee_Draw_Details())

    print(''' 
    ''')

    input(f"{colour_violet_bg}Press Enter key to enter next player{colour_end}")

    print(''' 
    ''')

GCU_Banner()


#Using Pandas to create dataframe
raffle_cols = ["Name","Draw Number"]

raffle_dataFrame = pd.DataFrame(raffle_draw_list,columns=raffle_cols)




#Print Raffle Draw List
print(raffle_dataFrame.to_string(index=False))









    








