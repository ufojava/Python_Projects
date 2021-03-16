'''
Description: Demonstration on the use of the class object to hold company staff details

Written By: Ufuoma Okoro

Department: HOme Office

'''

#Import Libraried
import os
import sys
import json
from json import JSONEncoder

#Set colour pallete
coulour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Json file name
file_name = "comp_details.json"


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


#Function to save json fomat file
def Save_Json_file(in_file,comp_obj):

    #Call encoder
    get_encoder = Encode_From_Python().encode(comp_obj)


    #Save encodeed object to json file
    with open (in_file, "w") as jsonFile:


        jsonFile.write(get_encoder)



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



Clear_Screen()
#To save of print object 
save_comp_detail = input(f"{colour_blue}Save: s, Print: p, Exit: any key: {coulour_end} ")

if (save_comp_detail == "s" or save_comp_detail == "S"):

    Clear_Screen()
    #Call save function
    Save_Json_file(file_name, temp_staff_json_object)
    print(f"{colour_green}Object has been saved to file{coulour_end}")
    

elif (save_comp_detail == "p" or save_comp_detail == "P"):

    Clear_Screen()

    for obj in temp_staff_json_object:

        print(obj.in_firstname, obj.in_lastname, obj.in_gender, obj.in_department,obj.in_year_of_service)

else:

    Clear_Screen()
    print(f"{colour_red}Program has exited !!!{coulour_end}")
    sys.exit()














