# SWEA D2
# 1940. 가랏! RC카!
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PjMgaALgDFAUq&categoryId=AV5PjMgaALgDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    answer = 0 # 정답
    speed = 0 # 속도
    numList = [] # 입력될 매초마다의 가속도


    #입력
    N = int(input())
    for i in range(N):
        temp = list(map(int, input().split()))
        numList.append(temp)

    #알고리즘
    for i in numList:
        if i[0] == [0]:
            continue
        elif i[0] == 1:
            speed += i[1]
        elif i[0] == 2:
            speed -= i[1]
            if speed < 0:
                speed = 0

        answer += speed

    #출력
    print(f"#{test_case} {answer}")