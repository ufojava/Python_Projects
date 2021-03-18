'''
Descripton: Code testbed / playground


'''


#Calculate age

from datetime import date

birth_date = date(1965,3,25)

today_date = date.today()

days_in_year = 365.2425

age = int((today_date - birth_date).days / days_in_year)

print(age)