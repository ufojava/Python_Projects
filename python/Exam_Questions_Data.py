'''
Module Questions Data

'''
#Import modules
import random

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
    Create a complex variable to print:
    1. true if the condition is me
    2. else print false
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

    #list_of_questions = [q_one, q_two, q_three, q_four, q_five, q_six, q_seven, q_eight, q_nine, q_ten]

    list_of_questions = {

        "q_one_key": q_one,
        "q_two_key": q_two,
        "q_three_key": q_three,
        "q_four_key": q_four,
        "q_five_key": q_five,
        "q_six_key": q_six,
        "q_seven_key": q_seven,
        "q_eight_key": q_eight,
        "q_nine_key": q_nine,
        "q_ten_key": q_ten 
    }


    #Shuffle list

    #random.shuffle(list_of_questions)
    return list_of_questions

    

    #return list_of_questions

        

