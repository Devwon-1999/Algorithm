# SWEA D3
# 12221. 구구단2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXpz3dravpQDFATi&categoryId=AXpz3dravpQDFATi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1'

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    A, B = map(int, input().split())

    if 1 <= A <= 9 and 1 <= B <= 9:
        answer = A * B
    else:
        answer = -1

    #출력
    print(f"#{test_case} {answer}")