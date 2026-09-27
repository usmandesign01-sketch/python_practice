user = int(input("Enter a number: "))
def check_even_odd_num(user):

    if user <= 0:
        print("You enter zero or negative number ")
    elif user % 2 == 0:
        print(f"The number {user} is even")

    elif user % 2 != 0:
        print(f"The number {user} is odd")
        
check_even_odd_num(user)

