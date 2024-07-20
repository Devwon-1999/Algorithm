# SWEA D2
# 2005. 파스칼의 삼각형
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
T = int(input())

for test_case in range(1, T + 1):
    # 입력
    N = int(input())

    # 최초 배열 초기화
    base = [[1 for j in range(i + 1)] for i in range(N)]

    # 배열 값 변경
    for i in range(2, N):
        for j in range(1, i):
            base[i][j] = base[i - 1][j - 1] + base[i - 1][j]

    # 출력
    print(f"#{test_case}")
    for i in base:
        for j in i:
            print(j, end=" ")
        print()
