# SWEA D2
# 1948. 날짜 계산기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    month1, day1, month2, day2 = map(int, input().split())

    if month1 == month2: #달이 같은경우 간단히 day끼리만 뺀후 + 1
        answer = day2 - day1 + 1

    else: #달이 다른경우
        answer = day[month1] - day1 + 1     # 먼저 첫번째 달의 날짜를 answer에 대입
        for i in range(month1 + 1, month2): # 첫번째 달 이후의 달 부터 구할 달의 바로 앞달까지 일수를 더해준 뒤
            answer += day[i]
        answer += day2                      # 마지막 달의 잔여 일수를 더함
    print(f"#{test_case} {answer}")

