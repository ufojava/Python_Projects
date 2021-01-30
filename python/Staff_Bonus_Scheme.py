'''
Synopsis: New Class implementation of bonus sceme

Written By: Ufuoma Okoro

Dept: Home Office

'''


#Import modules
import os
from datetime import date



#Variables
staff_list = []
today_date = date.today()
staff_no_genetator = 0
input_record_number  = 0

#Class - Staff template
class Staff_Records:

    def __init__(self,in_staff_no,in_first_name,in_last_name,in_age,in_yr_of_service,in_department,in_salary):
        #Initiate variables
        self.in_staff_no = in_staff_no
        self.in_first_name = in_first_name
        self.in_last_name = in_last_name
        self.in_age = in_age
        self.in_yr_of_service = in_yr_of_service
        self.in_department = in_department
        self.in_salary = in_salary

    def get_staff_no(self):
        return self.in_staff_no
    
    def get_firstname(self):
        return self.in_first_name

    def get_lastname(self):
        return self.in_last_name

    def get_age(self):
        return self.in_age

    def get_yr_of_srvice(self):
        return self.in_yr_of_service

    def get_department(self):
        return self.in_department

    def get_salary(self):
        return self.in_salary

    #Calculate salary increase
    def cal_sal_increase(self,in_yr, in_sal):

        #Incerment Rate
        lower_band_increase_rate = (2.5 / 100)
        middle_band_increase_rate = (3.75 / 100) 
        higher_band_increment_rate = (4.25 / 100)

        #Year of service classification
        yos_lower_classification = (in_yr <= 3)
        yos_middle_classificaiton = (in_yr >= 4 and in_yr <= 9)
        yos_higher_classificaiton = (in_yr >= 10)


        #Apply increment to salary
        if (yos_lower_classification):

            new_salary = (lower_band_increase_rate * in_sal) + in_sal
            return new_salary

        elif (yos_middle_classificaiton):

            new_salary = (middle_band_increase_rate * in_sal) + in_sal
            return new_salary

        elif (yos_higher_classificaiton):

            new_salary = (higher_band_increment_rate * in_sal) + in_sal
            return new_salary





os.system("Clear")


record_entry_counter = int(input("Number of record(s) you wish to input: "))
if (record_entry_counter >= 1 and record_entry_counter <= 5):

        for count in range(record_entry_counter):

            input_record_number += 1
            staff_no_genetator += 1

            #Take Staff Member Record
            os.system("Clear") #Clear Screen
            print(f"Record number: {input_record_number}")
            staff_no = int(staff_no_genetator)
            print()
            print(f"Staff No: {staff_no}")
            print()
            firstname = input("Firstname: ")
            print()
            lastname = input("Lastname: ")
            print()
            age = int(input("Age: "))
            print()
            year_of_Service = int(input("Year(s) of Service: "))
            print()
            department = input("Department: ")
            print()
            salary = int(input("Salary: "))


            #Pass input in the class        
            staff_details = Staff_Records(staff_no,firstname,lastname,age,year_of_Service,department,salary)

            #Process input
            staff_no = staff_details.in_staff_no
            firstname = staff_details.in_first_name.capitalize()
            lastname = staff_details.in_last_name.capitalize()
            age = staff_details.in_age
            year_of_Service = staff_details.in_yr_of_service
            department = staff_details.in_department.upper()
            salary = staff_details.in_salary

            #Append the processed information into list
            staff_list.append(Staff_Records(staff_no,firstname,lastname,age,year_of_Service,department,salary))

else:


    print("Number not in range!!!!")

os.system("Clear") #Clear screen for the print
display_salary_increase = input("Do you wish to display increment? y/n: ")
print()



#Loop through Object list Salary increase
if (display_salary_increase == "y" or display_salary_increase == "Y"):

    for member in staff_list:

        print(member.in_staff_no,member.in_first_name,member.in_last_name,member.in_age,member.in_yr_of_service,member.in_department,member.in_salary,staff_details.cal_sal_increase(member.in_yr_of_service, member.in_salary))

elif (display_salary_increase == "n" or display_salary_increase == "N"):

    os.system("Clear")
    search_name = input("Enter firstname: ")

    for member in staff_list:

        if (member.in_first_name == search_name):

            print(member.in_staff_no,member.in_first_name,member.in_last_name,member.in_age,member.in_yr_of_service,member.in_department,member.in_salary)


else:
    os.system("Clear")
    print("You have chosen no print output")



