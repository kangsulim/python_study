# 1. 여러 개의 값이 return 가능한가?
def func1():
    return "func1", "func2", "func3"

r1, r2, r3 = func1()
print(r1, r2, r3)

r4, r5, r6 = "func4", "func5", "func6"
print(r4, r5, r6)

r7 = "func7", "func8"
print(r7)

# 자동으로 ()가 쳐져서 튜플로 반환되고 그러므로 index를 따질 수 있어서 순서대로 r1, r2, r3 등에 대입할 수 있다


# 2. 기본값 매개변수
def func2(membershipType, name):
    return {
        "회원종류" : membershipType,
        "이름" : name
    }

member1 = func2("일반회원", "강수림")
print(member1)

member2 = func2("골드회원", "강목림")
print(member2)

# default value를 가지는 매개변수는 가장 뒤에 위치
def func2(name, membershipType="일반회원" ):
    return {
        "회원종류" : membershipType,
        "이름" : name
    }
member3 = func2("강금림")
print(member3)


# 3. 키워드 매개변수 -> 어떤 매개변수에 값을 전달할지 명시
def func3(name, membershipType, address, phone, registerDate):
    return {
        "회원종류" : membershipType,
        "이름" : name,
        "address" : address,
        "phone" : phone,
        "registerDate" : registerDate

    }

member4 = func3("강수림", "VIP", "주소", "전화번호", "가입일")
print("member4: ", member4)
member5 = func3(
    address="주소",
    phone="전화번호",
    membershipType="VIP",
    name="강수림",
    registerDate="가입일") # 매개변수 순서를 지키지 않아도 된다
print("member5: ", member5)

# 4. 가변 인자 *args : arguments / **kwargs : keyword arguments
# *변수명 / **변수명
def func4(*args):
    print(args)

func4(159, "fjksdfjk", False, [15,64,"fnskd"])  # (159, 'fjksdfjk', False, [15, 64, 'fnskd'])와 같이 argument를 튜플로 받는다

def func5(*aa, bb):
    print(f"aa: {aa}")
    print(f"bb: {bb}")

# func5(1,2,3,4,5,6,7)    # 우선순위의 문제
func5(1,2,3,4,5,6,7, bb=8)  # 가변인자와 함께 쓰이면 매개변수를 명시

def func6(address, **cc):
    print(f"cc: {cc}")
    print(address)
    print(cc)

func6("부산", name="강수림", age=25)

"""
매개변수 작성 순서 요약
1. 일반(필수)
2. default value
3. *args
4. 키워드 전용 인자
5. **kwargs
"""

def func(a, b=0, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

func(10, 20, 30, 40, 50, name="강수림", age=25)

