# SWEA D3
# 2817. 부분 수열의 합
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

from itertools import combinations

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    answer = 0
    for i in range(1, N + 1):
        for j in combinations(num_list, i):
            print(j, sum(j))
            if sum(j) == K:
                answer += 1
    print(f"#{test_case} {answer}")