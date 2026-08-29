# find average of std
# def avg(**std):
#     total = 0
#     for x in std:
#         total = total + x
#         print(total/len (std))
#     return total
# avg(10,20,30,40,50)

def avg(**std):
    total = 0
    for x in std.values():
        total = total + x
    print("average:",total/len(std))

avg(physics = 78, english = 66, urdu = 88, pak_study = 40)