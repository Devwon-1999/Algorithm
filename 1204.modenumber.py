# SWEA D2
# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))
    temp = [0 for i in range(1000)]
    for i in score:
        temp[i - 1] += 1
 
    answer = temp.index(max(temp))
    answer_list = list(filter(lambda n: temp[n] == temp[answer], range(len(temp))))
 
    print(f"#{N} {max(answer_list) + 1}")


