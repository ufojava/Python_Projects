'''
Synopsis: Script to create an computer aided exam

Written By: Ufuoma Okoro

Dept: HOme Office

'''

#Import Questions from Data File
import os
import re #Reg Expression
from numpy import random


#Colour Pallette
colour_end = "\33[0m" #Terminate Colour
colour_green = "\33[32m" #Colour Green
colour_blue = "\33[34m" #Colour Blue
colour_red = "\33[31m" #Colour Red
colour_yellow = "\33[33m"
colour_blue_bg = "\33[44m" #Colour Blue Background
colour_violet_bg = "\33[45m"


def Exam_Header(in_question_number):

    #Import library
    import os

    #Clear Screen
    os.system("clear")

    print(f"{colour_green}******** CODEBASE FUNDAMENTALS EXAMINATION *******{colour_end}")
    print()
    print(f"{colour_blue}Queston {in_question_number}{colour_end}")
    print()

    

def Question_One():

    
    question_one_score = 0
    Exam_Header("1")

    print()
    print(f'''
    {colour_blue_bg}How best can you describe Strings, Integers, Floats and Booleans?{colour_end}
    ''')
    
    print('''
    a. Strings, Integers and Floats can be described as Data Types
    b. String = Text, Integers = Numbers, Floats = Numbers with floating points
    c. All can be described as Data Structures
    d. None of the above
    ''')
    #Take player answer
    question_one_answer = input(f"{colour_yellow}Select correct answer: {colour_end}")

    #Test for input type - must be string
    while not (question_one_answer == "a" or question_one_answer == "b" or question_one_answer == "c" or question_one_answer == "d" ):

        question_one_answer = input(f"{colour_red}Invalid selection!!! Make Selection: {colour_end}")
    
    if (question_one_answer == "a"):

        #Title Header
        Exam_Header(1)

        print(f"{colour_green}{question_one_answer} is the correct answer{colour_end}")
        question_one_score += 1
    else:
        #Title
        Exam_Header(1)

        print(f"{colour_red}{question_one_answer} is incorrect{colour_end}")
        
    return question_one_score

    
#Question 2 Function
def Question_Two():

    question_two_score = 0

    data_type_list = ["String","Integer","Float"]

    #Variable
    # In Python, how do you call a String, Integer, Float and Boolean? 
    for data_type in data_type_list:

        #Call header function
        Exam_Header("2")

        print(f'''
        {colour_blue_bg}In Python, how do you call a String, Integer, Float: ?{colour_end} 
        ''')

        print()
        answer_input = input(f"{colour_yellow}Call the {data_type} function and press Enter:{colour_end} ")
        print()

        #Check answer
        if (answer_input == "str"):
            
            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add a point to the score
            question_two_score += 1

            print()
            #Pause process untill key is pressed
            input(f"{colour_violet_bg}Press enter key to continue...{colour_end}")
        
        elif (answer_input == "int"):
            
            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add  a point to the score
            question_two_score += 1

            print()
            #Pause process untill key is pressed
            input(f"{colour_violet_bg}Press enter key to continue...{colour_end}")

        elif (answer_input == "float"):

            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add a point to the score
            question_two_score += 1

        
        #Return question score
        #return question_two_score

