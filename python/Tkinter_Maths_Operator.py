'''
Description: Program to utilise Tkinter to execute the basic maths operator:
Frame will be used in ths

Progam will accept 2 numbers and then:

1.Addition
2.Subtract
3.Multiply
4.Divide

Provide an answer after a click to calculate

'''

#Library
from tkinter import *
import os


#Initialise main window
main_window = Tk()
main_window.title("Mathify For Kids")

#Create Main window size
main_window.geometry("500x500")

#Top frame
top_frame = Frame(master = main_window,width=500,height=100,pady=30,bg="grey")
top_frame.grid(row=0,column=0,sticky="we")

#Blank grid
blank_grid = Label(top_frame,text="",width=15,bg="grey")
blank_grid.grid(row=0,column=0)

app_title = Label(top_frame,text="ARITHMETIC HELPER FOR KIDS",bg="brown",fg="white",borderwidth="5",relief="groove")
app_title.grid(row=0,column=1)

#Blank grid
blank_grid = Label(top_frame,text="",width=15,bg="grey")
blank_grid.grid(row=0,column=2)

#Middle frame
middle_frame = Frame(master =main_window ,width=500,height=300,pady=50)
middle_frame.grid(row=1,column=0,sticky="w")

#Frame for instructions
frame_for_instructions = Frame(master=middle_frame,width=100,height=50,pady=5)
frame_for_instructions.grid(row=0,column=0,sticky="w")


label_instruction = Label(frame_for_instructions,text="Input numbers, select maths symbol, click select and then calculate button",fg="blue")
label_instruction.grid(row=0,column=0,sticky="w")

data_input_frame = Frame(master=middle_frame,width=100,height=200)
data_input_frame.grid(row=1,column=0,sticky="w")


#Labels for data entry

label_number_one = Label(data_input_frame,text="Number One:")
label_number_one.grid(row=1,column=0,sticky="w")

#Variable for selected option
selected_option = StringVar()

#Select operator from dropdown list
operator_options =  [
                    "Addition",
                    "Subtraction",
                    "Multiplication",
                    "Division"
                    ]

#Set default option
selected_option.set(operator_options[0])


#Functionto display selection
def Show_Option(in_selected):

    get_selected_option = Label(data_input_frame,text=in_selected.get(),fg="green")
    get_selected_option.grid(row=2,column=3)


#Function to calculate
def Calculate(in_num_one,in_operator,in_num_two):

    #Variables
    get_num_one = int(in_num_one.get())
    get_num_two = int(in_num_two.get())
    calc_numbers = 0
    calculated_result = ""
    calculated_answer = StringVar()

    #Calculate input
    if (in_operator == "Addition"):

        #Addition
        calc_numbers = get_num_one + get_num_two

        #Convert number back to string
        calculated_result = str(calc_numbers)

        #Place answer
        calculated_answer = Label(data_input_frame,text=calculated_result,fg="green")
        calculated_answer.grid(row=4,column=1,sticky="w")
        

    elif (in_operator == "Subtraction"):

        #Subtraction
        calc_numbers = get_num_one - get_num_two

        #Convert result to string
        calculated_result = str(calc_numbers)

        #Place answer
        calculated_answer = Label(data_input_frame,text=calculated_result,fg="green")
        calculated_answer.grid(row=4,column=1,sticky="w")

    elif (in_operator == "Multiplication"):

        #Multiplication
        calc_numbers = get_num_one * get_num_two

        #Conver result to string
        calculated_result = str(calc_numbers)

        #Place answer
        calculated_answer = Label(data_input_frame,text=calculated_result,fg="green")
        calculated_answer.grid(row=4,column=1,sticky="w")

    elif (in_operator == "Division"):

        #Division
        calc_numbers = round(get_num_one / get_num_two,2)

        calculated_result = str(calc_numbers)

        #Place answer
        calculated_answer = Label(data_input_frame,text=calculated_result,fg="green")
        calculated_answer.grid(row=4,column=1,sticky="w")


#Label for selector
label_operator = Label(data_input_frame,text="Select Operator:",pady=15)
label_operator.grid(row=2,column=0,sticky="w")

#Show Operator option
get_operator_options = OptionMenu(data_input_frame, selected_option, *operator_options)
get_operator_options.grid(row=2,column=1)

#Button for Selector
button_operator = Button(data_input_frame,text="Click to Select",fg="brown",command=lambda:Show_Option(selected_option))
button_operator.grid(row=2,column=2)



#Second number
label_number_two = Label(data_input_frame,text="Number Two:")
label_number_two.grid(row=3,column=0,sticky="w")

label_answer = Label(data_input_frame,text="Answer:",pady=20)
label_answer.grid(row=4,column=0,sticky="w")

#Entry fields

#Input for number one
in_number_one = Entry(data_input_frame,width=5,borderwidth=3)
in_number_one.grid(row=1,column=1,sticky="w")

in_number_two = Entry(data_input_frame,width=5,borderwidth=3)
in_number_two.grid(row=3,column=1,sticky="w")





#Bottom frame
bottom_frame = Frame(master = main_window,width=500,height=100,pady=30,bg="grey")
bottom_frame.grid(row=3,column=0,sticky="we")

#Blank grid
blank_grid = Label(bottom_frame,text="",width=22,bg="grey")
blank_grid.grid(row=0,column=0)

calculate_button = Button(bottom_frame,text="Calculate",borderwidth="3",relief="raised",command=lambda:Calculate(in_number_one, selected_option.get(), in_number_two))
calculate_button.grid(row=0,column=1,sticky="we")




#Terminate main windows
main_window.mainloop()

