# Write a function which take a number from user and make a square of that number
def square_number():
    user = int(input("Enter a number: "))
    return user * user

result = square_number()
print("The square of the number is:", result)