def Question_Three():

    #Variable
    #In Python, what is a list?
    question_three_score = 0

    Exam_Header("3")

    print(f'''
    {colour_blue_bg}In Python, what is a list?{colour_end} 
    ''')

    print('''
    a. All the answers below
    b. Can be used to store a string
    c. Can hold an Integer value
    d. A list is used to store items in a single variable
    ''')
    print()
    question_three_answer = input(f"{colour_yellow}Make your selection:{colour_end} ")
    
    #Check for valid input
    while not (question_three_answer == "a" or question_three_answer == "b" or question_three_answer == "c" or question_three_answer == "d"):

        question_three_answer = input(f"{colour_red}Invalid selecction !!! Make your selection:{colour_end} ")
        print()

    if (question_three_answer == "a"):

        #Call header 
        Exam_Header(3)

        print(f"{colour_green}{question_three_answer} is the correct answer{colour_end}")
        question_three_score += 3
    else:

        #Call header
        Exam_Header(3)

        print(f"{colour_red}{question_three_answer} is the incorrect answer. A list can store multiples of different data types in a single varaiable{colour_end}")
    
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

    #Loop Counter Range
    input_counter = 6

    #Loop for list
    for in_list in range(input_counter):

        #Call header function
        Exam_Header("4")

        print()
        print(f'''
        {colour_blue_bg}Create a list containing 3 String, 2 Intgers and 1 Floats  press enter{colour_end}
        ''')

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

        in_value = input(f"{colour_yellow}Input lists {in_status} value: {colour_end} ")

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
    print(f"{colour_green}String: {num_of_str}, Integer {num_of_int}, Float: {num_of_float}{colour_end}")
    print()

    #Check input

    if (num_of_str == 3 and num_of_int == 2 and num_of_float == 1):

        print(f"{colour_green}{question_list} list is correct{colour_end}")
    else:

        print(f"{colour_red}{question_list} is incorrect. You should have 3 string, 2 integers and 1 float.{colour_end}")

    #3 Mark score for question
    question_four_score += 3
    return question_four_score

def Question_Five():

    #Question score
    question_five_score = 0

    Exam_Header("5")

    print(f'''
    {colour_blue_bg}Using a For Loop, print the elements in a list containing months of the year{colour_end}
    ''')


    print()
    #Using a For Loop, print the elements in a list containing months of the year
    print(f'''
    For Loop in a List
    Your code task
    1. Create a List with name: {colour_blue_bg}first_three_months{colour_end}
    2. Items in the list shold be the first three months in format: {colour_blue_bg}jan....{colour_end}

    The result will display the 3 months
    ''')

    month_data = ["list_name","first_month","second_month","third_month"]

    get_month_data = []

    #List of month
    print()

    for m_data in month_data:

        Exam_Header("5")

        print(f'''
        1. Create a List with name: {colour_blue_bg}first_three_months{colour_end}
        2. Items in the list shold be the first three months in format: {colour_blue_bg}jan....{colour_end}
        {colour_blue_bg}Using a For Loop, print the elements in a list containing months of the year{colour_end}
        ''')

        in_month_data = input(f"{colour_yellow}Enter {m_data}:{colour_end} ")
        
        get_month_data.append(in_month_data)
        print()
        print(f"{colour_green}You have input {in_month_data}{colour_end}")
        print()
        input(f"{colour_violet_bg}Press enter to continue...{colour_end}")

    def Student_Question_Five(in_list_name,mth_one,mth_two,mth_three):

        #Check for student input
        if (in_list_name != "first_three_months" or mth_one != "jan" or mth_two != "feb" or mth_three != "mar"):

            #Call Title
            Exam_Header("5")
            print(f"{colour_red}Incorrect answer. One or more of your input(s) is/are wrong.{colour_end}")

        else:


            #Create list
            in_list_name = []
            print()
            
            #Append the first month
            in_list_name.append(mth_one)
            in_list_name.append(mth_two)
            in_list_name.append(mth_three)
            print()

            #Call Title
            Exam_Header("5")
            
            print(f"{colour_green}Correct{colour_end}")
            for month in in_list_name:

                print(f"{colour_green}{month}{colour_end}")
        
            #Add score
            #question_five_score += 3

        #Return the score for question 5
        return question_five_score


    #Call Student function        
    Student_Question_Five(get_month_data[0],get_month_data[1],get_month_data[2],get_month_data[3])




