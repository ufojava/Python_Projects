'''
Synopsis: Script to create an computer aided exam

Written By: Ufuoma Okoro

Dept: HOme Office

'''

#Import Questions from Data File
import os
import re #Reg Expression



#Colour Pallette
colour_end = "\33[0m" #Terminate Colour
colour_green = "\33[32m" #Colour Green
colour_blue = "\33[34m" #Colour Blue
colour_red = "\33[31m" #Colour Red
colour_yellow = "\33[33m"
colour_blue_bg = "\33[44m" #Colour Blue Background
colour_violet_bg = "\33[45m"


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



def Exam_Header(in_question_number):

    #Import library
    import os

    #Clear Screen
    Clear_Screen()

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
        question_one_score += 3

        #Return score value
        return question_one_score
    else:
        #Title
        Exam_Header(1)

        print(f"{colour_red}{question_one_answer} is incorrect{colour_end}")

        #Return the current score
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
        if (answer_input == "str" and data_type == data_type_list[0]):
            
            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add a point to the score
            question_two_score += 1

            print()
            #Pause process untill key is pressed
            input(f"{colour_violet_bg}Press enter key to continue...{colour_end}")
            

        
        elif (answer_input == "int" and data_type == data_type_list[1]):
            
            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add  a point to the score
            question_two_score += 1

            print()
            #Pause process untill key is pressed
            input(f"{colour_violet_bg}Press enter key to continue...{colour_end}")

        elif (answer_input == "float" and data_type == data_type_list[2]):

            print(f"{colour_green}{answer_input} is the correct answer{colour_end}")

            #Add a point to the score
            question_two_score += 1

            #Return the question score 2
            return question_two_score

        
        

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

        #Return Score
        return question_three_score
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

        #3 Mark score for question
        question_four_score += 3
        return question_four_score

    else:

        print(f"{colour_red}{question_list} is incorrect. You should have 3 string, 2 integers and 1 float.{colour_end}")

        #3 Mark score for question
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

        sub_question_five_score = 0

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
            #Add score
            sub_question_five_score  += 3

            for month in in_list_name:

                print(f"{colour_green}{month}{colour_end}")
        
            

            #Return the score for question 5
            return sub_question_five_score 


    #Call Student function        
    question_five_score = Student_Question_Five(get_month_data[0],get_month_data[1],get_month_data[2],get_month_data[3])

    return question_five_score




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

    

    task_list = ["IF", "ELSE"]

    get_input = []



    for prompt in task_list:

        #Call Title
        Exam_Header("8")

        print(f'''
        {colour_blue_bg}Using the IF, ELIF and ELSE Conditional statements, create a code block.{colour_end}

        {colour_blue_bg}You goal is to print Success if 20 is greater than 10 else print Unsuccessful{colour_end}
        ''')

        #First line of the IF Statement
        build_code_input = input(f"{colour_yellow}{prompt}..: {colour_end} ")

        #Add input to list
        get_input.append(build_code_input)
        print()

    #Check student work

    #Stage one IF Statement
    if (get_input[0] == "if(20 > 10):" or get_input[0] == "if (20 > 10):" or get_input[0] == "IF(20 > 10):" or get_input[0] == "IF (20 > 10):"):

        #Call Title
        Exam_Header("8")

        print(f"{colour_green}{get_input[0]} is Correct{colour_end}")

        #Add one point to question 8 score
        question_eight_score += 1

        #Pause program
        print()
        input(f"{colour_violet_bg}Press enter to continue..{colour_end}")

    else:

        #Call Title
        Exam_Header("8")

        print(f"{colour_red}{get_input[0]} is incorrect{colour_end}")
    
    #Stage 2 print output statement
    if (get_input[1] == "else:" or get_input[1] == "ELSE:"):

        #Call Title
        Exam_Header("8")

        print(f"{colour_green}{get_input[1]} is correct{colour_end}")

        #Add one point to the question 8 score
        question_eight_score += 1
    else:

        #Call Title
        Exam_Header("8")

        print(f"{colour_red}{get_input[1]} is incorrect{colour_end}")



