def sum(a,b):
    print(a + b)
    return(a + b)
sum(2,3)

def sum_num(a,b=10):
    return a + b

total = sum_num(10)
print(f"Total",total)

def greet(name, greeting = "Welcome!"):
    print(name, greeting)
    return(name, greeting)
greet("usman")
greet("KHan", greeting="Hi")