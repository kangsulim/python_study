from email.headerregistry import ContentTypeHeader


class 클래스:

    def __init__(self, 변수1, 변수2):
        # 생성자 -> 인스턴스 변수 정의
        self.변수1 = 변수1
        self.변수2 = 변수2

    # Java의 toString() 오버라이딩과 같은 의미 - 실제로 프로그램 서비스 제공 중에 사용
    def __str__(self):
        return f"변수1: {self.변수1}, 변수2: {self.변수2}"

    # toSring() 레퍼런스(개발단계, 디버깅) - 개발 중에 사용
    def __repr__(self):
        return f"변수1111: {self.변수1}, 변수2222: {self.변수2}"

    # 객체 비교
    def __eq__(self, other):
        return self.변수1 == other.변수1 and self.변수2 == other.변수2

    def __add__(self, other):
        return 클래스(self.변수1 + other.변수1, self.변수2 + other.변수2)

    def __sub__(self, other):
        return 클래스(self.변수1 - other.변수1, self.변수2 - other.변수2)

    def __contains__(self, item):
        return item in (self.변수1, self.변수2) # in 이니까 boolean type 반환

c1 = 클래스(10, 20)
print(c1.__str__())
print(c1.__repr__())

print(c1)   # 변수1: 10, 변수2: 20
            # ↑ 위의 결과를 보면 __str__의 우선순위가 __repr__ 보다 높다

c2 = 클래스(10, 20)

print(c1.__eq__(c2))

c3 = c1.__add__(c2)
print(c3)

c4 = c1.__sub__(c2)
print(c4)

print(c3.__contains__(40))
print(c3.__contains__(10))