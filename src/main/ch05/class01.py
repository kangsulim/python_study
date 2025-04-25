# 1 python의 class 정의
# 1. 멤버 변수만 있는 클래스 생성

class Student:  # 파일명과 클래스명이 같지 않아도 된다 (Java 클래스와 다른 점)
    # 멤버 변수
    name = "강수림"
    age = 25


print(Student())    # <__main__.Student object at 0x000001A115D20310>

print(Student().name)   # 강수림
print(Student().age)    # 25

# 위에서 각각의 객체들은 사용 시에 새로 생성된 것이기 때문에 모두 다른 객체이다 (주소가 다름)

# 그러므로 동일한 객체를 사용하려면 변수에 대입해야한다
s1 = Student()
print(s1)

print()

# 2. 멤버 변수와 메서드가 포함된 클래스
class Student:
    name = "강수림"
    age = 25

    def toString(self):
        return f"Student(name: {self.name}, age: {self.age})"

    @classmethod
    def toString2(cls):
        return f"Student(name: {cls.name}, age: {cls.age})"

s1 = Student()
print(s1.name)
print(s1.age)
print(s1.toString())    # 메서드의 매개변수에 자동으로 현재 참조중인 객체의 주소가 포함된다

print(Student.toString2())  # 클래스명.메서드명() <- Static의 개념

Student.name = "강목림"    # 값을 바꿀 수 있다

print(Student.toString2())  # 진짜 바뀜

print(s1.name)  # 그래서 객체의 name도 바뀜

s1.name = "강금림" # 객체명.변수명 바꿔봄

print(Student.toString2())  # 클래스 자체를 바꾸지는 않고

print(s1.toString2())   # cls를 받는 toString2()도 못 바꾸고

print(s1.toString())    # self를 받는 toString()

print()


# 3. 사실 python class에서 멤버 변수는 생성자 안에서 생성한다
class Student:
    # python은 클래스 메서드와 스태틱 메서드를 구분해뒀다
    # 클래스 변수(Java의 static 변수)
    name = "강수림(클래스변수)"
    age = "25(클래스변수)"
    def __init__(self):
        # 멤버 변수
        self.name = "강수림"
        self.age = 25
# 이것이 진짜 멤버 변수 정의 / 위에서 한 것은 클래스 변수를 만든 것!!!

    def toString(self):
        return f"Student(name: {self.name}, age: {self.age})"

    # classmethod는 클래스 변수에 접근 가능
    @classmethod
    def toString2(cls):
        return f"Student(name: {cls.name}, age: {cls.age})"

    # 클래스 변수와 멤버 변수에 접근할 수 없다
    @staticmethod
    def toString3(name, age):
        return f"Student(name: {name}, age: {age})"

print(Student.name) # 강수림(클래스변수)
print(Student.age)  # 25(클래스변수)

s1 = Student()

print(s1.name)  # 강수림
print(s1.age)   # 25

print(s1.toString())    # Student(name: 강수림, age: 25)
print(s1.toString2())   # Student(name: 강수림(클래스변수), age: 25(클래스변수))


# 4 각각의 메서드에서 변수 참조
class Student:
    name = "강수림(클래스변수)"
    age = "25(클래스변수)"

    def __init__(self):
        # 멤버 변수
        self.name = "강수림"
        self.age = 25

    def toString(self):
        return f"Student(name: {self.name}, age: {self.age}, clsName: {self.__class__.name})"

    @classmethod
    def toString2(cls):
        return f"Student(name: {cls.name}, age: {cls.age})"

    @staticmethod
    def toString3(name, age):
        return f"Student(name: {name}, age: {age})"

s1 = Student()
print(s1.toString())    # Student(name: 강수림, age: 25, clsName: 강수림(클래스변수))

