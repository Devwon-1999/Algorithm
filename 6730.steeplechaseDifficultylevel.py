# SWEA D3
# 6730. 장애물 경주 난이도
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWefy5x65PoDFAUh&categoryId=AWefy5x65PoDFAUh&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    #입력
    N = int(input())
    numList = list(map(int, input().split()))

    up = []
    down = []
    if N == 2:
        if numList[0] > numList[1]:
            down.append(numList[0] - numList[1])
            up.append(0)
        elif numList[1] > numList[0]:
            up.append(numList[1] - numList[0])
            down.append(0)

    else:
        for i in range(N - 1):
            if numList[i] > numList[i + 1]:
                down.append(numList[i] - numList[i + 1])
            elif numList[i] < numList[i + 1]:
                up.append(numList[i + 1] - numList[i])
            else:
                up.append(0)
                down.append(0)

    #출력
    print(f"#{test_case} {max(up)} {max(down)}")

