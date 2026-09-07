# print ("Hello I am learning OOPs topic in 07_Sept_2026")


'''OOP in Python :
    To map with real world scenarios, we started using objects in code.
    this is called oop.
    
    Why we Use?
    To increase the reusability of program '''

# Class VS Objects
'''Obj:
        In real world everything is object like Mouse, Car, Pen, Keyboard etc
        From everything we can make an objects but first we will make a class
        list string are object '''

'''Class:
        Class is a blueprint for creating an objects.
        Example: let's suppose I have a car we desing a blueprint that every Car will have blue color
        and 4 seats with AC'''

# Without OOP, you might write:
dog_name = "Buddy"
dog_age = 3

def bark(name):
    return f"{name} says woof!"
bark(dog_name)

# With OOP, you bundle data + behavior together:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"





# How to define a class for what to store
# class Car:              # Class
#     color = "Blue"
#     model = "Toyota"

# # How to make an objects
# car1 = Car              # Object
# print(car1.color)
# print(car1.model)