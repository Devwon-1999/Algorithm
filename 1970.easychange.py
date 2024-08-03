# SWEA D2
# 1970. 쉬운 거스름돈
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = [0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())

    i = 0

    while N > 0 and i < len(won):
        if N >= won[i]:
            N -= won[i]
            answer[i] += 1
        else:
            i += 1

    print(f"#{test_case}")
    for i in answer:
        print(i, end = " ")
    print()
