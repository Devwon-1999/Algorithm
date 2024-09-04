# SWEA D3
# 1213. [S/W 문제해결 기본] 3일차 - String
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=4


for _ in range(10):
    #변수
    answer = 0

    #입력
    N = int(input())
    find_string = input()
    base_string = list(input())

    for i in range(0, len(base_string) - len(find_string) + 1):
        if find_string == "".join(base_string[i:i + len(find_string)]):
            answer += 1
    #출력
    print(f"#{N} {answer}")