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

# How to define a class for what to store
# class Car:              # Class
#     color = "Blue"
#     model = "Toyota"

# # How to make an objects
# car1 = Car              # Object
# print(car1.color)
# print(car1.model)



# Class Attribute:
#                 An attribute that belongs to the class rather than a particular object.
class Employe:
    salary = 12300
    language = "Py"

usman = Employe()
usman.name = "Usman Khan"
print(f"Name is {usman.name}\nlanguage is {usman.language}\nsalary is {usman.salary}")

print("\n")

kamran = Employe()
kamran.name = "Kamran"
print(f"Name is {kamran.name}\nlanguage is {kamran.language}\nsalary is {kamran.salary}")

# Here name is Object attribute and salaray and language are class attribute