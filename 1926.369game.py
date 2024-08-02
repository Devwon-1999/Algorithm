# SWEA D2
# 1926. 간단한 369게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

N = int(input())

clap = ["3", "6", "9"]

for i in range(1, N + 1):
    i = str(i)
    cnt = 0
    for j in i:
        if j in clap:
            cnt += 1

    if cnt == 0:
        print(i, end = " ")
    elif cnt == 1:
        print("-", end = " ")
    elif cnt == 2:
        print("--", end = " ")

# Sorry: TabError: inconsistent use of tabs and spaces in indentation (line 8)
# 코드 들여쓰기 오류

#Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
# 배열에 할당된 크기를 넘어서 접근했을 때
# 전역 배열의 크기가 메모리 제한을 초과할 때
# 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
# 0으로 나눌 떄
# 라이브러리에서 예외를 발생시켰을 때
# 재귀 호출이 너무 깊어질 때
# 이미 해제된 메모리를 또 참조할 때
# 프로그램(main 함수)이 0이 아닌 수를 반환했을 때