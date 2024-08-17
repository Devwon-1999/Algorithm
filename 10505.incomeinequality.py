# SWEA D3
# 10505. 소득 불균형
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXNP4CvauaMDFAXS&categoryId=AXNP4CvauaMDFAXS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    N = int(input())
    numList = list(map(int, input().split()))

    avg = sum(numList) // N
    for i in numList:
        if i <= avg:
            answer += 1

    #출력
    print(f"#{test_case} {answer}")