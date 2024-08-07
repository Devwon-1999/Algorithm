# SWEA D2
# 1961. 숫자 배열 회전
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

#메인 알고리즘
def rotation(arr):
    arrReturn = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrReturn[i][j] = arr[N-1-j][i]
    return arrReturn

for test_case in range(1, T + 1):
    #입력
    N = int(input())
    numList = [list(map(int, input().split())) for _ in range(N)]

    #90, 180, 270 뒤집음
    numList90 = rotation(numList)
    numList180 = rotation(numList90)
    numList270 = rotation(numList180)


    #출력
    print(f"#{test_case}")
    for a, b, c in zip(numList90, numList180, numList270):
        print(f"{''.join(map(str, a))} {''.join(map(str, b))} {''.join(map(str, c))}")