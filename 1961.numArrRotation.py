# SWEA D2
# 1961. 숫자 배열 회전
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numList = []
    for i in range(N):
        temp = list(map(int, input().split()))
        numList.append(temp)


    print(f"#{test_case} {numList}")