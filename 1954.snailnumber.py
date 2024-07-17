# SWEA D2
# 1954. 달팽이 숫자
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for test_case in range(1, T + 1):
    N = int(input())
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    dir_num = 0
    x, y = 0, 0
    base = [[0] * N for i in range(N)]
    base[x][y] = 1

    for i in range(2, N * N + 1):
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if not in_range(nx, ny) or base[nx][ny] != 0:
            dir_num = (dir_num + 1) % 4

        x, y = x + dxs[dir_num], y + dys[dir_num]
        base[x][y] = i

    print(f"#{test_case}")
    for i in range(N):
        for j in range(N):
            print(base[i][j], end = " ")
        print()
