def func1():
    print("함수1 호출")

func1()

# 변수에 함수를 담는 방법
func2 = func1

print(id(func1))
print(id(func2))

func2()
print()

# 1. 콜백 함수
def func3_1(data):
    print("함수3_1 호출")
    return f"{data} 처리 완료"

def func3_2(data):
    print("함수3_2 호출")
    return f"{data} 처리 실패"

def func4(callbackfunc):
    print("함수4 호출")
    print(callbackfunc("새로운 데이터"))
    print("함수4 호출 끝")

func4(func3_1)