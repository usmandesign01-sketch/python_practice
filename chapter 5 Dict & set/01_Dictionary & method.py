dict = {} # Empty dictionary 
print(dict)
print(type(dict))

name = {

"Harry" : 1300, #"Harry" and "Usman" are keys while 100 and 99 are values
"Usman1" : 99,
"Nida" : 885
}

# Dictionary method are following : 

print(name.values())
print(name.keys())
print(name.items())
print(type(name))
# Dictionary are mutable so we can update the values . for example
# name.update({"Usman": 100 , "Nida": 885})
# print(name) # In this update function i change the values because dict are mutable(changeble)
# print(name.get("juniad"))
# print(name)
print(name.get("Usman")) # get specified value of key
print(name["Usman1"]) # what differnce have in these two get method. In method one if key is not present then it will return None but in second method it will give error if key is not present
# print(name.pop("Nida")) # pop method remove the specified key and value from dictionary
# print(name)
# print(name.popitem()) # popitem method remove the last inserted key and value from dictionary
# print(name)
# print(name.setdefault("Nida", 1000)) # setdefault method return the value of specified key if key is present in dictionary otherwise it will add the key and value in dictionary
# print(name)
# print(name.clear()) # clear method remove all the key and value from dictionary
# print(name)
print(name.copy()) # copy method return the copy of dictionary
print(name.fromkeys(["Usman", "Nida", "Sohail"], 100)) # fromkeys method return the new dictionary with specified keys and values
print(name.update({"Usman": 1008 , "Nida": 885})) # update method update the value of specified key if key is present in dictionary otherwise it will add the key and value in dictionary
print(name["Harry"])