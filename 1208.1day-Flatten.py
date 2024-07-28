# SWEA D3
# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = 10

for test_case in range(1, T + 1):
    answer = 0

    N = int(input()) # 덤프 횟수
    num_list = list(map(int, input().split())) # 주어지는 리스트

    for i in range(N):
        if len(set(num_list)) == 1:
            break
        else:
            max_index = num_list.index(max(num_list))
            min_index = num_list.index(min(num_list))
            num_list[max_index] -= 1
            num_list[min_index] += 1

    answer = max(num_list) - min(num_list)
    print(f"#{test_case} {answer}")
