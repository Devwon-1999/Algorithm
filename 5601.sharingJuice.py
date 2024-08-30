# SWEA D3
# 5601. [Professional] 쥬스 나누기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGAylqcdYDFAUo&categoryId=AWXGAylqcdYDFAUo&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    #입력
    N = int(input())

    # 출력
    print(f"#{test_case}", end = " ")
    for i in range(N):
        print(f"{1}/{N}", end = " ")
    print()


