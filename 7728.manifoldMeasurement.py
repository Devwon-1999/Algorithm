# SWEA D3
# 7728. 다양성 측정
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWq40NEKLyADFARG&categoryId=AWq40NEKLyADFARG&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    #입력
    N = list(input())
    N = set(N)

    #출력
    print(f"#{test_case} {len(N)}")