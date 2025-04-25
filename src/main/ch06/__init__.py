from module01_1_ import name,  add, Student
__all__ = [name, add, Student]

# __init__에 import 한 것을 통해
# from src.main.ch06 패키지의 경로만 import 하면
# __init__에 정의된 내용을 모두 사용할 수 있다.