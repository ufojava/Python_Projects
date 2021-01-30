'''
Synopsis: Use class ot create object for the Ejarome Okoro Family

Next step:

(1) Create object from every entry and store in List
(2) Export to JSON or CSV
(3) Retreive the Records

Written By: Ufuoma Okoro

Dept: Home Office

'''

#Import module
from datetime import date, timedelta
import os




#Class to construct the object
class FamilyMember:

    #Initialize the attributes
    def __init__(self,firstname,lastname,gender,in_fam_pos,in_age):

        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.gender = gender.upper()
        self.in_fam_pos = in_fam_pos
        self.in_age = in_age
    
    #Check the fmember postion in the family
    def Member_Position(self):

       famliy_position = self.in_fam_pos

       max_fam_members = 8

       #Categorise Family Position code

       fam_pos1 = "POS1"
       fam_pos2 = "POS2"
       fam_pos3 = "POS3"
       fam_pos4 = "POS4"
       fam_pos5 = "POS5"
       fam_pos6 = "POS6"
       fam_pos7 = "POS7"
       fam_pos8 = "POS8"

       for _ in range(max_fam_members):

            if (famliy_position == 1):
                return fam_pos1

            elif (famliy_position == 2):
                 return fam_pos2

            elif (famliy_position == 3):
                 return fam_pos3

            elif (famliy_position == 4):
                return fam_pos4
            
            elif (famliy_position == 5):
                return fam_pos5

            elif (famliy_position == 6):
                return fam_pos6

            elif (famliy_position == 7):
                return fam_pos7
            
            elif (famliy_position == 8):
                return fam_pos8

    def Calculate_Age(self,in_date_of_birth):

        #Variables
        days_in_year = 365.2425
        today_date = date.today()

        #Calculate age
        family_member_age = int((today_date - in_date_of_birth).days / days_in_year)

        return family_member_age

        



    
#Class to convert date input
class DOB_Convert:

    #Method to convert the input
    def convert_dob_input(self,in_number_description):


        #Variables
        local_day_description = "Enter the day of your birth: "
        local_mth_description = "Enter the month of your birth: "
        local_yr_description = "Enter the year of your birth: "
        

        if (in_number_description == local_yr_description):

        
            #While loop in combination of try except to receive integers
            while True:

                try:

                    in_numb_yr = int(input(f"{in_number_description} "))

                    while True:
                        if (in_numb_yr <1000):
                            print()
                            print("Enter Valid Year yyyy!!!")
                            print()
                            in_numb_yr = int(input(f"{in_number_description}: "))

                        else:
                            
                            return in_numb_yr
        

                except:
                    print(f"This prompt only accepts integers!!!")

                
                else:
                    break
        if (in_number_description == local_mth_description):

        

            while True:

                try:
                    print()
                    in_numb_mth = int(input(f"{in_number_description} "))

                    #Check if the entry is between 1 and 12 digits
                    while True:
                        if(in_numb_mth < 1 or in_numb_mth > 12):

                            print("Birth month out of range, enter month between 1 and 12 !!!")
                            print()
                            in_numb_mth = int(input(f"{in_number_description}: "))

                        else:

                            return in_numb_mth
                        

                except:
                    print(f"This prompt only accept integers!!!")

                else:
                    break


        if (in_number_description == local_day_description):

            while True:

                try:
                    in_numb_day = int(input(f"{in_number_description} "))

                    #Check input digit to ensure valid day of the month
                    while True:

                    
                        if(in_numb_day < 1 or in_numb_day > 31):
                            print()
                            print("Invalid day of the month!!")
                            print()
                            in_numb_day = int(input(f"{in_number_description} "))
                            print()
                        else:
                            return in_numb_day


                except:
                    print(f"This prompt only accepts integers!!!")

                else:
                    break
        else:
            print(f"No Matching description!!! {in_number_description} Local: {local_yr_description}")

       


#Function to create single line space
def Spacer():
    print()

#Function to clear screen
def ClearScreen():
    os.system("clear")

#Variable
in_num_describ_day = "Enter the day of your birth: "
in_num_describe_mth = "Enter the month of your birth: "
in_num_describe_yr = "Enter the year of your birth: "

family_object_list = []


#Main Program Starts here

entry_counter = 0

while (entry_counter != 3):
    ClearScreen()

    #Increase counter by 1 for the While loop
    entry_counter += 1
    print(f"Entry No: {entry_counter}")

    #Enter Family member name
    in_firstname = input("Enter your firstname: ")
    Spacer()
    in_lastname = input("Enter your lastname: ")
    Spacer()

    #Enter Date of Birth
    '''
    ********* Date of Birth Process ********

    This Section uses the Calculate_Age Class to convert the integer.
    The class method convert_dob_input also erro checks the input for: Digits for year, month and day

    '''

    in_date_of_birth_yr = DOB_Convert().convert_dob_input(in_num_describe_yr)
    Spacer()
    in_date_of_birth_mth = DOB_Convert().convert_dob_input(in_num_describe_mth)
    Spacer()
    in_date_of_birth_day = DOB_Convert().convert_dob_input(in_num_describ_day)
    Spacer()

    #Create the date of birth after the conversion
    family_date_of_birth = date(in_date_of_birth_yr,in_date_of_birth_mth,in_date_of_birth_day)

    #Input family seniority position
    in_fam_poistion = input("Enter postion in the family: ")
    Spacer()
    in_gender = input("Enter your gender, M/F: ")
    in_gender_chk = (in_gender == "F" or in_gender == "f" or in_gender == "M" or in_gender == "m")
    Spacer()


    #Error check the gender input
    while (not in_gender_chk):
        repeat_in_gender = input("Inavlid input!! enter M / F: ")
        in_gender_chk = repeat_in_gender #Assign repeat input to gender
        in_gender = repeat_in_gender #Update gender


    
    #Process input Data with the Class Object template
    family_member = FamilyMember(in_firstname,in_lastname,in_gender,in_fam_poistion,family_date_of_birth) #Call class FamilyMember abd enter input

    #Calculate the age from the dat input
    get_age = family_member.Calculate_Age(family_date_of_birth)

    
    
    
    #Create list / Array from each object
    family_object_list.append(FamilyMember(in_firstname,in_lastname,in_gender,in_fam_poistion,get_age))



#List the Array / List of all the entries

ClearScreen() #Clear Screen to reveal report

for famObj in family_object_list:

    print(famObj.firstname,famObj.lastname,famObj.gender,famObj.in_fam_pos,famObj.in_age)

