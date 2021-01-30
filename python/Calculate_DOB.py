'''
Synopsis: how to calculate dat of birth

written by: Ufuoma Okoro

Dept: Home Office
'''


#Import Modules
from datetime import date
import sys



while True:

    try:

        birth_day = int(input("Input your birth day, dd: "))
        break
    except:
        print("Error!!! Enter your birth day:")

        #sys.exit("Script will terminate")


print()
birth_month = int(input("Input your birth month, mm: "))
print()
birth_year = int(input("Input your birth year, yyyy: "))

def CalcAge(in_yr,in_mth,in_day):

    #Variable
    today_date = date.today()
    days_in_yr = 365.2425

    create_age = date((in_yr), (in_mth), (in_day))

    age = int((today_date - create_age).days) / days_in_yr


    return int(age)

print(f"Your age is: {CalcAge(birth_year,birth_month,birth_day)} ")



