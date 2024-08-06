# SWEA D2
# 1961. 숫자 배열 회전
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    #입력
    N = int(input())
    numList = [list(map(int, input().split())) for _ in range(N)]

    #90, 180, 270 뒤집음
    numList90 = rotation(numList)
    numList180 = rotation(numList180)
    numList270 = rotation(numList270)


    #출력
    print(f"#{test_case}")
    for a, b, c in zip(numList90, numList180, numList270):
        print(f"{a} {b} {c}")