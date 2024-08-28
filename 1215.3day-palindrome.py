# SWEA D3
# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = 10
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

for test_case in range(1, T + 1):
    #변수
    answer = 0 #정답을 저장할 변수
    maze = [] #주어지는 8*8 격자

    #입력
    N = int(input()) #찾을 N만큼 길이의 회문
    for i in range(8): #격자 입력
        temp = list(input())
        maze.append(temp)

    #알고리즘
    # 가로 방향 회문 검사
    for i in range(8):
        for j in range(8 - N + 1):
            # 가로로 연속된 N글자 확인
            if palindrome(maze[i][j:j + N]):
                answer += 1

    # 세로 방향 회문 검사
    for i in range(8):
        for j in range(8 - N + 1):
            # 세로로 연속된 N글자 확인
            column_string = "".join(maze[j + k][i] for k in range(N))
            if palindrome(column_string):
                answer += 1

    #출력
    print(f"#{test_case} {answer}")