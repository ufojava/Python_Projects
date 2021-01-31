'''
Synopsis: This is where I will perform unit testing



'''



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



