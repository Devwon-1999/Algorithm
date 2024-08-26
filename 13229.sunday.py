# SWEA D3
# 13229. 일요일
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX0SaDW6L2oDFASs&categoryId=AX0SaDW6L2oDFASs&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = 0

    #입력
    string = input()
    if string == "SUN":
        answer = 7
    else:
        answer = 6 - day.index(string)

    #출력
    print(f"#{test_case} {answer}")