# SWEA D2
# 2001. 파리 퇴치
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    fly_list = []
    for i in range(N):
        temp = list(map(int, input().split()))
        fly_list.append(temp)

    answer = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    cnt += fly_list[x][y]
            answer = max(answer, cnt)

    print(f"#{test_case} {answer}")