def Question_Nine():

    #University Description
    university_student_ages = [f"{colour_blue}Student one age:{colour_end} ", f"{colour_red}Student two age:{colour_end} ", f"{colour_green}Student three age:{colour_end} "]

    #Variables
    get_student_ages = []

    student_counter = 0

    aggregate_student_ages = 0

    while True:

        #Take input from student
        for student in university_student_ages:

            #Clear Screen
            Clear_Screen()

            Exam_Header("9")

            print(f"{colour_blue_bg}Goal is to get the ages of 3 students, send the total of the ages to the company accounts department{colour_end}")
            print(f"{colour_blue_bg}Enter three student ages range{colour_end} {colour_yellow}(17 and 65){colour_end}{colour_blue_bg} and send the total to accounts{colour_end}")
            print()

            input_student_ages = input(f"{student}")
            print()

            while not (input_student_ages.isdigit()):
                input_student_ages = input(f"{colour_red}Inavlid input!!{colour_end} {student}")
            
            #Convert student age digit to integer
            age_converter = int(input_student_ages)

            #Check age range
            age_range = (age_converter > 16 and age_converter < 66)

            if (age_range):

                #Add ages to list
                get_student_ages.append(age_converter)

                #Increment the counter by one
                student_counter += 1

                #Sum of all the ages
                aggregate_student_ages = sum(get_student_ages)

            else:

                Exam_Header("9")
                print(f"{colour_red}Incorrect age input: {input_student_ages}{colour_end}")
                return


        #Break While loop if counter is 3
        if (student_counter == 3):

            #Request input for the return value 
            input_student_return_value = input(f"{colour_yellow}Do you know the function return value? Enter the number:{colour_end}  ")

            #Check that input is digit
            while not (input_student_return_value.isdigit):
                print()
                input_student_return_value = input(f"{colour_red}Invalid input !!! Enter return value:{colour_end} ")
            
            #Convert the input to intger
            converted_return_value = int(input_student_return_value)

            #Evaluate agregate student ages with question return value input
            if (converted_return_value == aggregate_student_ages):

                Exam_Header("9")
                print()
                print(f"{colour_green}Correct. Your return value input was{colour_end} {colour_yellow}{converted_return_value}{colour_end} {colour_green}and aggregate student ages was{colour_end}{colour_yellow} {aggregate_student_ages}{colour_end}")
                print()
            
            else:

                Exam_Header("9")
                print()
                print(f"{colour_red}Incorrect!! Your return value{colour_end}{colour_yellow} {converted_return_value}{colour_end}{colour_red} did not match the total of the re students ages of{colour_end}{colour_yellow} {aggregate_student_ages}{colour_end}")
        break




def Question_Ten():

    Exam_Header("10")

    print(f'''
    {colour_blue_bg}Variable_one = 20{colour_end}
    {colour_blue_bg}Using the division assignment operator to divide variable_one by 5, what is the return data type{colour_end}
    Answer is:

    a. str) b. int) c. float) d. bool) e. none of the above)
    
    ''')
    student_answer = input(f"{colour_yellow}Input your asnwer:{colour_end} ")

    #Error check input

    while not (student_answer == "a" or student_answer == "b" or student_answer == "c" or student_answer == "d" or student_answer == "e"):

        Exam_Header("10")

        print(f'''
        {colour_blue_bg}Variable_one = 20{colour_end}
        {colour_blue_bg}Using the division assignment operator to divide variable_one by 5, what is the return data type{colour_end}
        Answer is:

        a. str) b. int) c. float) d. bool) e. none of the above)
        
        ''')
        print()
        student_answer = input(f"{colour_red}Invalid selection!!!{colour_end}{colour_yellow} Choose from options a to e:{colour_end} ")

    if (student_answer == "c"):

        #Get question title
        Exam_Header("10")
        print(f"{colour_green}{student_answer} is correct. The division assigment operator always returns a float data type{colour_end}")

    else:

        Exam_Header("10")
        print(f"{colour_red}{student_answer} is incorrect. The division assigment operator always returns a float data type{colour_end}")













    

def Question_Answer():

    
    

    #Variables
    def Questions():
    #Exam Questions

        #Variable
        question_counter = 0
        total_scores = 0

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
        {colour_blue_bg}Variable_one = 20{colour_end}
        {colour_blue_bg}Using the division assignment operator to divide variable_one by 5, what is the return data type{colour_end}
        '''

        #List of all questions
        list_of_questions = {"q_one_key": q_one,"q_two_key":q_two,"q_three_key":q_three,
        "q_four_key":q_four,"q_five_key":q_five,"q_six_key":q_six,"q_seven_key":q_seven,"q_eight_key":q_eight,
        "q_nine_key":q_nine,"q_ten_key":q_ten}


        #Loop through random questions
        for question in list_of_questions:

            #Clear screen
            Clear_Screen()
            #Increment queston counter
            question_counter += 1

            #Check answer
            if (question == "q_one_key"):

                

                print(list_of_questions[question])

                #Call Anser One
                total_scores += Question_One()
                
                print()
                input(f"{colour_yellow}Current Score is: {total_scores}{colour_end} {colour_violet_bg}Press any key to continue ...{colour_end}")
                

            elif (question == "q_two_key"):

                print(list_of_questions[question])

                #Call Answer Two
                total_scores += Question_Two()
                print()
                input(f"{colour_yellow}Current Score is: {total_scores}{colour_end} {colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_three_key"):

                print(list_of_questions[question])

                #Call Answer Three
                total_scores += Question_Three()
                print()
                input(f"{colour_yellow}Current Score is: {total_scores}{colour_end} {colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_four_key"):

                print(list_of_questions[question])

                #Call Answer four
                total_scores += Question_Four()
                print()
                input(f"{colour_yellow}Current Score is: {total_scores}{colour_end} {colour_violet_bg}Press any key to continue ...{colour_end}")

            elif (question == "q_five_key"):

                print(list_of_questions[question])

                #Call Answer five
                total_scores += Question_Five()
                print()
                input(f"{colour_yellow}Current Score is: {total_scores}{colour_end} {colour_violet_bg}Press any key to continue ...{colour_end}")

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







