'''Write a program to input eight numbers 
from the user and display all unique numbers (once)
'''


# set = (int(input("Enter 1st numbers :") , input("Enter 2nd numbers :"), input("Enter 3rd numbers :"), input("Enter 4th numbers :"), 
#            input("Enter 5th numbers :"), input("Enter 6th numbers :"), input("Enter 7th numbers :"), input("Enter 8th numbers :" )))
# print (set)



num1 = int(input("Enter 1 number : "))
# print(num1.append())
num2 = int(input("Enter 2 number : "))
# print(num2.append())
num3 = int(input("Enter 3 number : "))
# print(num3.append())
num4 = int(input("Enter 4 number : "))
# print(num4.append())

set_numbers = {num1, num2, num3, num4}

print(set_numbers)