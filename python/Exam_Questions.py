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




#Test
get_questions = Questions()

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
    annswer = input("Select answer to the question: ")







