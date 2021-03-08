'''
Description: Using classes to create staff objects

Written By: Ufuoma Okoro

'''
#Import Library
import os
import csv

#Create colour pallate

colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"


#Mt First class
'''

class Company_Staff:

    def __init__(self,in_firstname,in_lastname,in_age,in_staff_number,in_dept,yrs_of_service):

        self.in_firstname = in_firstname
        self.in_lastname = in_lastname
        self.in_age = in_age
        self.in_staff_number = in_staff_number
        self.in_dept = in_dept
        self.yrs_of_service = yrs_of_service



    def calc_bonus(self):

        #Age to calculate and return bonus entitlement
        get_age = self.in_age
        get_yrs_of_service = self.yrs_of_service

        #Bonus classification
        bonus_higher_rate = 1500
        bonus_middle_rate = 750
        bonus_lower_rate = 350
        bonus_nil = 0

        #Staff classification
        staff_higher_entitlement = ((get_age >= 25 and get_age <= 65) and (get_yrs_of_service > 10))
        staff_middle_entitlement = ((get_age >= 18 and get_age <= 65) and (get_yrs_of_service >= 5 and get_yrs_of_service <= 9))
        staff_lower_entitlement = ((get_age >= 18 and get_age <= 65) and (get_yrs_of_service <= 4))


        #Bonus calculation
        if(staff_higher_entitlement):

           

            return bonus_higher_rate #Return higher rate bonus

        elif (staff_middle_entitlement):


            return bonus_middle_rate #Return middle rate bonus

        elif (staff_lower_entitlement):


            return bonus_lower_rate #Return lower rate bonus

        else:

            return bonus_nil


top_staff_member = Company_Staff("Ufuoma","Okoro",66,"001","EUX",5)

#Print Bonus
print(f"{colour_green}{top_staff_member.in_firstname} {top_staff_member.in_lastname}{colour_end} {colour_yellow}{top_staff_member.calc_bonus()}{colour_end}")

'''

#Test how to work with JSON files


def Test_Save_Object():

    import json

    def dumps_json():

        #My Object

        my_first_Object = {

        "name": "Ufuoma",
        "age": 54,
        "Salary": 25000.0

        }

        #Convert to JSON
        my_converted_json = json.dumps(my_first_Object)


        temp_list = [my_first_Object]

        my_second_object = {

        "name": "Ovie",
        "age": 55,
        "Salary": 45000.0

        }

        temp_list.append(my_second_object)

        #print(temp_list)


        for details in temp_list:

            print(details)
    
    dumps_json()

    def loads_json():

        # My String Object

        my_loads_object = '{"name":"Ufuoma","age":55,"Salary":25000.0}'

        #Laod file
        load_my_json_object = json.loads(my_loads_object)

        print(load_my_json_object)

    #loads_json()

    








Test_Save_Object()