def Question_Six():

    #Question score
    question_six_score = 0

    input_values = ["Input First Number", "Input Operator", "Input Second Number"]

    #Student entered values
    received_values = []

    def Proc_Complex_Variable(in_first_param, in_operator, in_second_param):

        #Convert string numbers to integers
        convert_first_param = int(in_first_param)
        convert_second_param = int(in_second_param)

        #Check and assign operator
        if (in_operator == "<"):

            complex_variable = (convert_first_param < convert_second_param)

        elif (in_operator == ">"):

            complex_variable = (convert_first_param > convert_second_param)

        elif (in_operator == ">="):

            complex_variable = (convert_first_param >= convert_second_param)

        elif (in_operator == "<="):

            complex_variable = (convert_first_param <= convert_second_param)


        #Solve true and false 
        if (complex_variable):

            #Call Title
            Exam_Header("6")

            print(f"{colour_green}True. Your answer is correct{colour_end}")
            #question_six_score += 3

        else:

            #Call Title
            Exam_Header("6")
            print(f"{colour_red}False. You answer is incorrect{colour_end}")

        #Return score
        return question_six_score

    

    for value in input_values:

        Exam_Header("6")

        print(f'''
        {colour_blue_bg}Create a complex variable that prints true:{colour_end}

        {colour_blue_bg}1. You will input your first digit{colour_end}
        {colour_blue_bg}2. Enter an operator >, <, >= or <={colour_end}
        {colour_blue_bg}3. Now you final number{colour_end}
        {colour_blue_bg}The return has to be true get a correct result.{colour_end}
        ''')

        get_value = input(f"{colour_yellow}{value}: {colour_end}")

        #Add value to the Received List
        received_values.append(get_value)
    
    #Set expression to check Operator
    chk_operator = (received_values[1] == ">" or received_values[1] == "<" or received_values[1] == ">=" or received_values[1] == "<=")

    if (received_values[0].isdigit() and received_values[2].isdigit() and chk_operator):

         #Call function six
        Proc_Complex_Variable(received_values[0],received_values[1],received_values[2])

    else:

        #Call Title
        Exam_Header("6")

        print(f"{colour_red}Incorrect input !!!, You entered {received_values}{colour_end}")




def Question_Seven():

    #Question severn score
    question_seven_score = 0

    #Call Title
    Exam_Header("7")

    #Solve the Arithmetical problems:
    print(f"{colour_blue_bg}1. Using variable assignment add 5 to existing variable. Answer should be 10{colour_end} ")
    print()

    try:

        in_add_assign, in_add_int = input(f"{colour_yellow}Input Add assignment and number:{colour_end} ").split()

        add_variable = 5

        if ( in_add_assign == "+="):

            add_variable += int(in_add_int)

            #Check total which should equal 10
            if (add_variable == 10):

                #Call Title
                Exam_Header("7")
            
                print(f"{colour_green}Correct Add Assignment: {add_variable}{colour_end}")

                #Add to one point to score
                question_seven_score += 1

                #Pause program
                print()
                input(f"{colour_violet_bg}Press enter to continue..{colour_end}")

            else:

                #Call Title
                Exam_Header("7")

                print(f"{colour_red}{add_variable} is incorrect{colour_end}")

                print()
                input(f"{colour_violet_bg}Press enter to continue..{colour_end}")
    except:
        pass
    
    #Call Title
    Exam_Header("7")

    print(f"{colour_blue_bg}Using assignment multiply 10 and you answer should be 190:{colour_end} ")
    print()

    try:
    
        in_multiply_assign, in_multiply_int = input(f"{colour_yellow}input Multiply assigment and number:{colour_end} ").split()

        #Multiply Variable
        multiply_variable = 19

        if ( in_multiply_assign == "*="):

            multiply_variable *= int(in_multiply_int)

            if (multiply_variable == 190):

                #Call Title
                Exam_Header("7")

                print(f"{colour_green}Correct multiply assigment: {multiply_variable}{colour_end}")

                #Add one point to the seven score
                question_seven_score += 1


            else:
                
                #Call Title
                Exam_Header("7")

                print(f"{colour_red}{in_multiply_assign} is incorrect{colour_end}")
    except:
        pass

    

