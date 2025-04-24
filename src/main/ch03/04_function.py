# 람다
"""
java 람다식 확인하기
"""

# lambda 매개변수: 표현식
def add(num1, num2):
    return num1 + num2
print(add(10, 20))

add = lambda num1, num2: num1 + num2
print(add(10, 20))

numbers = [1,5,7,8,9,6,2,4]

students = [("강수림", 25), ("강목림", 26), ("강금림", 27)]
sorted_students = sorted(students, key=lambda student: students[1])
print(sorted_students)

print(numbers)
numbers2 = list(map(lambda number: number * 3, numbers)) # map = 반복
print(numbers2)

print(numbers)
numbers3 = list(filter(lambda num: num % 2 == 0, numbers))
print(numbers3)

numbers4 = list(map(lambda num: f"<h1>{num}</h1>", numbers3))
print(numbers4)

