# def countdown(n):
#     if n == 0:
#         print("Blast off!")
#         return(n)
#     print(n)
#     countdown(n-1)

# countdown(3)

# print number from one to ten through recursion instead of loop

# def print_num(n):
#     if n<1:
#         return
#     print(n)
#     print_num(n-1)
# print_num(50)

# for x in range(1,51):
#     print("Loop",x)

# x = 1
# while x < 10:
#     x = x + 1
#     print(x)

def num(n):
    if n<2:
        return
    print(n)
    num(n-1)
a = num(5)
print("Counting completed")