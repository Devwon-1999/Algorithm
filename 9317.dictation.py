# SWEA D3
# 9317. 석찬이의 받아쓰기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AW-hOY5KeEIDFAVg&categoryId=AW-hOY5KeEIDFAVg&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=20&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    #입력
    N = int(input())
    original = input()
    dictation = input()

    for i in range(N):
        if original[i] == dictation[i]:
            answer += 1

    #출력
    print(f"#{test_case} {answer}")
