# SWEA D3
# 1289. 원재의 메모리 복구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    original = list(input())
    base = ["0" for _ in range(len(original))]

    for i in range(len(original)):
        if original[i] != base[i]:
            base[i:] = [original[i]] * (len(base) - i)
            answer += 1

    #출력
    print(f"#{test_case} {answer}")