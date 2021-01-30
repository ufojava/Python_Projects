'''
Sysnopsis: Program to determine the tax bracket of staff members

Class: Get_Person_Details - Firstname, Lastname, Age, Department and Gross Salary

Class: 
    with 3 Tax categories A, B and C

'''

class Get_Staff_members:

    #Initialize parameters
    def __init__(self,staff_firstname,staff_lastname,staff_age,staff_department,staff_gross_salary):

        self.staff_firstname = staff_firstname
        self.staff_lastname = staff_lastname
        self.staff_age = int(staff_age)
        self.staff_department = staff_department
        self.staff_gross_salary = float(staff_gross_salary)

    #Return Staff Tax Code
    def staff_tax_code(self):

        #Variable for Tax Code

        tax_code = " "
        
        #Category
        tax_code_0701 = (self.staff_gross_salary <= 25000.00 and self.staff_age < 65)
        tax_code_0702 = ((self.staff_gross_salary > 25000.00) and (self.staff_gross_salary <= 90000.00) and self.staff_age < 65)
        tax_code_0703 = (self.staff_gross_salary > 90000.00 and self.staff_age < 65)
        tax_code_0765 = "0765"

        #Allocate Tax Code
        if(tax_code_0701):
            tax_code = "0701"
            return tax_code

        elif(tax_code_0702):
            tax_code = "0702"
            return tax_code

        elif(tax_code_0703):
            tax_code = "0703"
            return tax_code
        else:
            return tax_code_0765

    #Calculate Staff Tax
    def staff_tax_calc(self,in_tax_code):

        #Variable

        #Tax Band
        tax_lower_band = 0.22
        tax_middle_band = 0.40
        tax_higher_band = 0.50
        tax_allowance = 10000.00
        pension_age = 65
        
        #Staff Tax Calcuations
       
        salary_after_tax = 0.0
        cumulative_monthly_salary = 0.0
        month_of_year = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        last_mth_of_year = month_of_year[-1]
        
    
        
        #Check Valid Tax
        if (in_tax_code == "0701" or in_tax_code == "0702" or in_tax_code == "0703" or in_tax_code == "0765"):



            #Tax Calculation - lower
            if (in_tax_code == "0701" and self.staff_age < pension_age):

                end_of_yr_tax_adjustment = ((self.staff_gross_salary / 12) * tax_lower_band) 

                for mth in month_of_year:

                    if (cumulative_monthly_salary > tax_allowance):

                        if (mth == last_mth_of_year): #Last month of the year adjustments

                           mth_salary_after_tax = ((self.staff_gross_salary / 12) - (((self.staff_gross_salary /12) * tax_lower_band) * 2))
                           cumulative_monthly_salary += mth_salary_after_tax
                           print(f"{mth}'s deduction includes a tax adjustment for the year")

                        else:
                            mth_salary_after_tax = (self.staff_gross_salary / 12) - ((self.staff_gross_salary /12) * tax_lower_band)
                            cumulative_monthly_salary +=  mth_salary_after_tax

                        #Print cumulitive gross salary + tax
                        print(f"{mth} salary after tax: {round(mth_salary_after_tax,2)}")
                        print(f"{mth} cumulative salary: {round(cumulative_monthly_salary,2)}")
                        print()

                    elif (cumulative_monthly_salary < tax_allowance):

                        #Month Salary Variable
                        mth_salary_after_tax = (self.staff_gross_salary / 12)

                        #Add monthly total to cumulative total
                        cumulative_monthly_salary += mth_salary_after_tax

                        #Print cumulative gross salary - tax
                        print()
                        print(f"{mth} salary after tax: {round(mth_salary_after_tax,2)}")
                        print(f"{mth} cumulative salary: {round(cumulative_monthly_salary,2)}")
                        print()
                #Return Salary
                salary_after_tax = cumulative_monthly_salary - end_of_yr_tax_adjustment #May tax is not removed
                return salary_after_tax



            #Tax Calculation - middle
            elif (in_tax_code == "0702" and self.staff_age < pension_age):

                end_of_yr_tax_adjustment = ((self.staff_gross_salary / 12) * tax_middle_band) 

                for mth in month_of_year:

                    if (cumulative_monthly_salary > tax_allowance):

                        if (mth == last_mth_of_year):

                            mth_salary_after_tax = ((self.staff_gross_salary / 12) - (((self.staff_gross_salary /12) * tax_middle_band) * 2))
                            cumulative_monthly_salary += mth_salary_after_tax
                            print(f"{mth}'s deduction includes a tax adjustment for the year")
                        
                        else:

                            mth_salary_after_tax = (self.staff_gross_salary / 12) - ((self.staff_gross_salary /12) * tax_middle_band)
                            cumulative_monthly_salary +=  mth_salary_after_tax

                            #Print the monthly salary after tax
                            print(f"{mth} salary after tax: {round(mth_salary_after_tax,2)}")

                            #Print cumulitive gross salary + tax
                            print(f"{mth} cumulative salary: {round(cumulative_monthly_salary,2)}")
                            print()
                        

                    elif (cumulative_monthly_salary < tax_allowance):
                        cumulative_monthly_salary += (self.staff_gross_salary / 12)

                        #Print cumulative gross salary - tax
                        print()
                        print(f"{mth} cumulative salary: {round(cumulative_monthly_salary,2)}")
                        print()
                
                
                #Return Salary
                salary_after_tax = cumulative_monthly_salary - end_of_yr_tax_adjustment #May tax is not removed
                return salary_after_tax

            

            #Tax Calculation - higher
            elif (in_tax_code == "0703" and self.staff_age < pension_age):

                end_of_yr_tax_adjustment = ((self.staff_gross_salary / 12) * tax_higher_band) 

                for mth in month_of_year:


                    mth_salary_after_tax = (self.staff_gross_salary / 12) - ((self.staff_gross_salary /12) * tax_higher_band)
                        
                    cumulative_monthly_salary += mth_salary_after_tax

                    #Print monthly salary after tax
                    print(f"{mth} salary after tax: {round(mth_salary_after_tax,2)}")

                    #Print cumulitive gross salary + tax
                    print(f"{mth} cumulative salary: {round(cumulative_monthly_salary,2)}")
                    print()

                salary_after_tax = cumulative_monthly_salary

                return salary_after_tax

            #Tax Calculation - pension age
            elif (in_tax_code == "0765" and self.staff_age >= pension_age):

                for mth in month_of_year:


                    mth_salary_after_tax = (self.staff_gross_salary / 12)
                    cumulative_monthly_salary += mth_salary_after_tax

                    #Print monthly salary
                    print(f"{mth} salary:            {round(mth_salary_after_tax,2)}")
                    print(f"{mth} cumulative salary: {round(cumulative_monthly_salary,2)}")

                return cumulative_monthly_salary

        else:

            print(f"{in_tax_code} is an invalid tax code")


#Main Program Starts here

take_first_name = input("Enter your firstname: ")
print()
take_last_name = input("Enter your lastname: ")
print()
take_age = input("Enter your age: ")
print()
take_staff_dept = input("Your department: ")
print()
take_gross_salary = input("Input your gross salary: ")

#Call Class - Get Staff Members
retreive_tax_code = Get_Staff_members(take_first_name,take_last_name,take_age,take_staff_dept,take_gross_salary)

print(f"Your tax code is {retreive_tax_code.staff_tax_code()}")

#Round to 2 decimal places
final_tax_calc = round(retreive_tax_code.staff_tax_calc(retreive_tax_code.staff_tax_code()),2)

#Get tax calculation


#print(f"You Salary after tax is: {retreive_tax_code.staff_tax_calc(retreive_tax_code.staff_tax_code())}")
print(f"You Salary after tax is: {final_tax_calc}")
    

