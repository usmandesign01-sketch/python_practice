'''# My code
current_year = 2026
date_of_birth_year = int(input("Enter your date of birth year : "))
age = current_year - date_of_birth_year
print("You are ", age, "old")'''


import datetime

birth_year = int(input("Enter birth year : "))
current_year = datetime.datetime.now().year
age = current_year - birth_year

print("You are",age, "year")