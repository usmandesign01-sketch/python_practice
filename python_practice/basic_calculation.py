print("Simple Calculation")

a = int(input("Enter 1st Number : "))

b = int(input("Enter 2nd Number : "))

c = input("Enter Operation : ")

if c == "+" :
    print (a+b)

elif c == "-" :
    print (a-b)

elif c == "*" :
    print (a*b)

elif c == "/" :
    if b == 0:
        print("cannot divide by zero")
    else:
        print (a/b)

else :
    print("Invalid Entry")