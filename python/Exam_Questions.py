'''
Synopsis: Script to create an computer aided exam

Written By: Ufuoma Okoro

Dept: HOme Office

'''

#Import Questions from Data File
import os
import re #Reg Expression
from numpy import random

#Variable
question_counter = 0

    

def Question_One():

    #Variable
    #How best can you describe Strings, Integers, Floats and Booleans?
    question_one_score = 0
    

    print('''
    a. Strings, Integers and Floats can be described as Data Types
    b. String = Text, Integers = Numbers, Floats = Numbers with floating points
    c. All can be described as Data Structures
    d. None of the above
    ''')
    #Take player answer
    question_one_answer = input("Select correct answer: ")

    #Test for input type - must be string
    while not (question_one_answer == "a" or question_one_answer == "b" or question_one_answer == "c" or question_one_answer == "d" ):

        question_one_answer = input("Invalid selection!!! Make Selection: ")
    
    if (question_one_answer == "a"):

        print("Correct answer")
        question_one_score += 1
    else:

        print("Incorrect answer")
        
    return question_one_score

    
#Question 2 Function
def Question_Two():

    question_two_score = 0

    #Variable
    # In Python, how do you call a String, Integer, Float and Boolean? 
    print('''
    Intput your answer when prompted.
    ''')
    str_answer_input = input("Call the string function and press Enter: ")
    print()
    int_answer_input = input("Call the Integer function and press Enter: ")
    print()
    float_answer_input = input("Call the float function and press Enter: ")
    print()

    #Check answer
    if (str_answer_input == "str"):
        
        print("Correct!!")

        #Add a point to the score
        question_two_score += 1

    else:
        print("Incorrect!! You call a String function with a str()")
    
    if (int_answer_input == "int"):
        
        print("Correct!!")

        #Add  a point to the score
        question_two_score += 1
    else:
        print("Incorrect You call an Integer function with a int()")

    if (float_answer_input == "float"):

        print("Correct!!")

        #Add a point to the score
        question_two_score += 1
    else:
        print("Incorrect you call a float function with a float()")
    
    #Return question score
    return question_two_score

def Question_Three():

    #Variable
    #In Python, what is a list?
    question_three_score = 0

    print('''
    a. All the answers below
    b. Can be used to store a string
    c. Can hold an Integer value
    d. A list is used to store items in a single variable
    ''')
    print()
    question_three_answer = input("Make your selection: ")
    
    #Check for valid input
    while not (question_three_answer == "a" or question_three_answer == "b" or question_three_answer == "c" or question_three_answer == "d"):

        print("Invalid selection !!! Make a selection")
        print()

        if (question_three_answer == "a"):

            print("Correct !!")
            question_three_score += 3
        else:

            print("Incorrect answer. A list can store multiples of different data types in a single varaiable")
    
    #Return Score
    return question_three_score

def Question_Four():

    #Create a list containing 3 String, 2 Integers and 1 Float press enter

    #Variables
    question_four_score = 0
    question_list = []

    #Count for data type
    num_of_int = 0
    num_of_str = 0
    num_of_float = 0


    print('''
    Input value and press enter
    ''')
    input_counter = 6

    #Loop for list
    for in_list in range(input_counter):

        if (in_list == 0):
            in_status = "first"
        elif (in_list == 1):
            in_status = "second"
        elif (in_list == 2):
            in_status = "third"
        elif (in_list == 3):
            in_status = "fourth"
        elif (in_list == 4):
            in_status = "fifth"
        elif (in_list == 5):
            in_status = "sixth"

        in_value = input(f"Input list value {in_status}: ")

        #Check for digital input
        if (in_value.isdigit()):
            
            #Convert the string digit to an integer
            convert_input_int = int(in_value)

            #Numnber of data type
            num_of_int += 1

            #Append value to list
            question_list.append(convert_input_int)

        #Reg Exp search for float
        elif (re.findall("[.]",in_value)):
            convert_input_float = float(in_value)

            #Add number to data type
            num_of_float += 1

            #Append input to the list
            question_list.append(convert_input_float)

        else:

            #Append string
            num_of_str += 1
            question_list.append(in_value)

    print()
    print(f"String: {num_of_str}, Integer {num_of_int}, Float: {num_of_float}")

    #Check input

    if (num_of_str == 3 and num_of_int == 2 and num_of_float == 1):

        print("Corret !!!")
    else:

        print("Incorrect!!!")

    #3 Mark score for question
    question_four_score += 3
    return question_four_score

