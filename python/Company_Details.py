'''
Description: Staff members of the company using class and class inheritance

1. Class to take in:
Firstname
Lastname
Age

2. Class to:
Department
Designation
Salary
Performance level 1 - 5

Method to award bonus to deserving staff
Bonus
Salary increase


Method to save ouput
Save to CSV File
Use Pandas to display
Option to search for report
Pull full reports

'''

#Import Library
import os
import csv
import sys
import pandas as pd
import datetime


#Colour Palette
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Colour Background
colour_blue_bg = "\33[44m"
colour_violet_bg = "\33[45m"


''' 
Class to take in staff:
Firstname
Lastname
Age

'''

class Staff_Member:

    def __init__(self,firstname,lastname,age):

        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def Technilogy_Group (self):

        return True




''' 
Class for staff:
Department
Salary
'''

class Staff_Department(Staff_Member):

    def __init__(self,firstname,lastname,age,salary, department):
        
        super().__init__(firstname,lastname,age)

        #Child initialization
        self.salary = salary
        self.department = department

    
    def Process_Staff_Department(self):

        if (self.department == "Infra_Ops" and self.salary <= 35000.0):

            return "Instrastructure Engineer"

        elif (self.department == "Infra_Ops" and (self.salary >35000.0 and self.salary <= 45000.00)):

            return "Senior Insfreastructure Engineer"

        elif (self.department == "Infra_Ops" and self.salary > 45000.00):

            return "Technology Architech"



        



    




staff_one = Staff_Department("Ufuoma", "Okoro", 55, 25000.0, "Infra_Ops")

print(staff_one.firstname,staff_one.lastname,staff_one.age,staff_one.salary,staff_one.department,staff_one.Process_Staff_Department())






    



