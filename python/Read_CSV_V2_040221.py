'''
Synposis: Script to read csv file and to write to the csv file

Wrtitten By: Ufo Okoro

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
Write_CSV_File(write_file_name)




