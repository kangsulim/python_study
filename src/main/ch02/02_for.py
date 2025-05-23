# 범위 생성 함수 range()

r = range(10)
print(r)

rList = list(r)
print(rList)

r2 = range(5, 10)
print(list(r2))

r3 = range(0, 10, 2)
print(r3)
print(list(r3))

for num in range(10):
    print(num)

for num in [0,1,2,3,4,5,6,7,8,9]:
    print(num)

studentDict = {
    "name" : "강수림",
    "age" : 25,
    "address" : "양산시"
}

for student in studentDict:
    print(student)

studentItems = studentDict.items()  # list로 바꾸는 이유는 list와 관련된 함수를 쓰기 위함
print(studentItems)

for item in studentItems:
    print(item)

for key, value in studentItems:
    print(key, value)



# 08_dict 에서 한 while -> for

students = [
    {
        "code": 1,
        "name": "Andrew"
    },
    {
        "code": 2,
        "name": "Johan"
    },
    {
        "code": 3,
        "name": "Kyle"
    }
]

result = {}



for student in students:
    keys = list(student)
    for key in keys:
        if key in result:
            result[key].append(student[key])
            continue
        result[key] = [student[key]]

print(result)

# 점프 투 파이썬 for문 중
# 컴프리헨션

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 이중 for문도 가능

print()

for x in range(2, 10):
    for y in range(1, 10):
        if y == 1:
            print(f"{x}단", end="\t\t")
        print(f"{x} X {y} = {x*y}", end="\t" if y != 9 else "\n")
# 3항 연산자 형태
# a if 조건 else b


print()


print("2단\t\t\t3단\t\t\t4단\t\t\t5단\t\t\t6단\t\t\t7단\t\t\t8단\t\t\t9단")
for x in range(1, 10):
    for y in range(2, 10):
        multiple = x*y
        print(f"{y} X {x} = {multiple}", end="\t")
    print()










