'''
Description: Staff HR System that will hold

1. Class to hold Staff Firstname, Lastname and Age
2. Return the Staff Firstname, Lastname and Age

3. Child Class that will inherit Staff Details
4. Method allocate Department for the Staff member
5. Method to assign the staff salary

6. Method to save object to csv file
7. Report to retreive staff information

'''

#Import Library
import os
import sys
import pandas as pd
import csv
import pyfiglet as figlet_format
import time


#Set colour pallette
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

#Background Colour
colour_blue_bg = "\33[44m"
colour_violet_bg = "\33[45m"

def Clear_Screen():

    #Variables
    windows_computers =  (os.name == "nt")
    linux_computers = (os.name == "Linux")
    mac_computers = (os.name =="posix")

    if (windows_computers):

        os.system("cls")

    elif (linux_computers or mac_computers):

        os.system("clear")




#Class for Staff Personal Details

class Staff_Personal_Details:

    #Initialise Staff Personal Details
    def __init__(self,staff_firstname,staff_lastname,staff_age):

        self.staff_firstname = staff_firstname
        self.staff_lastname = staff_lastname
        self.staff_age = staff_age

    #Return Staff Personal Details
    def Get_Staff_Details(self):

        #Staff Member Object
        staff_member_object = []

        #Add object to list object
        staff_member_object.append(self.staff_firstname)
        staff_member_object.append(self.staff_lastname)
        staff_member_object.append(self.staff_age)


        return staff_member_object

class Staff_Dept_Salary(Staff_Personal_Details):

    #Initilialise all properties
    def __init__(self, staff_firstname, staff_lastname, staff_age):

        #Inherit Personal details
        super().__init__(staff_firstname, staff_lastname, staff_age)


    def Create_Dept_Salary(self):

        #Clear Screen
        Clear_Screen()

        dept_salary_obj = []
        staff_department = ""

        #Append input to list
        dept_salary_obj.append(self.staff_firstname)
        dept_salary_obj.append(self.staff_lastname)
        dept_salary_obj.append(self.staff_age)

        print(f'''
        Staff Departments

        1. Information Technology
        2. Human Resources
        3. Clinical
        4. Facilities
        
        ''')


        #Enter the Staff Department
        while True:

            try:
                print()
                in_staff_department = input("Input staff department: ")

                if (in_staff_department == "1" or in_staff_department == "2", in_staff_department == "3" or in_staff_department == "4"):

                    break

                else:

                    input(f"{colour_red}Invalid input!!! Enter the number agaist the department. Press Enter to try again.{colour_end}")

            except:

                pass

        #Process Department input

        if (in_staff_department == "1"):

            staff_department = "Information Technology"

        elif (in_staff_department == "2"):

            staff_department = "Human Resources"

        elif (in_staff_department == "3"):

            staff_department = "Clinical"

        elif (in_staff_department == "4"):

            staff_department = "Facilities"



        
        #Enter the Salary
        while True:

            try:
                print()

                in_staff_salary = float(input(f"Input salary - {colour_yellow}1000.0, 1500.0, 2000.0, 2500.0:{colour_end}  "))

                if (in_staff_salary == 1000.0 or in_staff_salary == 1500.0 or in_staff_salary == 2000.0 or in_staff_salary == 2500.0):

                    break
                else:

                    input(f"{colour_red}Invalid salary input!! Press Enter to try again{colour_end}")

            except:

                pass




        #Append Department and Salary input to list
        dept_salary_obj.append(staff_department)
        dept_salary_obj.append(in_staff_salary)

        #Return the List
        return dept_salary_obj




#Input Staff Details

while True:

    #Clear Screen
    Clear_Screen()

    try:

        in_personal_details = Staff_Personal_Details(input("Input firstname: ").capitalize(), input("Input lastname: ").capitalize(), int(input("Input age: ")))

        break

    except:

        input(f"{colour_red}Input for age is incorrect!!! Can only be a number. Press Enter key to continue...{colour_end}")

        pass


#Input Staff Details


get_staff_details = in_personal_details.Get_Staff_Details()

for staff_obj in get_staff_details:

    print(staff_obj)





