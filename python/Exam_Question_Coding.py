'''
Description: Practical Coding Examination

Problem:

The Head of Department in your company have been given instructions to award bonuses to members of staff who 10 days or less in the month of January
The bonus is 50.00 pounds

Instructions:

1. Create a variable that takes in name from the keyboard
2. Create another variable that takes in number of days absense
3. Build a function that takes in both above vairables (Name and Absense)
4. Create a new variable an assign it Absense converted to an Integer
5. Use If statement to check if the Absense is less than or equal to 10
6. print Name and you are entitled to 50 pounds
7. Else Print Name has not been awarded 50 pounds
7. Call your function and pass you variables into your function

'''


in_staff_name = input("Input your name: ")
print()
in_staff_absence = input("Input your absense figures for the month of January: ")


def Process_Bonus(in_name,in_absence):

    convert_absence = int(in_absence)

    if (convert_absence <= 10):

        print(f"{in_name} is awarded 50 Pounds")
    else:
        print(f"{in_name} has not been awarded 50 Pounds")

#Call function

Process_Bonus(in_staff_name, in_staff_absence)

