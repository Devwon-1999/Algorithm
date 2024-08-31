# SWEA D3
# 8658. Summation
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AW1lwyh6WPwDFARC&categoryId=AW1lwyh6WPwDFARC&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    answer = []

    #입력
    numList = list(map(int , input().split()))

    for i in numList:
        temp1 = list(str(i))
        temp2 = 0
        for j in temp1:
            num = int(j)
            temp2 += num
        answer.append(temp2)

    #출력
    print(f"#{test_case} {max(answer)} {min(answer)}")