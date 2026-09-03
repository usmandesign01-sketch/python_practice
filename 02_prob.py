# check your file "donkey.txt" whether the word donkey is present or not

file = open("donkey.txt")
word = file.read()
word = word.lower()

if "donkey" in word:
    print("Yes the word Donkey is present")
else:
    print("NO the word Donkey is not present")