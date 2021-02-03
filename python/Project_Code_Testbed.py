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
    

Calc_Prize_Money_Test(2)

'''
Creating a GUI for application


'''






