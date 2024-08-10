# SWEA D2
# 1285. 아름이의 돌 던지기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV18-stqI8oCFAZN&categoryId=AV18-stqI8oCFAZN&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    #변수
    score = 0 # 점수
    people = 0 # 동일 정답자 수
    scoreList = [] # 절대값으로 점수만을 저장하는 리스트

    #입력
    N = int(input())
    temp = list(map(int, input().split()))

    #메인 알고리즘
    for i in temp:
        scoreList.append(abs(i))

    sorted_scoreList = sorted(scoreList)

    score = min(sorted_scoreList)
    people = sorted_scoreList.count(min(sorted_scoreList))

    #출력
    print(f"#{test_case} {score} {people}")