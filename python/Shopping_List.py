'''
Description: Shopping List . Buy products with cost assocaited with it

Import File working Directory: /home/ufookoro/playground/projects/powershell/import_Files
Import File: Stoct_Price.csv

'''


#Import library
import os
import sys
import csv


#Create colout pallette
colour_end = "\33[0m"
colour_red = "\33[31m"
colour_green = "\33[32m"
colour_yellow = "\33[33m"
colour_blue = "\33[34m"



def Get_Product_List():


    #Product List
    products = []


    with open("/home/ufookoro/playground/projects/powershell/import_Files/Stock_Price_V2.csv", "r") as stock_import:

        #Define reader
        data_reader = csv.DictReader(stock_import)

        #Product Menu
        print('''

        1. Print complete list
        2. Print Specific product
        3. Check Product Code
        
        ''')


       

        while True:

            menu_option = input("Select an option: ")

            #Test Option
            try:

                if (menu_option == "1" or menu_option == "2" or menu_option == "3"):

                    break
            except:
                pass

            
        if (menu_option == "1"):

            #Clear Screen
            os.system("clear")
            for row in data_reader:

                #Build product list
                products.append(row)

            for product in products:

                print(product)

        elif (menu_option == "2"):

            get_product_code = input("Input product code: ")

            for row in data_reader:

                if (row["Code"] == get_product_code):

                    products.append(row)
            print(products)


        elif (menu_option == "3"):

            #Variable
            #Populate list
            for row in data_reader:

                #Build product list
                products.append(row)
        

            shopping_list = []
            shopping_items_qty = 0
            product_code_exist = False

            while True:

                try:

                    #Get the number of items
                    get_shopping_list_qty = int(input("Enter number to items you wish to purchase: "))
                    break
                    
                except:
                    pass

            #Enter product code
            print()
            get_product_code = input("Enter product code: ")
            print()

            #Input produce code
            for product in products:
                if (get_product_code  == product["Code"]):
                    product_code_exist = True

            print(product_code_exist)



        
    
    return products



        
#Class to create orders
class Create_Order:

    def __init__(self,firstname,lastname):

        self.firstname = firstname
        self.lastname = lastname


    
    def Stock_List(self): 

        get_firstname = self.firstname
        get_lastname = self.lastname

        os.system("clear")
        print(f'''
        {get_firstname} {get_lastname}

        ''')

        #Get stock list and specific order
        get_stock = Get_Product_List()


        





      


#Main program starts here

#Get buyer details
process_orders = Create_Order("Ufuoma", "Okoro")

#Print Buyer Details
print(f"{process_orders.firstname} {process_orders.lastname}")

print('''
********* Main Menu *******
1. Run Product Stock Check Program
2. Exit program

''')

while True:

    run_program = input("Enter menu option: ")

    try:

        if (run_program == "1" or run_program == "2"):
            break
    
    except:
        pass



if (run_program == "1"):

    process_orders.Stock_List()

elif (run_program == "2"):

    print("Progam will exit")
    sys.exit()


      
