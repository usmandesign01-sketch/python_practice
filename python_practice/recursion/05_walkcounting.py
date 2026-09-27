# def walk(steps):
#     if steps == 10:
#         print("walk time completed")
#         return 
#     print("walk count",steps)
#     walk(steps + 1)
# # print("Your walk time completed")
# walk(1)

def count(number):
    if number == 0:
        return 0
    return number + count(number - 1)

print(count(5))