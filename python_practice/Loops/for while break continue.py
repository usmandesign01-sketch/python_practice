# loops
# for i in range(1,9):
#     print(i)

# x = 10
# while x>1:
#     print(x)
#     x = x - 1

# Question 1
# print number from 1 to 100 through while loop
# number = 1
# while number<=100:
#     print(number)
#     number = number + 1

# Question 2
# print number from 100 to 1 through while loop
# number = 100
# while number>=1:
#     print(number)
#     number = number - 1

# Question 3
# print a multiplication table of n number

# number = 1
# user_ka_input = int(input("Enter a number : "))
# while number<=10:
#     print(user_ka_input, "*", number, "=", user_ka_input*number)
#     number = number + 1

# Question 4
# print a list_number (confused)
# a = [14,155,11,66,87,88,66,44,90,0.50]
# index = 0
# while index < len(a):
#     print(a[index])
#     index = index + 1

# fruits = ["apple","banana","Grapes","pineapple"]
# idx = 0
# while idx < len(fruits):
#     print(fruits[idx])
#     idx = idx + 1

# fruits = ("apple","banana","Grapes","pineapple")
# idx = 0
# while idx < len(fruits):
#     print(fruits[idx])
#     idx = idx + 1

# fruits = ["apple","banana","grapes"]
# idx = 0
# while idx < len(fruits):
# 	if idx == 2:
# 	print(fruits[idx])
# 	idx = idx + 1

# Question 5 print x number from list
# nums = [14,155,11,66,87,88,66,44,90,0.50]
# x = 90
# i = 0
# while i< len(nums):
#     if(nums[i]==x):
#         print("FOUND at index",i)
#     i = i+ 1\

# name = "usman khan"
# for x in name:
#     if (x == "s"):
#         print("FOUND",x)

# ***************************************************************************************************************
# lets practice for loop

# print the elements of the list
# nums = [14,155,11,66,87,88,66,44,90,0.50]
# for x in nums:
#     print(x)

# search for x number 
nums = (14,155,11,66,87,88,11,66,44,90,0.500)
index = 0
for x in nums:
    if (x == 11):
        print(x,"found at index", index)
        break
    index = index + 1