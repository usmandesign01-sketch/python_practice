# def show(*language):
#     language = "Java","C++","Django","Javascript","Python"
#     for x in language:
#         print(x)
# show()

# # *********************************************************************************
# def test(*arg):
#     print("Ye mila mujay", arg)
#     print("Type", type(arg))
# test(12,13,14)

# # *********************************************************************************
# def total_nums(*exam):
#     total = 0
#     for x in exam:
#         total = total + x
#     print("Total",total)
# total_nums(4,1,54,3)

# # *********************************************************************************
# # problem 2: add a number

# def task_user(*num_add):
#     total = 0
#     for x in num_add:
#         total = total + x
#     return total

# a = task_user(443,520,1008,399,443)
# print("Total:",a)

# # *********************************************************************************
# # problem 3
# # auto
# def avg(*numbers):
#     average = 0
#     for x in numbers:
#         average = average + x
#     print(average/len(numbers))
    
# avg(10, 20, 30, 40, 50)

# # *********************************************************************************
# # manual
# def avg(*numbers):
#     total = 0
#     count = 0
#     for x in numbers:
#         total = total + x
#         count = count + 1
#     print(total/count)
#     # return total
#     # return count

# avg(10,20,30,40,50)

# # *********************************************************************************

# # find how much positive number are in list
# def find(*larNum):
#     count = 0
#     for x in larNum:
#         if x>0:
#             count = count + 1
#     print (count)
#     return count
# find(3,4,-5,3,6) 

# *********************************************************************************

# incompleteeeeeeeeee
# def num(*numbers):
#     largest_number = [0]
#     for x in numbers:
#         if x > largest_number:
#             print (x)
#             largest_number = x
#     return largest_number
# a = num(10,20,30,40,50)
# print(a)
# *********************************************************************************

# final challenge question 
''' total nikalna hay
    average nakalna hay
    largest number nikalna hai
    even numbers ki count nikani hai'''

def analyze_number(*numbers):
    total = 0
    average = 0
    largest = 0
    count_even = 0
    for i in numbers:
        total = total + i
        average = total/len(numbers)
        if i > largest:
            largest = i
        if i % 2 == 0:
            count_even = count_even + 1
    print(" Total:",total,"\n","Average:",average,"\n","Largest:",largest,"\n","Total even number:",count_even)
    return total, average, largest, count_even


analyze_number (10,25,8,40,13,22,34,44,33,6)
