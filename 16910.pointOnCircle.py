# SWEA D3
# 16910. 원 안의 점
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYcllbDqUVgDFASR&categoryId=AYcllbDqUVgDFASR&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    #입력
    N = int(input())

    for i in range(-N, N + 1):
        for j in range(-N, N + 1):
            if (i ** 2) + (j ** 2) <= (N ** 2):
                answer += 1

    print(f"#{test_case} {answer}")