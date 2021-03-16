'''
Descripton: Code testbed / playground


'''


class Computer_Assets:

    def __init__(self,manufacturer,model,location):

        self.manufacturer = manufacturer
        self.model = model
        self.location = location


#Input computer assets
in_manufacturer = input("Input asset manufacturer: ").capitalize()

print()
in_model = input("Input asset model: ").upper()

print()
in_location = input("Input asset location: ").capitalize()


#Feed input into class
computer_object = Computer_Assets(in_manufacturer, in_model, in_location)

#Print assets
print()
print(computer_object.manufacturer, computer_object.model,computer_object.location)

