# SWEA D3
# 15941. 평행사변형
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYVgOZEKOpcDFAQK&categoryId=AYVgOZEKOpcDFAQK&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    N = int(input())

    answer = N * N

    #출력
    print(f"#{test_case} {answer}")