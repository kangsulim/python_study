anyTuple = (1,2,3,4)
print(anyTuple)
print(anyTuple[2:])

newList = list(anyTuple)
print(newList)

newTuple = anyTuple + (5,6,7,8)
print(newTuple)

a, b, *c = newList
d, e, *f = newTuple

print(a,b,c,d,e,f)

newTuple = 1,2,3,4,5
print(newTuple)