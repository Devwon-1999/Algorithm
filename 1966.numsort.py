# SWEA D2
# 1966. 숫자를 정렬하자
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numList = list(map(int, input().split()))

    sort_numList = sorted(numList)

    print(f"#{test_case} {' '.join(map(str, sort_numList))}")