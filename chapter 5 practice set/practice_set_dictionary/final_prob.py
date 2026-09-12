'''🔥 Day 3 Final Challenge

Create a Student Record Program using a dictionary.

Your dictionary should contain at least:

name
age
city
math
computer
english

Then calculate:

Total marks
Average marks

and print a clean student summary.

Then:

Add a new piece of information

For example:

"grade"

and update the dictionary.'''

std_info = {
    "name" : "USMAN Khan",
    "age" : 19.4,
    "city" : "Mingora, Tindodag",
    "math_marks" : 50,
    "computer_marks" : 87,
    "english_marks" : 78,
    "physics_marks" : 89,
    "urdu_marks" : 89,
    "mutalia_Quran_marks" : 45

}
for key, value in std_info.items():
    print(f"{key} : {value}")