def Question_Eight():

    #Question eight score
    question_eight_score = 0

    #First line of the IF Statement
    in_if_statement_first_line = input(f"{colour_yellow}Input the first line of your IF statement:{colour_end} ")
    print()

    #Else condition if not ment
    in_else_statement_line = input(f"{colour_yellow}Input ELSE statement line:{colour_end} ")


    #Check student work

    #Stage one IF Statement
    if (in_if_statement_first_line == "if(20 > 10):" or in_if_statement_first_line == "if (20 > 10):"):

        print()
        print(f"{colour_green}{in_if_statement_first_line} is Correct{colour_end}")

        #Add one point to question 8 score
        question_eight_score += 1

    else:

        print()
        print(f"{colour_red}{in_if_statement_first_line} is incorrect{colour_end}")
    
    #Stage 2 print output statement
    if (in_else_statement_line.startswith("else:")):

        print()
        print(f"{colour_green}{in_else_statement_line} is correct{colour_end}")

        #Add one point to the question 8 score
        question_eight_score += 1
    else:

        print(f"{colour_red}{in_else_statement_line} is incorrect{colour_end}")



def Question_Nine():

    #University Description
    university_student_ages = [f"{colour_blue}Student one age:{colour_end} ", f"{colour_red}Student two age:{colour_end} ", f"{colour_green}Student three age:{colour_end} "]

    #Variables
    student_one = 0
    student_two = 0
    student_three = 0

    student_counter = 0

    aggregate_student_ages = 0

    while True:

        #Take input from student
        for student in university_student_ages:

            #Clear Screen
            os.system("clear")
            print(f"{colour_blue_bg}Enter student age between 17 and 65{colour_end}")
            print()
            print(f"{colour_blue_bg}Variable for total number of students:{colour_end} {colour_yellow}aggregate_student_ages{colour_end}")
            print()
            print(f"{colour_blue_bg}Variable for student one:{colour_end} {colour_yellow}student_one{colour_end}")
            print(f"{colour_blue_bg}Variable for student two:{colour_end} {colour_yellow}student_two{colour_end}")
            print(f"{colour_blue_bg}Variable for student three:{colour_end} {colour_yellow}student_three{colour_end}")
            print()

            input_age = int(input(f"{student}"))
            print()
            input_assignment = input(f"Input assigment command to add {student} to {colour_yellow}aggregate_student_ages: {colour_end}")

            #Check command
            if (input_assignment == "aggregate_student_ages += student_one" or input_assignment == "aggregate_student_ages += student_two" or input_assignment == "aggregate_student_ages += student_three"):



                while not (input_age > 0 and input_age < 65):
                    input_age = int(input(f"{student}"))
            

                if (student == university_student_ages[0]):

                    #Convert input to intgers
                    convert_student_one = int(input_age)

                    #Assign age to student one
                    student_one = convert_student_one

                    #Increment student counter
                    student_counter += 1

                    #Add age number to the total
                    aggregate_student_ages += student_one
                
                elif (student == university_student_ages[1]):

                    #Convert input to intgers
                    convert_student_two = int(input_age)

                    #Assign age to student one
                    student_two = convert_student_two

                    #Increment student counter
                    student_counter += 1

                    #Add age number to the total
                    aggregate_student_ages += student_two

                elif (student == university_student_ages[2]):

                    #Convert input to intgers
                    convert_student_three = int(input_age)

                    #Assign age to student one
                    student_three = convert_student_three

                    #Increment student counter
                    student_counter += 1

                    #Add age number to the total
                    aggregate_student_ages += student_three

            else:

                print()
                print(f"{colour_red}Incorrect Assignement Operator for{colour_end} {student}")
                print()
                input(f"{colour_violet_bg}Press any key to continue...{colour_end}")

        #Break While loop if counter is 3
        if (student_counter == 3):

            print()
            print(f"{colour_green}The total number of student ages is: {aggregate_student_ages}{colour_end}") 
            break




def Question_Ten():

    #Import Library
    import os

    #Colour palet
    colour_end = "\33[0m"
    colour_red = "\33[31m"
    colour_green = "\33[32m"
    colour_yellow = "\33[33m"
    colour_blue = "\33[34m"
    colour_blue_bg = "\33[44m"
    colour_violet_bg = "\33[45m"

    print(f'''
    {colour_blue_bg}1. Input your first Integer, press enter and input the second intger for testing your code block{colour_end}
    {colour_blue_bg}2. The variable holding the processed variables is:{colour_end} {colour_violet_bg}accounting_total{colour_end}
    {colour_blue_bg}3. What command do you use to send{colour_end}{colour_violet_bg}accounting_total{colour_end} {colour_blue_bg} when function is called?{colour_end}

    ''')











    

