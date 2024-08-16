# SWEA D3
# 12368. 24시간
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXsEBlLqedsDFARX&categoryId=AXsEBlLqedsDFARX&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    A, B = map(int, input().split())

    answer = (A + B) % 24

    #출력
    print(f"#{test_case} {answer}")