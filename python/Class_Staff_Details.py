'''
Description: Demonstration on the use of the class object to hold company staff details

Written By: Ufuoma Okoro

Department: HOme Office

'''

#Import Libraried
import os
import json
from json import JSONEncoder

#Set colour pallete
coulour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"


#Class for staff details
class Staff_Details:

    #Initialize the input parameters
    def __init__(self,in_firstname, in_lastname,in_gender,in_department, in_year_of_service):

        self.in_firstname = in_firstname
        self.in_lastname = in_lastname
        self.in_gender = in_gender
        self.in_department = in_department
        self.in_year_of_service = in_year_of_service


#Class to encode from Python to JSON
class Encode_From_Python(JSONEncoder):

    def default(self,in_object):

        #Return the converetd object
        return in_object.__dict__



def Clear_Screen():

    os.system("clear")
    print(f'''
    {colour_green}********* STAFF DETAILS *********{coulour_end}

    ''')


#List to hold temporarily hold staff details
temp_staff_json_object = []

#Input list of questions
list_of_questions = [f"{colour_yellow}Input your firstname:{coulour_end} ",f"{colour_yellow}Input your lastname:{coulour_end} ",f"{colour_yellow}Input your gender:{coulour_end} ",f"{colour_yellow}Input your department:{coulour_end} ",f"{colour_yellow}Input number of year of service:{coulour_end} "]

#Take in staff details

for entry_count in range(3):

    #Clear Screen 
    Clear_Screen()
    get_staff_firstname = input(list_of_questions[0])
    Clear_Screen()
    get_staff_lastname = input(list_of_questions[1])
    Clear_Screen()
    get_gender = input(list_of_questions[2])
    Clear_Screen()
    get_department = input(list_of_questions[3])
    Clear_Screen()
    get_year_of_service = input(list_of_questions[4])

    #Check Year of Service for intger
    while not (get_year_of_service.isdigit()):

        get_year_of_service = input(f"{colour_red}Invalid input!!!, input must be number{coulour_end}. {list_of_questions[4]}")

    #Convert year of service to number
    convert_year_of_service = int(get_year_of_service)

    #Cerate the object
    temp_staff_json_object.append(Staff_Details(get_staff_firstname, get_staff_lastname, get_gender, get_department, get_year_of_service))

    #Encode to JSON for Loads or Dumps
    encode_list_object = Encode_From_Python().encode(temp_staff_json_object)

    print(encode_list_object)

'''
for obj in temp_staff_json_object:

    print(obj.in_firstname, obj.in_lastname, obj.in_gender, obj.in_department,obj.in_year_of_service)

'''  

#Save encodeed object to json file
with open ("comp_details.json", "w") as jsonFile:


    jsonFile.write(encode_list_object)










