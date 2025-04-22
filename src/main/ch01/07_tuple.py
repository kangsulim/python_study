anyTuple = (1,2,3,4)
print(anyTuple)
print(anyTuple[2:])

newList = list(anyTuple)
print(newList)

newTuple = anyTuple + (5,6,7,8)
print(newTuple)

a, b, *c = newList
d, e, *f = newTuple
# a,b,c,d,e = newList # ValueError: not enough values to unpack (expected 5, got 4)

print(a,b,c,d,e,f)

newTuple = 1,2,3,4,5
print(newTuple)