if __name__ == '__main__':
    print("예외처리")

    numbers = [1,2,3,4,5]

    try:
        print(numbers[5])
    except IndexError as e:
        print(e, "오류가 발생했습니다.")
        print("원인은 범위 초과입니다.")

    print()

    try:
        print("예외 강제 발생")
        raise TypeError("자료형이 맞지 않습니다.")
    except TypeError as e:
        print(e)
