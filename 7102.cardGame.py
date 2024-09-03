# SWEA D3
# 7102. 준홍이의 카드놀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWkIlHWqBYcDFAXC&categoryId=AWkIlHWqBYcDFAXC&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    count = [0 for _ in range(N + M + 1)]  # 빈도 리스트 초기화

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            count[i + j] += 1  # 합의 빈도 계산

    max_count = max(count)  # 최대 빈도
    most_common = [i for i, v in enumerate(count) if v == max_count]  # 최대 빈도의 합 찾기

    print(f"#{test_case}", end = " ")
    for i in most_common:
        print(i, end = " ")
