'''🔴 Problem 10 — break
Create a loop from 1 to 20.
When the number reaches 10, stop the loop.'''

number = 1
while number < 21:
    print(number)
    if number == 10:
        break
    number = number + 1