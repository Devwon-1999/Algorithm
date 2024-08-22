# SWEA D3
# 11688. Calkin-Wilf tree 1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXgZSOn6ApIDFASW&categoryId=AXgZSOn6ApIDFASW&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=20&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    answer = [1, 1]

    #입력
    str = input()

    for i in str:
        if i == "L":
            answer[1] = answer[0] + answer[1]
        elif i == "R":
            answer[0] = answer[0] + answer[1]

    #출력
    print(f"#{test_case} {answer[0]} {answer[1]}")