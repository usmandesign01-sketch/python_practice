# def count_even(numbers):
#     even = 0
#     for x in numbers:
#         if x % 2 == 0:
#             even = even + 1
#     return even

# numbers = [2,4,3,55,6,89,60]
# result = count_even(numbers)
# print(result)

def count_odd(numbers):
    odd = 0
    for x in numbers:
        if x % 2 != 0:
            odd += 1
    return odd
numbers = [4, 7, 12, 15, 18, 21, 24, 29, 31]
result = count_odd(numbers)
print(result)