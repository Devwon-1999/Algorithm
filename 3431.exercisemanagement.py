# SWEA D3
# 3431. 준환이의 운동관리
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    L, U, X = map(int, input().split())

    if X < L:
        answer = L - X
    elif X > U:
        answer = -1
    elif L <= X <= U:
        answer = 0

    #출력
    print(f"#{test_case} {answer}")