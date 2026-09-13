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

# ******************************************************************************************************************************

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
# printing total marks

total_marks = (
    std_info["math_marks"]
    + std_info["computer_marks"]
    + std_info["english_marks"]
    + std_info["physics_marks"]
    + std_info["urdu_marks"]
    + std_info["mutalia_Quran_marks"]
)

# print(std_info) # This print in list form

for key, value in std_info.items():
    print(f"{key} : {value}")
    
print(total_marks)

average = total_marks/6
print(f"The average is {average}")

# total_marks = ["math_marks" + "computer_marks" + "english_marks" + "physics_marks" + "urdu_marks" + "mutalia_Quran_marks" ]
# print(total_marks)
# std_info["computer_marks"]
