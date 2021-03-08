'''
Description: DEmonstrate the use of class to hold family members

Written By: Ufuoma Okoro

Department: Home Office


'''

#Import Library
import os
import csv

#Set colour pallete
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"



#Class to process famaily data
class Family_Data:

    

    def __init__(self,in_name,in_age,in_gender):

        self.in_name = in_name
        self.in_age = in_age
        self.in_gender = in_gender

    def get_member(self):

       return f"My name is {self.in_name},I am {self.in_age} years old and I am {self.in_gender}"
       

        

#Mr First obeject fromt the class
first_member_ufuoma = Family_Data("Ufuoma", 55, "Male")

get_ufuoma_details = first_member_ufuoma.get_member()

#Print all details for Ufuoma
print(get_ufuoma_details)

#Get Ufuoma gender
get_ufuoma_gender = first_member_ufuoma.in_gender
print()
print(f"His gener is {get_ufuoma_gender}")







    


