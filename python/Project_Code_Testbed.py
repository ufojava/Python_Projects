'''
Synopsis: This is where I will perform unit testing



'''



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
    
        


Take_Multiple_Inputs()









