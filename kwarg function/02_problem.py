def info(**person):
    for x, y in person.items(): # mtlb har item se mumhe key bhi do aur uski value bhi do.
        print(x,y)
    return person
info(name = "Usman Khan", age = "20", course = "python", level = "beginer")
