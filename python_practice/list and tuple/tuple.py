# print("Inshall tommorow i will start from tuple")


num = (1,2,3,4,4,4,5) # why this is tuple because of this "()" bracket

print()

print(type(num))

# num [0] = 2222 # tuple are immutable
# print(num)

no = num.count(4) #count number of repitition
print (no)

index = num.index(1)
print(index)

p = (1,2,3,4)
a,b,c,d = p
print(a,b,c,d)

tup = ()
print(tup)
print(type(tup))

tup = (1)
print(tup)

tup = (1,)
print(tup)

tup = (1,2,3,4,3,4,4,5)
print(tup.count(4))