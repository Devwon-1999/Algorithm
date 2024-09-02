# SWEA D3
# 5431. 민석이의 과제 체크하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWVl3rWKDBYDFAXm&categoryId=AWVl3rWKDBYDFAXm&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numList = list(map(int, input().split()))
    base = [i for i in range(1, N + 1)]

    for i in numList:
        if i in base:
            base.remove(i)

    print(f"#{test_case}", end = " ")
    for i in base:
        print(i, end = " ")
    print()