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

    def convert_obj(self,in_object):

        #Return the converetd object
        return in_object.__dict__







