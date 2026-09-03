# with open("c.txt") as file:
#     data = file.read()
#     print(data)
# file = open("c.txt")
# data = file.read()
# print(data)

f = open("text1.txt", "r")
data = f.read()
print(data)


for lines in f:
    print(lines)
f.close
for x in f:
    print(x)