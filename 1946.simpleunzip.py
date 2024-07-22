# SWEA D2
# 1946. 간단한 압축 풀기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PmkDKAOMDFAUq&categoryId=AV5PmkDKAOMDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    order = []
    string = ""
    for i in range(N):
        temp = list(input().split())
        order.append(temp)

    for char, num in order:
        string += char * int(num)

    cnt = 0
    print(f"#{test_case}")
    for i in list(string):
        print(i, end = "")
        cnt += 1
        if cnt % 10 == 0:
            print()
    print()