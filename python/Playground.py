'''
Descripton: Code testbed / playground


'''


#Calculate age

#Get computer random numbers
def Computer_Numbers():

    

    #Import library
    from numpy import random,sort

    get_computer_numbers = sort(random.randint(60, size=(6)))

    for number in get_computer_numbers:

        print(type(number))

    return

   


    




computer_play = Computer_Numbers()


print(computer_play)