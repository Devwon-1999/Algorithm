# SWEA D2
# 21425. +=
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AZD8K_UayDoDFAVs&categoryId=AZD8K_UayDoDFAVs&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    A, B, N = map(int, input().split())

    while True:
        if A > B:
            B += A
            answer += 1
        else:
            A += B
            answer += 1

        if A > N or B > N:
            break
    # 출력
    print(f"#{test_case} {answer}")