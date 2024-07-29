# SWEA D3
# 1209. [S/W 문제해결 기본] 2일차 - Sum
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

for _ in range(10):
    N = int(input()) # 테스트케이스 번호
    answer = []
    base = []

    for i in range(100):
        temp = list(map(int, input().split()))
        base.append(temp)

    # 가로
    for x in range(100):
        temp_sum = 0
        for y in range(100):
            temp_sum += base[x][y]
        answer.append(temp_sum)

    # 세로
    for x in range(100):
        temp_sum = 0
        for y in range(100):
            temp_sum += base[y][x]
        answer.append(temp_sum)

    # 대각선
    temp_sum = 0
    for i in range(100):
        temp_sum += base[i][i]
    answer.append(temp_sum)

    dx, dy = [i for i in range(99, -1, -1)], [i for i in range(100)]
    temp_sum = 0
    for i in range(100):
        temp_sum += base[dx[i]][dy[i]]
    answer.append(temp_sum)

    print(f"#{N} {max(answer)}")