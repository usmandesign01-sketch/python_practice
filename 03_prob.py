# what happen if you open a non-existing file in "r" mode

# it will give error

file = open("xyz", "r")
data = file.read()
print(data)
file.close()