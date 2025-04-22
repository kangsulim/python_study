# set, list, dict, tuple
set1 = set()
list1 = list()
dict1 = dict()
tuple1 = tuple()

print(type(set1)) # 자료형을 확인하는 type 함수

list2 = []
dict2 = {}
dict3 = {
    "n":0
}
tuple2 = ()
tuple3 = (10) # 10 <- 값이 하나라서 ()를 연산 기호로 본다
tuple4 = (10, ) # ,가 들어가면 그 때 부터 튜플로 본다
set2 = {0}


print(list2) # []
print(dict2) # {}
print(tuple2) # ()
print(set2) # {0}
print(dict3) # {'n': 0}

print(type(()))