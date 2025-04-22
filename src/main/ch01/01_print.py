print("Hello python", 123, end="!!!!!")
# 매개변수에 *values: object 이므로 튜플을 받는다.
# 그러므로 print는 여러개의 argument를 튜플의 형태로 받는다.
# end = "\n" 였는데 \n 대신에 !!!!!로 바꿨기 때문에 개행 하지 않는다

print("진짜로 개행 안 하는지 확인") # ㅇㅇ 개행 안 했네

# print(end="!!!", values=("Hello python", "test")) 이런 개념도 있기는 하다