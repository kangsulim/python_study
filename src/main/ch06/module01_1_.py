name = "강수림"

def add(n1, n2):
    return n1 + n2

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

if __name__ == "__main__":
    print("모듈 1번 실행")
    print(__name__)
    print(add(10, 20))
    print(Student("강수림", 25))