def Question_Answer():

    
    total_scores = 0

    #Variables
    def Questions():
    #Exam Questions

        #Variable
        question_counter = 0

        q_one = f'''
        {colour_blue_bg}How best can you describe Strings, Integers, Floats and Booleans?{colour_end}
        '''
        q_two = f'''
        {colour_blue_bg}In Python, how do you call a String, Integer, Float: ?{colour_end} 
        '''

        q_three = f'''
        {colour_blue_bg}In Python, what is a list?{colour_end} 
        '''

        q_four = f'''
        {colour_blue_bg}Create a list containing 3 String, 2 Intgers and 1 Floats  press enter{colour_end}
        '''

        q_five = f'''
        {colour_blue_bg}Using a For Loop, print the elements in a list containing months of the year{colour_end}
        '''

        q_six = f'''
        {colour_blue_bg}Create a complex variable that prints true:{colour_end}

        {colour_blue_bg}1. You will input your first digit{colour_end}
        {colour_blue_bg}2. Enter an operator >, <, >= or <={colour_end}
        {colour_blue_bg}3. Now you final number{colour_end}
        {colour_blue_bg}The return has to be true get a correct result.{colour_end}
        '''

        q_seven = f'''
        {colour_blue_bg}Solve the variable assignment problems:{colour_end}
        '''

        q_eight = f'''
        {colour_blue_bg}Using the IF, ELIF and ELSE Conditional statements, create a code block.{colour_end}

        {colour_blue_bg}You goal is to print Success if 20 is greater than 10 else print Unsuccessful{colour_end}
        '''

        q_nine = f'''
        {colour_blue_bg}You company accountant requires you to create a script to add up the ages of their three students{colour_end}
        {colour_blue_bg}What Assignment Operator will you use to send the added up students ages?{colour_end}
        '''

        q_ten = f'''
        {colour_blue_bg}A fucntions is created to produce a accounting figures which is part of a software for the accounting dpeartment{colour_end}
        {colour_blue_bg}Call the function by assinging to a variable{colour_end}
        '''

        #List of all questions
        list_of_questions = {"q_one_key": q_one,"q_two_key":q_two,"q_three_key":q_three,
        "q_four_key":q_four,"q_five_key":q_five,"q_six_key":q_six,"q_seven_key":q_seven,"q_eight_key":q_eight,
        "q_nine_key":q_nine,"q_ten_key":q_ten}


        #Loop through random questions
        for question in list_of_questions:

            #Clear screen
            os.system("clear")
            #Increment queston counter
            question_counter += 1

            #Check answer
            if (question == "q_one_key"):

                

                print(list_of_questions[question])

                #Call Anser One
                Question_One()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_two_key"):

                print(list_of_questions[question])

                #Call Answer Two
                Question_Two()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_three_key"):

                print(list_of_questions[question])

                #Call Answer Three
                Question_Three()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_four_key"):

                print(list_of_questions[question])

                #Call Answer four
                Question_Four()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_five_key"):

                print(list_of_questions[question])

                #Call Answer five
                Question_Five()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_six_key"):

                print(list_of_questions[question])

                #Call Answer six
                Question_Six()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_seven_key"):

                print(list_of_questions[question])

                #Call Answer Seven
                Question_Seven()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_eight_key"):

                print(list_of_questions[question])

                #Call Answer Eight
                Question_Eight()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_nine_key"):

                print(list_of_questions[question])

                #Call Answer Nine
                Question_Nine()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_ten_key"):

                print(list_of_questions[question])

                #Call Answer Ten
                Question_Ten()
                print()
                input(f"{colour_violet_bg}Press any key to continue ...{colour_end}")

    Questions()

            












'''
*********** Main Program Starts from here ***********
'''
Question_Answer()







