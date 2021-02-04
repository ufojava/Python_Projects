'''
Synopsis: Script to read csv file and to write to the csv file and finally to append to a a file

Wrtiten By: Ufo Okoro

Department: Home Office

'''

#Import Modules
import csv

#Variables
read_file_name = "Personal_Data_V2.csv" #Read file name
write_file_name = "Personal_Data_Write.csv" #File to write to


#Function to read a a csv file
def Read_CSV_File(in_read_filename):

    #Import CSV FIle
    with open(in_read_filename, "r",newline="") as get_file:

        #Create Reader
        file_reader = csv.DictReader(get_file)

        for row in file_reader:

            #Print the row
            print(row)
    
        #Close file
        get_file.close()


#Call Read CSV file
#Read_CSV_File(read_file_name)

#Function to write to a csv file

def Write_CSV_File(in_write_file):

    #Variables
    headers = ["Firstname","Lastname","Age"]
    fam_members = [["Ufuoma","Okoro","55"],["Ovie","Okoro","56"],["Igho","Okoro","54"],["Bami","Okoro","50"]]

    #Use Open create file
    with open(in_write_file, "w",newline="") as write_file:

        #Create writer  
        file_writer = csv.writer(write_file,delimiter=",")
        file_writer.writerow(headers)
        

        #Write Data to the 
        for fam in fam_members:
            file_writer.writerow(fam)

        #Close file
        write_file.close()


#Call writer CSV File
#Write_CSV_File(write_file_name)


#Funciton to append to a csv file
def Append_To_CSV_File(in_file_name,in_person_data):

    print(in_person_data)
    test_data = "Hello world"

    with open(in_file_name, "a",newline="") as get_file:

        #Define file writer
        file_writer = csv.writer(get_file,delimiter=",")


        #Append to file
        for row in in_person_data:

            file_writer.writerow(row)
    
    #Close file
    get_file.close()

#Empty list to take in data
person_data = []

def Take_Per_Details():
    #List ol personla details
    detail_list = []

    #Take in user details
    per_firstname = input("Firstname: ")
    print()
    per_lastname = input("Lastname: ")
    print()
    per_age = input("Age: ")

    #Capitalize the input
    per_firstname = per_firstname.capitalize()
    per_lastname = per_lastname.capitalize()

    print()
    #print(f"{per_firstname} {per_lastname} {per_age}")
    detail_list.append(per_firstname)
    detail_list.append(per_lastname)
    detail_list.append(per_age)
    
    return detail_list



#Get personal data
person_data.append(Take_Per_Details())

#Pass list into the write to csv file

Append_To_CSV_File(write_file_name,person_data)






