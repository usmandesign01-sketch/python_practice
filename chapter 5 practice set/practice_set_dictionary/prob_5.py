'''Problem 5 — Dictionary Update

Create:

student = {
    "name": "Usman",
    "age": 18,
    "city": "Swat"
}

Then:

Change the age.
Change the city.
Add "marks".
Print the updated dictionary.'''

std = {
    "name": "Usman",
    "age": 18,
    "city": "Swat"
}
# std.clear()
std["age"] = 19
std["city"] = "Mingora"
new_data = {"marks":43}
std |= new_data # New things i learn
print(std)


