'''
Module Questions Data

'''
#Import modules
import random

#Variables

def Questions():
    #Exam Questions

    q_one = '''
    If a salesman sold 5,000 cars in the year 2020 and has been informed that his target for 2021 has
    been increased by 3.75 percent
    How may cars will the salesman be expected to sell in 2021? 
    '''
    q_two = '''
    A client of yours had invested 3 Million pounds in portfolio which is currently paying £2.25 per share.
    There is an expectation that the share price will sold at £3.75 when the sctock lists on the London Stock exchange.
    How much will your client be worth after the London listing?
    '''

    q_three = '''
    The company Hong-Kong office will be shutting down due to the world pandemic.
    Hong-Kong sales represents 25 percent of total company sales (£45,000,000.00)
    Due to the closure of the office, how much is the company expected to make in
    the current year?  
    '''

    q_four = '''
    One of your companys clients has a portfolio worth £3 Million.
    You sold to the client 15 Percent of his total stock value.
    How much did you sell?
    '''

    q_five = '''
    Your comapny with a valuation of £45 Million has offered you stock options worth 0.75 Percent.
    How much is you stock worth?
    '''

    q_six = '''
    A child pair of shoes cost £15.99.
    The value-add tax is 17.5 pecent.
    How much will you need to present to the teller to complete the sale?
    '''

    q_seven = '''
    Your company total staff sick record in 2020 equaled to 10 staff out of a total of 55.
    Calculate the percentage staff loss in the year 2020? 
    '''

    q_eight = '''
    The price of oil in 2020 stood at $34 per barrel.
    A shortagte in the current year as triggered a price increase to $42 per barrel.
    Calculate the percentage price increase.
    '''

    q_nine = '''
    Your gross salary is £35,000.00 per anum.
    The tax is calculated at 22 Percent.
    You are entiled to £10,000.00 tax allowance for the year.
    What will be your net salary for the year?
    '''

    q_ten = '''
    Bonus Question:
    Whats is 18 percent of 5 Million barrels of oil
    '''

    list_of_questions = [q_one, q_two, q_three, q_four, q_five, q_six, q_seven, q_eight, q_nine, q_ten]


    #Shuffle list

    random.shuffle(list_of_questions)
    return list_of_questions

    

    #return list_of_questions

        

