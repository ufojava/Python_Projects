'''
Synopsis: This is where I will perform unit testing



'''


#Fuction to clear screen
def Clear_Screen():

    #Import Library
    import os

    #Apply appropirate clear screen
    if (os.name == "nt"):

        #Apply Windows clear screen
        os.system("cls")

    else:

        #Apply Linux or Mac OS
        os.system("clear")



#Funciton to match numbers in 2 sets of numbers
def print_match():

    list_one = [10,23,44,14]
    list_two = [10,14,8,6]

    list_one_set = set(list_one)
    list_two_set = set(list_two)



    match_numbers = len(set.intersection(list_one_set,list_two_set))

    number_match = (match_numbers >= 1)

    if (number_match):

        print(f"{match_numbers} matches found !!")

    else:

        print("No number match")


#Call function
#print_match()

#Function to slow print word
def Print_Slowly():

    import os
    import time
    from numpy import random

    print_slow = os.sys.stdout
    read_greeting = open("Greeting_Words.txt")


    def Process_Word(in_word):

        for letter in in_word:
            
            print_slow.write(letter)
            print_slow.flush()
            time.sleep(0.1)
        return ""
    
    def Spacer (in_num_space):

        for space in range(int(in_num_space)):
            print()

'''
    #Take in player name
    name_question = "What is your name: "
    lotto_player_name = input(f"{Process_Word(name_question)} ")
    Spacer(2)
    #Process_Word(name_question)
    time.sleep(.2)
    Process_Word(f"Hello {lotto_player_name}")
    Spacer(2)
    
    how_you_doing_description = "How are you doing: "
    how_you_doing_question = input(f"{Process_Word(how_you_doing_description)}")

    if (how_you_doing_question in read_greeting.read()):
        Spacer(2)
        Process_Word(f"It is good you are going {how_you_doing_question}")
        Spacer(2)
        Process_Word("Are you ready to win some money? ")
        #Close greening file
        read_greeting.close()
    else:
        Spacer(2)
        Process_Word("Oh! not so good :( but I hope you win some money...")
        
        #Close greentings file
        read_greeting.close()

    
    Spacer(2)

#Print_Slowly()

#Function to test prize money
def Calc_Prize_Money_Test(in_number_match_test):

    num_match_one = (in_number_match_test == 1)
    num_match_two = (in_number_match_test == 2)

    if (num_match_one):
        print("One number match £10.00")
    elif(num_match_two):
        print("Two number match £20.00")
    

#Calc_Prize_Money_Test(2)
'''
'''
Creating a GUI for application




import random


list_of_questions = ["q_one", "q_two", "q_three", "q_four", "q_five", "q_six", "q_seven", "q_eight", "q_nine", "q_ten"]

random.shuffle(list_of_questions)

print(list_of_questions)
'''

#Create list which contains string an integer values and count the number of integers

question_list = []


input_counter = 6
import re

num_of_int = 0
num_of_str = 0
num_of_float = 0

'''
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

    in_value = input(f"Input {in_status} list value : ")

    if (in_value.isdigit()):

    
        convert_input_int = int(in_value)

        question_list.append(convert_input_int)
        num_of_int += 1

    elif (re.findall("[.]",in_value)):

        convert_input_float = float(in_value)

        question_list.append(convert_input_float)
        num_of_float += 1

        
    else:
        question_list.append(in_value)
        num_of_str += 1




    #Appened input to list
    

    #Need to count the number of integers, str and floats

    for dataType in question_list:

        if (isinstance(dataType,str)):
            num_of_str += 1
        if (isinstance(dataType,int)):
            num_of_int += 1
        if (isinstance(dataType,float)):
            num_of_float += 1

print(question_list)
print(f"String: {num_of_str}, Integer: {num_of_int}, Float: {num_of_float}")
'''

#Use of dictionary

def Test_Question():

    set_q_one = '''This is the first'''
    set_q_two = "This is the second"
    set_q_three = "This is the third"


    my_questions = {"set_q_one_key": set_q_one,"set_q_two_key":set_q_two,"set_q_three_key":set_q_three}

    for quest in my_questions:
        
        if (quest == "set_q_one_key"):
            print(my_questions[quest])

#Test_Question()

def Data_Type():

    str_variable = "String"
    int_variable = 5
    float_variable = 2.0

    all_data_types = [str_variable,int_variable,float_variable]

    for d_type in all_data_types:

        print(type(d_type))

        input("Press any key to continue..")

#Data_Type()
def take_input():

    #Test creation of a variable that need to be passed into a funciton

    first_complex_variable = input("Input your first parameter for your complex variable: ")
    print()
    conditional_operator = input("Input your operator, <, >, >=, <=: ")
    print()
    second_complex_variable = input("Input your second parameter for your complex variable: ")

def Return_Complex_Variable(in_first_param, in_operator,in_second_param):

    convert_first_param = int(in_first_param)
    convert_second_param = int(in_second_param)

    #Check for operator
    if (in_operator == "<"):

        complex_expression = (convert_first_param < convert_second_param)

    elif (in_operator == ">"):


        complex_expression = (convert_first_param > convert_second_param)

    elif (in_operator == ">="):

        complex_expression = (convert_first_param >= convert_second_param)

    elif (in_operator == "<="):

        complex_expression = (convert_first_param <= convert_second_param)

    elif (in_operator == "="):

        complex_expression = (convert_first_param == convert_second_param)

    
    

    if(complex_expression):
        print("Condtion is true")
    else:
        print("Conditions is false")

