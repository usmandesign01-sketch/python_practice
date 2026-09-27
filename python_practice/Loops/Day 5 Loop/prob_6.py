'''

🟡 Problem 6 — Count Even Numbers
Given:
numbers = [12, 7, 5, 20, 33, 44, 18, 9]

'''

numbers = [12, 7, 5, 20, 33, 44, 18, 9]

count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1
print(f"Total even numbers are {count}")