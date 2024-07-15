# SWEA D2
# 백만장자 프로젝트
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    answer = 0

    for i in range(N-2, -1, -1):
        if price[i] >= max_price:
            max_price = price[i]
        else:
            answer += max_price - price[i]

    print(f"#{test_case} {answer}")