numbers = [1,2,3,4,5]

print(numbers[0])   # index
print(numbers[0:3]) # index to index
print(numbers[:3])  # start to end
print(numbers[3:])  # index to end
print(numbers[-3:]) # -index to end
print(numbers[:-2]) # start to -index
print("부산 동래구"[3:]) # string에서도 마찬가지로 index to end
print((1,2,3,4)[2:])    # 튜플도 마찬가지
# print({1,2,3,4}[2:])  # set은 순서가 없어서 안 된다
print([1,2,3,4][2:])    # 마찬가지로 list도 생성과 동시에 사용 가능

anyList = [[1, "김준일", [3, 4, [7, "김준이"], 6]]]

# 김준이를 출력하시오
print(anyList[0][2][2][1])

# [3, 4, [7, '김준이'], 6]를 출력하시오
print(anyList[0][2][:])

# [4, [7, '김준이']]를 출력하시오
print(anyList[0][2][2:3])   # index(start) to index(end)

listList = [[[0,1,2], [3,4,5], [6,7,8]],
            [[9,10,11],[12,13,14],[15,16,17]],
            [[18,19,20],[21,22,23],[24,25,26]]]

listK = []
n = 0

for i in listList:
    for j in i:
        for k in j:
            listK.append(k)
            print(listK[n], end=" ")
            n += 1
print()

print(listK[:])

# 05_operator, 06_while 학습 이후
# list 더하기
print([1,2,3] + [4,5,6])

# list 곱하기
print([1,2,3] * 3)

print(len([1,2,3])) # len() 함수
                    # list.len X / len(list)
print()

anyList = [1,2,3,4]
i = 0
while i < len(anyList):
    print(anyList[i])
    i += 1

print()

# print(3 + 'a') # 서로 다른 자료형은 오류

print(str(3) + "hi")    # 3hi
print(int("1") + 2)     # 3
                        # 자료형 함수를 사용하면 casting이 가능하다
print(bool("True") & False) # boolean도 마찬가지

# list 수정, 삭제한다.
del anyList[2]

print(anyList)

# del anyList[4] # del 키워드로 삭제할 때는 값이 꼭 존재해야

anyList.remove(1)
print(anyList)

anyList.pop(1)
print(anyList)

# 예외 처리를 위해 가능하다면 함수를 사용하도록 하자 (del 지양)
try:
    anyList.pop(4)
    print(anyList)
except Exception as e: # 여기에 '기분 나쁜 노란 줄'이 생긴 이유는 해당 코드가 검출 가능한 오류의 범위가 try 내에 작성한 오류 보다 너무 크기 때문이다. 여기서는 IndexError로 수정하면 기분 나쁜 노란 줄이 사라지지만 일단 놔둠.
    print("해당 리스트의 범위를 초과한 참조이다.")

anyList = [1,2,3]

anyList.append(4)
anyList.append([5, 6])

print(anyList)
print()

anyList = [1,2,3,5,8]
print(anyList)  # [1, 2, 3, 5, 8]
anyList.insert(3, 4) # index 3에 number data 4 삽입
print(anyList)  # [1, 2, 3, 4, 5, 8]
anyList.insert(5, [6,7]) # index 5에 list data [6,7] 삽입
print(anyList)  # [1, 2, 3, 4, 5, [6, 7], 8]

anyList = [1,5,2,3,4]
# anyList.sort() # 원본의 내용 수정
# copyAnyList = anyList.copy()    # 기존 리스트를 copy() 해서 다른 리스트에 저장
copyAnyList = anyList[:] # 이렇게 해도 마찬가지
copyAnyList.sort()
copyAnyList.reverse()
print(anyList)
print(copyAnyList)

print([1,2,3,4,5] == [1,2,3,4,5])
print([1,2,3,4,5] == [1,2,4,3,5])

anyList = [1,2,3,4,5]
anyList2 = [1,2,3,4,5]
print(anyList == anyList2)
print(id(anyList) == id(anyList2))
print(id(anyList), id(anyList2))

anyList2 = anyList
print(anyList == anyList2)
print(id(anyList) == id(anyList2))
print(id(anyList), id(anyList2))
print()

anyList = [1,2,3]
anyList2 = [4,5]
print(id(anyList))
anyList = anyList + anyList2
print(id(anyList))

anyList.extend([6,7])
print(id(anyList))
print()

anyList = [0,1,2,3,4,5,6,7,8,9]
print(anyList[::]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(anyList[1:9:2]) # [1, 3, 5, 7]
print(anyList[-7:-2:3]) # [3, 6]
print(anyList[::-1])
print()

# 점프 투 파이썬 list 끝

anyList.clear()
print(anyList)
print(id(anyList))