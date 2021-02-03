'''
Synposys: Script to demonstrate how to read csv files

Written By: Ufuoma Okoro

Dept: Home Office

'''

import csv

#Import csv file data
with open("Personal_Data_V2.csv", "r") as personal_data_import:

    #Define the reader
    data_reader = csv.DictReader(personal_data_import)

    #Create Menu
    print('''
    
    1. Print all data

    2. Search by Lastname
    
    ''')
    print()
    in_option = int(input("Select option: "))



    #Iterate through the data
    if (in_option == 1):

        for row in data_reader:

            #print(row["Firstname"], row["Lastname"], row["Age"], row[Nationality])
            print(row)
    
    elif (in_option == 2):

        search_lastname = input("Input lastname: ")
        print()
        column_names = data_reader.fieldnames
        #print(column_names)
       
        for row in data_reader:

            if(row["Lastname"] == search_lastname.capitalize()):

                
                #print(row["Firstname"], row["Lastname"], row["Age"], row["Nationality"])
                print(row)

    else:

        print(f"{in_option} is an invalid selection !!!")



