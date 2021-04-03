'''
Description:: Script to hold personal details

'''

#Import libraries
import os


#Create colour pallete
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"

class Family_Members:

    def __init__(self,firstname,lastname,age):

        self.firstname = firstname
        self.lastname = lastname
        self.age = int(age)


list_of_family_members = []

os.system("clear")

while True:

    try:


        number_of_entries = int(input("Enter the number of family members: "))
        break
    except:
        pass


for member in range(number_of_entries):

    os.system("clear")

    family_input = Family_Members(input("Firstname: ").capitalize(), input("Lastname: ").capitalize(), input("Age: "))

    list_of_family_members.append(family_input)




#List all the family members in the list
os.system("clear")
for member in list_of_family_members:

    print(member.firstname,member.lastname,member.age)


