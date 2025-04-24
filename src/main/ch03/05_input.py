a = int(input("a입력: ")) ## 특정 자료형으로 쓰고 싶으면 강제 형변환 필요
b = input("b입력: ")

print(a, b)
print(type(a))
print(type(b))

# "10 20"
number = input("두 수 입력: ").split()
print(number)

number1, number2 = input("두 수 입력: ").split()
print(number1, number2)

# 람다식 변환
number1, number2 = map(lambda n: int(n), input("두 수 입력: ").split())
print(number1, number2)

def parseInt(n):
    return int(n) # 얘도 함수

number1, number2 = map(parseInt, input("두 수 입력: ").split())
print(number1, number2)

# 그러므로
number1, number2 = map(int, input("두 수 입력: ").split()) # int 만 작성해도 함수를 정의한 것과 같으니까 동작이 같음 ㅇㅇ
print(number1, number2)