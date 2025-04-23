studentDict = dict()

studentDict = {
    "name" : "James",
    "age" : 245
}
print(studentDict)

# Dict 갑 추가
studentDict["address"] = "Busan"
print(studentDict)

# List와의 차이점
anyList = []
# anyList[0] = "test" # List는 기존에 할당되어 있는 주소의 값만 변경할 수 있다.
anyList.append("test")  # 그러므로 append 함수를 사용하여 값을 추가해야 한다.
print(anyList)  # ['test']

print()

# Dict 특정 value 조회
name = studentDict.get("name")
print(name)
print(studentDict["name"])
print(name)

# Dict value 수정
studentDict["address"] = "Seoul"
print(studentDict)

# Dict key : value 삭제

del studentDict["age"]
print(studentDict)
studentDict.pop("name")
print(studentDict)

# # 특정 키의 value를 None(NULL)으로 수정하기
# studentDict["address"] = None
# print(studentDict)

# Dict의 key-value 쌍 -> item
studentDict["name"] = "Paul"
studentDict["age"] = 25
print(type(studentDict.items()))    # <class 'dict_items'>
print(studentDict.items())          # dict_items([('address', 'Seoul'), ('name', 'Paul'), ('age', 25)])
print(list(studentDict.items()))    # [('address', 'Seoul'), ('name', 'Paul'), ('age', 25)]

addressItem = list(studentDict)[0]
print(addressItem)
print()

key, value = list(studentDict.items())[0]
print(f"key: {key}, value: {value}")

# Dict의 key 뽑기
print(studentDict.keys())
print(list(studentDict.keys()))

# Dict values
print(studentDict.values())
print(list(studentDict.values()))

searchKey = "code"

students = [
    {
        "code": 1,
        "name": "Andrew"
    },
    {
        "code": 2,
        "name": "Johan"
    },
    {
        "code": 3,
        "name": "Kyle"
    }
]

# searchkey를 통해 code만 추출
result = []

i = 0
while i < len(students):
    student = students[i]
    result.append(student[searchKey])
    i += 1

print(result)

# result Dict 내에 list 형태로 각 학생의 item을 종류별로 나누어 담기

students = [
    {
        "code": 1,
        "name": "Andrew"
    },
    {
        "code": 2,
        "name": "Johan"
    },
    {
        "code": 3,
        "name": "Kyle"
    }
]

result = {}

i = 0

while i < len(students):
    student = students[i]
    keys = list(student.keys())

    j = 0
    while j < len(keys):
        key = keys[j]
        j += 1
        if key in result:
            result[key].append(student[key])
            continue
        result[key] = [student[key]]

    i += 1

print(result)

# 이후에 result를 set()에 담으면? -> 중복이 제거된다

