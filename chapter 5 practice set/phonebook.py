phonebook = {
    "Usman Khan" : "0342-9434607",
    "Osama Khan" : "0349-9434607",
    "Hamza Khan" : "0315-9014220",
    "Sheheryar Khan" : "0347-7717529",
}
# print(phonebook["Usman Khan"])
# print(phonebook.get("bhai Khan"))

car_brand = {
    "car" : "Toyota",
    "Color" : "white",
    "Model" : "New brand 2026",
    "Price" : "15 lac"
}

# print(car_brand["Price"])

my_details = {
    "Name" : "Usman Khan",
    "Father_Name" : "Fazal Malik",
    "Address" : "Tindodag, Mingora Swat",
    "Study_Status" : "Currently pass FSc in CS ",
    "Phone_Number" : "0342-9434607"
}
# print(my_details)

urdu_english_dictionary = {
    
    "door" : "Darwaza",
    "handle" : "Lasky",
    "key" : "Chabe"
}
# word = input("Konsa word chahiya : ").lower()

# print("Urdu Matlb : ", urdu_english_dictionary.get("word"))

my_details = {
    "Name" : "Usman Khan",
    "Father_Name" : "Fazal Malik",
    "Address" : "Tindodag, Mingora Swat",
    "Study_Status" : "Currently pass FSc in CS ",
    "Phone_Number" : "0342-9434607"
}
# print("name :" , my_details.get("computer"))
print(list(my_details.items()))