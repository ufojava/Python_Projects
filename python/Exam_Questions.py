'''
Synopsis: Script to create an computer aided exam

Written By: Ufuoma Okoro

Dept: HOme Office

'''

#Import Questions from Data File
from Exam_Questions_Data import Questions
import os

#Variable
question_counter = 0

#Get questions from the Exam question data
get_questions = Questions()

def Question_Answer(in_question):

    #Variables
    question_one = "q_one"
    question_two = "q_two"
    question_three = "q_three"
    question_four = "q_four"
    question_five = "q_five"
    question_six = "q_six"
    question_seven = "q_seven"
    question_eight = "q_eight"
    question_nine = "q_nine"
    question_ten = "q_ten"

    

    def Question_One():

        #Variable
        

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
            os.sys.exit()
        else:

            print("Incorrect answer")
            os.sys.exit()

    #Call the correct function for the answer function
    if (question_one):

        Question_One() 



'''
*********** Main Program Starts from here ***********

'''

for q_number in get_questions:

    #Increment counter by 1
    question_counter += 1
    os.system("clear")
    print(f"Question {question_counter}")
    print('''
    
    ''')
    print(q_number)
    print('''
    
    ''')
    '''
    if (q_number)
    annswer = input("Select answer to the question: ")
    '''
    Question_Answer("q_one")







