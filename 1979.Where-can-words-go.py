# SWEA D2
# 1979. 어디에 단어가 들어갈 수 있을까
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    answer = 0 #정답을 저장할 변수
    base = [] #입력되는 격자를 저장할 리스트

    #입력
    size, word_length = map(int, input().split())
    #size : 격자의 크기, word_length : 찾을 단어의 길이

    #line by line으로 입력되는 격자를 base에 대입
    for i in range(size):
        temp = list(map(int, input().split()))
        base.append(temp)

    #격자 검증
    for i in range(size):
        cnt = 0

        #가로 검증
        for j in range(size):
            if base[i][j] == 1:
                cnt += 1
            if base[i][j] == 0 or j == size - 1:
                if cnt == word_length:
                    answer += 1
                cnt = 0
        #세로 검증
        for j in range(size):
            if base[j][i] == 1:
                cnt += 1
            if base[j][i] == 0 or j == size - 1:
                if cnt == word_length:
                    answer += 1
                cnt = 0


    print(f"#{test_case} {answer}")