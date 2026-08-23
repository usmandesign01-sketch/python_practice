user = int(input("Enter a number: "))
def check_even_odd(user):
    if user <= 0:
        print("You enter zero or negative number ")
    elif user % 2 == 0:
        print("Even number")

    elif user % 2 != 0:
        print("Odd number")
check_even_odd(user)