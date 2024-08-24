# SWEA D3
# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = 10

def squared(A, B):
    if B == 0:
        return 1
    return A * squared(A, B - 1)

for test_case in range(1, T + 1):
    N = int(input())
    #입력
    A, B = map(int, input().split())

    #출력
    print(f"#{test_case} {squared(A,B)}")