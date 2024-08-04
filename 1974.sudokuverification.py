# SWEA D2
# 1974. 스도쿠 검증
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    base = [] #격자
    answer = 1 #정답
    #입력
    for i in range(9):
        temp = list(map(int, input().split()))
        base.append(temp)

    # 가로 격자 확인
    for i in range(9):
        check = set()
        for j in range(9):
            check.add(base[i][j])

        if len(check) != 9:
            answer = 0
            break

    # 세로 격자 확인
    for i in range(9):
        check = set()
        for j in range(9):
            check.add(base[j][i])
        if len(check) != 9:
            answer = 0
            break

    # 3 * 3 격자 확인
    for i in range(0, 9, 3):  # 0, 3, 6 - 각 3x3 블록의 시작 행
        for j in range(0, 9, 3):  # 0, 3, 6 - 각 3x3 블록의 시작 열
            check = set()
            for x in range(3):  # 3x3 블록의 행을 순회
                for y in range(3):  # 3x3 블록의 열을 순회
                    check.add(base[i + x][j + y])  # 현재 3x3 블록의 요소를 check 집합에 추가
            if len(check) != 9:  # 중복이 있거나 숫자가 빠졌다면
                answer = 0
                break
        if answer == 0:
            break

    print(f"#{test_case} {answer}")