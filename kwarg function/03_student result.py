# find total marks
def std(**marks):
    total_marks = 0
    for x in marks.values():
        print(x)
        total_marks = total_marks + x
    return(total_marks) 
a =std(physics = 40, chemistry = 49)
print("Total:",a)