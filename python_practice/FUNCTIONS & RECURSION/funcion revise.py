# Function: A function is a reusable block of code designed to perform a particular task.

# instead of writting 19 times 
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# just write this
# def greet():
#     print("Hello")
# greet()
# greet()
# greet()
# greet()

def hi(name): # name is a parameter
    print("Hello", name)
hi("Usman") # Usman is an argument
hi("Alice")
hi("Bob")
hi("Charlie")
hi("David")

def add(a, b):
    return a + b # return send the value where the function is called

result = add(5, 3)
print(f"The sum is: {result + 2}")