def Question_Five():

    print('''
    Place Holder Question Five
    ''')

def Question_Six():

    print('''
    Place Holder Question Six
    ''')

def Question_Seven():

    print('''
    Place Holder Question Seven
    ''')

def Question_Eight():

    print('''
    Place Holder Question Eight
    ''')

def Question_Nine():

    print('''
    Place Holder Question Nine
    ''')

def Question_Ten():

    print('''
    Place Holder Question Ten
    ''')









    

def Question_Answer():

    
    total_scores = 0

    #Variables
    def Questions():
    #Exam Questions

        q_one = '''
        How best can you describe Strings, Integers, Floats and Booleans?
        '''
        q_two = '''
        In Python, how do you call a String, Integer, Float: ? 
        '''

        q_three = '''
        In Python, what is a list? 
        '''

        q_four = '''
        Create a list containing 3 String, 2 Intgers and 1 Floats  press enter
        '''

        q_five = '''
        Using a For Loop, print the elements in a list containing months of the year
        '''

        q_six = '''
        How do you best describe a variable ?
        '''

        q_seven = '''
        Create 3 variable that stores the string, Integer and Float values
        '''

        q_eight = '''
        Using the IF, ELIF and ELSE Conditional statements, create a code block that will:
        1. Check a variable value of 20 and print "This is 20"
        2. Check another variable value of 30 and print "This is 30"
        3. Else print "This is neither 20 or 30"
        '''

        q_nine = '''
        Create a function that will return the sum of 2 numbers
        '''

        q_ten = '''
        Create a Function that will print "This is my first function"
        Call the function by assinging to a variable
        '''

        #List of all questions
        list_of_questions = {"q_one_key": q_one,"q_two_key":q_two,"q_three_key":q_three,
        "q_four_key":q_four,"q_five_key":q_five,"q_six_key":q_six,"q_seven_key":q_seven,"q_eight_key":q_eight,
        "q_nine_key":q_nine,"q_ten_key":q_ten}


        #Loop through random questions
        for question in list_of_questions:

            #Clear screen
            os.system("clear")
        

            #Check answer
            if (question == "q_one_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Anser One
                Question_One()
                input("Press any key to continue ...")

            elif (question == "q_two_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer Two
                Question_Two()
                input("Press any key to continue ...")

            elif (question == "q_three_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer Three
                Question_Three()
                input("Press any key to continue ...")

            elif (question == "q_four_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer four
                Question_Four()
                input("Press any key to continue ...")

            elif (question == "q_five_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer five
                Question_Five()
                input("Press any key to continue ...")

            elif (question == "q_six_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer six
                Question_Six()
                input("Press any key to continue ...")

            elif (question == "q_seven_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer Seven
                Question_Seven()
                input("Press any key to continue ...")

            elif (question == "q_eight_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer Eight
                Question_Eight()
                input("Press any key to continue ...")

            elif (question == "q_nine_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer Nine
                Question_Nine()
                input("Press any key to continue ...")

            elif (question == "Q_ten_key"):

                print(list_of_questions[question])
                print('''
                Answer question
                ''')

                #Call Answer Ten
                Question_Ten()
                input("Press any key to continue ...")

    Questions()

            












'''
*********** Main Program Starts from here ***********
'''
Question_Answer()







