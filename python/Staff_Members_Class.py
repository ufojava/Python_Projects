'''
Synopsis: Script to create staff members using class

Written By: Ufo Okoro

Dept: Home Office

'''

#Create Class - Staff Members
class StaffMember:

    #Initilize Varaibles
    def __init__(self,first_name,last_name,age,salary):

        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.salary = float(salary)
    

    #Get Staff Details
    def process_staff_details(self):

        #Staff Salary Increment
        staff_Increment = 0

        #Staff Increment Salaries
        category_A = (self.age <= 45 and self.salary <= 30000)
        category_B = ((self.age > 45 and self.age <= 60) and (self.salary > 30000.00 and self.salary <= 90000.00))

        if(category_A):
            staff_Increment = 1500.00
            return staff_Increment + self.salary
        elif(category_B):
            staff_Increment = 3000.00
            return staff_Increment + self.salary
        else:
            return self.salary

    def staff_entitled_promo(self,in_new_salary):

        #Variable
        promotion_eligibility = " "
        if (in_new_salary <= 30000):
            promotion_eligibility = "Eligible"

            return promotion_eligibility
        else:
             promotion_eligibility = "Not Eligible"

             return promotion_eligibility




        
#Main Program
take_first_name = input("Enter your firstname: ")
print()
take_last_name = input("Enter your lastnane: ")
print()
take_age = input("Enter your age: ")
print()
take_salary = input("Enter your gross salary: ")
print()

staff_details = StaffMember(take_first_name,take_last_name,take_age,take_salary)

print(f"{staff_details.first_name.capitalize()} {staff_details.last_name.capitalize()}: £{staff_details.process_staff_details()}")
print()

#Check for promotion eligibility
print(f"You are {staff_details.staff_entitled_promo(staff_details.process_staff_details())} for promotion")