#Return_Complex_Variable(first_complex_variable,conditional_operator,second_complex_variable)

#Function to take 2 inputs from the terminal
def Take_Multiple_Inputs():
    import os
    #The sume of 2 variables

    try:

        add_assign, in_int = input("Add assignment and integer: ").split()

        add_variable = 5

        if (add_assign == "+="):

            add_variable += int(in_int)

            print(add_variable)
    except:

        pass
    print("Test completed")
    

#Take_Multiple_Inputs()

#Function create an if statement for student

def IF_Statement_Builder():

    

    in_if_statement_first_line = input("input the complete line of your IF statement: ")
    print()
    

    in_if_statement_else = input("Input your ELSE statement line: ")
    print()
    in_do_somthing_if_statement_false = input("Input message if condition is not ment: ")

    #Process student input information
    if (in_if_statement_first_line == "if(20 > 10):" or in_if_statement_first_line == "if (20 > 10):"):

        print("first line check passed")
    else:
        print("First ine check incorrect")
    
    

#IF_Statement_Builder() 

#Create questions contained within a lis a loop through each one an assign the value to a variable

def Question_Module():


    question_list = ["What is your name? ", "How old are you? ","Your city of birth? "]

    player_name = " "
    player_age = " "
    player_birth_city = " "

    for player_detail in question_list:

        if (question_list[0] == player_detail):
            player_name = player_detail

        elif (question_list[1] == player_detail):
            player_age = player_detail

        elif (question_list[2] == player_detail):
            player_birth_city = player_detail

    #Print the details
    print(player_name)
    print(player_age)
    print(player_birth_city)

#Question_Module()

def Question_Ten_Template():

    import os

    #Colour
    colour_end = "\33[0m"
    colour_blue = "\33[34m"
    colour_green = "\33[32m"
    colour_red = "\33[31m"
    colour_yellow = "\33[33m"

    player_question_description = [f"{colour_blue}Player 1 jersey number:{colour_end} ", f"{colour_red}Player 2 jersey number:{colour_end} ", f"{colour_green}Player 3 jersey number:{colour_end} "]

    player_one = 0
    player_two = 0
    player_three = 0

    player_counter = 0

    while True:

        for player in player_question_description:

            os.system("clear")
            take_input = input(f"{player}")

            if (player == player_question_description[0]):

                #Convert input
                convert_player_one = int(take_input)
                player_one = convert_player_one

                #Increase counter
                player_counter += 1

            elif (player == player_question_description[1]):
                
                #Conver input
                convert_player_two = int(take_input)
                player_two = convert_player_two

                #Increase counter
                player_counter += 1


            elif (player == player_question_description[2]):

                #Conver input
                convert_player_three = int(take_input)
                player_three = convert_player_three

                #Increase counter
                player_counter += 1

        if (player_counter == 3):
            break
    
    os.system("clear")
    print(f"{colour_blue}Player 1 jersey number: {player_one}{colour_end}")
    print()
    print(f"{colour_red}Player 2 jersey number: {player_two}{colour_end}")
    print()
    print(f"{colour_green}Player 3 jersey number: {player_three}{colour_end}")
    print()


#Question_Ten_Template()

def Question_Nine():

    import os

    #Colour Pallette
    colour_end = "\33[0m" #Terminate Colour
    colour_green = "\33[32m" #Colour Green
    colour_blue = "\33[34m" #Colour Blue
    colour_red = "\33[31m" #Colour Red
    colour_yellow = "\33[33m"
    colour_blue_bg = "\33[44m" #Colour Blue Background
    colour_violet_bg = "\33[45m"

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
            input_assignment = input(f"Input assigment command to add {student} to {colour_yellow}aggregate_student_ages:{colour_end} ")

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

                print(f"{colour_red}Incorrect Assignement Operator for{colour_end} {student}")
                print()
                input(f"{colour_violet_bg}Press any key to continue...{colour_end}")

        #Break While loop if counter is 3
        if (student_counter == 3):

            print()
            print(f"{colour_green}The total number of student ages is: {aggregate_student_ages}{colour_end}") 
            break

#Question_Nine()


def Question_Two():

    import os

    colour_end = "\33[0m"
    colour_blue = "\33[34m"
    colour_green = "\33[32m"
    colour_red = "\33[31m"
    colour_yellow = "\33[33m"

    question_two_score = 0

    data_type_list = ["String","Integer","Float"]

    #Variable
    # In Python, how do you call a String, Integer, Float and Boolean? 
    for data_type in data_type_list:

        os.system("clear")

        answer_input = input(f"{colour_yellow}Call the {data_type} function and press Enter:{colour_end} ")
        print()

        #Check answer
        if (answer_input == "str"):
            
            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add a point to the score
            question_two_score += 1
        
        elif (answer_input == "int"):
            
            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add  a point to the score
            question_two_score += 1

        elif (answer_input == "float"):

            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add a point to the score
            question_two_score += 1
        
        #Return question score
        #return question_two_score

#Question_Two()

def Test_Input():

    #Test for Integeer entry

    in_test_interger = input("Input number: ")

    if (in_test_interger.isdigit()):

        print("This is a number")
    
    else:

        print("Is not digit")


#Test_Input()

aggregate_age_list = [10,5,8,7]

sum_of_list = sum(aggregate_age_list)

print(sum_of_list)


























