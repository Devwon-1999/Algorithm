# SWEA D2
# 1984. 중간 평균값 구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))

    num_list.remove(max(num_list))
    num_list.remove(min(num_list))

    print(f"#{test_case} {round(sum(num_list)/len(num_list))}")