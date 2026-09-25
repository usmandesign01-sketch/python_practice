print("==== Kwarg function ======")
def user(**info):
    for x,y in info.items():
        print(x,y)
    print(info)
user(name =":Usman khan", father_name =":Fazal Malik",age =":19", city =":Mingora")