'''
Descripton: Code testbed / playground


'''


#Calculate age

computer_numbers = {10,12,25,44,50,59}
player_numbers = {9,10,44,58,2,5}

#Get match between player and computer
def Get_Number_Match(in_computer_number,in_player_number):

    player_name = "Ufuoma Okoro"

    get_match = set.intersection(in_computer_number,in_player_number)

    count_match = len(get_match)

    return player_name, count_match



play_results = Get_Number_Match(computer_numbers, player_numbers)

print(play_results[0],play_results[1])
   