number = 10
name = "강수림수림" # 다른 건 그냥 그런데 얘가 좀 중요 : 여러 함수 사용 가능
isOpen = True

print(number)
# print(name_) # 오류 앞 라인까지는 실행 된다
print(name)
print(isOpen)

# print(name.index("숭"))  # exception
# print(name.find("숭"))   # return -1

print(name.index("수",2))
print(name.find("수"))

print("이름은: {name}, 숫자: {number}, 열림: {isOpen}".format(name=name, number=number, isOpen=isOpen))
print(f"이름은: {name}, 숫자: {number}, 열림: {isOpen}") # f 포매팅 : 정처기에 나온 적 있음, 여기서는 변수를 넣었지만 함수 등도 사용 가능
address = """부
산
동
래
구
중앙대로""" # 여러 줄로 나누어 쓸 수 있음
print(address)

