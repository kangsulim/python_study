"""
생성자를 통한 주입
"""

class 무기:
    def __init__(self, 공격력):
        self.공격력 = 공격력

    def 공격(self):
        pass

class 총(무기):
    def __init__(self, 공격력, 총알):
        # super(공격력)    # python의 super는 부모의 생성자가 아니라 부모 클래스에 접근하는 용도로 사용된다
        super().__init__(공격력)  # 그러므로 __init__을 사용하여 부모 클래스를 생성해야한다
        self.총알 = 총알

    def 공격(self):
        print(f"총을 쏜다.(데미지: {self.공격력})")
        self.총알소비()
        return self.공격력

    def 총알소비(self):
        self.총알 -= 1
        print(f"잔탄량: {self.총알}")

class 칼(무기):
    def __init__(self, 공격력):
        super().__init__(공격력)

    def 공격(self):
        print(f"칼을 휘두른다.(데미지: {self.공격력})")
        return self.공격력

class 손:
    def __init__(self, 타입, 무기):
        self.타입 = 타입    # 왼손, 오른손
        self.무기 = 무기
        self.데미지합 = 0

    def 데미지_합(self, 데미지):
        self.데미지합 += 데미지
    
    def 손으로_공격(self):
        print(f"{self.타입}으로 공격합니다.")
        데미지 = self.무기.공격()
        self.데미지_합(데미지)


# 총1 = 총(100, 10)
# 총1.공격()

오른손 = 손("오른손", 칼(50))
왼손 = 손("왼손", 총(100, 3))

오른손.손으로_공격()
while 왼손.무기.총알 > 0:
    왼손.손으로_공격()

print()

print(f"오른손 누적 데미지: {오른손.데미지합}")
print(f"왼손 누적 데미지: {왼손.데미지합}")
"""
오른손으로 공격합니다.
칼을 휘두른다.(데미지: 50)
왼손으로 공격합니다.
총을 쏜다.(데미지: 100)
잔탄량: 2
왼손으로 공격합니다.
총을 쏜다.(데미지: 100)
잔탄량: 1
왼손으로 공격합니다.
총을 쏜다.(데미지: 100)
잔탄량: 0

오른손 누적 데미지: 50
왼손 누적 데미지: 300
"""

