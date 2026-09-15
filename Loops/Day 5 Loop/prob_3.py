'''🟢 Problem 3 — Multiplication Table
Ask the user for a number.'''

user = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{user} * {i} = {user * i}")