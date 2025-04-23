# 논리 연산
data1 = 10
data2 = 2

r1 = data1 == data2 # 같냐
r2 = data1 != data2 # 다르냐
print(r1, r2)

r3 = r1 and r2
r4 = r1 or r2
print(r3, r4)

print(not r3)
print(not (r3 and r4))

# 멤버 연산자 : in / not in

print("a" in "apple")
print("b" in "apple")
print("a" in ["a", "b", "c"])
print("d" in ["a", "b", "c"])
print("a" in ("a", "b", "c"))
print("name" in {"name" : "강수림", "age" : 25})
print("25" in {"name" : "강수림", "age" : 25}.values())


# 식별 연산자 : is / is not
print([1,2,3,4] is [1,2,3,4])
print([1,2,3,4] == [1,2,3,4])

print(10 == 10)
# print(10 is 10)


# if
if data1 == data2:
    print(f"data1: {data1}, data2: {data2}는 같다.")
else:
    print(f"data1: {data1}, data2: {data2}는 다르다.")


if data1 == 2:
    print("data1이 2입니다")
elif data2 == 2:
    print("data2가 2입니다")
else:
    print("둘 다 아닙니다")







