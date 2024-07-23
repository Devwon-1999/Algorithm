# SWEA D2
# 1976. 시각 덧셈
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    hour1, min1, hour2, min2 = map(int, input().split())

    answer_hour = hour1 + hour2
    answer_min = min1 + min2

    if answer_min > 59:
        answer_min -= 60
        answer_hour += 1

    if answer_hour > 12:
        answer_hour -= 12

    print(f"#{test_case} {answer_hour} {answer_min}")
