'''
Descripton: Code testbed / playground


'''

'''
import random


#Various ways to loop
def Player_Input():

        #Take in player input, Number and operator

        while True:

            try:
                player_number = int(input("Input a number between 1 and 99: "))

                if (player_number > 0 and player_number < 100):

                    break
            
            except:


                pass

#Player_Input()

#Produce random number between 2 numbers
def Computer_Random():




   get_Computer_Number = random.randint(1, 99)

   print(f"The Computer numner is {get_Computer_Number}")



Computer_Random()


'''

#Add a class object to a list

result_list = []
import os
import os.path
import json
import pandas as pd

import datetime

todays_date_time = datetime.datetime.now()

'''
class Get_Result:

    def __init__(self,in_firstname,in_lastname,in_percentage,in_score,in_date):

        self.in_firstname = in_firstname
        self.in_lastname = in_lastname
        self.in_percentage = in_percentage
        self.in_score = in_score
        self.in_date = in_date




for result in range(2):

    result_list.append(Get_Result(input("Enter firstname: "),input("Enter lastname: "),input("Enter percentage: "),input("Enter socre: "),todays_date_time))


os.system("clear")
    
for result in result_list:

   

    print(result.in_firstname,result.in_lastname,result.in_percentage,result.in_score,result.in_date)




if os.path.isfile("my_test_file.txt"):

    print("File exist")

else:

    print("File does not exist")

'''



#Import csv file

#input_name = input("Enter your first or last name: ")

data_frame = pd.read_csv("predict.csv")

score_col = data_frame["Score"]
max_value = score_col.max()


#filtered_data = data_frame.loc[((data_frame["Firstname"] == input_name) | (data_frame["Lastname"] == input_name) & max_value)]
filtered_data = data_frame.loc[(data_frame["Score"] == max_value)]

#filtered_data = data_frame.loc[[0,1,2],:]

#filtered_data = data_frame.loc[0:2,:]

#filtered_data = data_frame.loc[:,["Percentage","Date"]]

#filtered_data = data_frame.loc[0:2,"Lastname":"Date"]

#Create a boolean condition

get_limited_columns = filtered_data.loc[:,["Percentage","Date"]]

print(filtered_data)









    












   