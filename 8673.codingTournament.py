# SWEA D3
# 8673. 코딩 토너먼트1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AW2Jldrqlo4DFASu&categoryId=AW2Jldrqlo4DFASu&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    K = int(input())
    numList = list(map(int, input().split()))

    for round in range(K):
        next_round = []  # 다음 라운드에 올라갈 사람들을 저장할 리스트

        # 2명씩 대결
        for i in range(0, len(numList), 2):
            a = numList[i]
            b = numList[i + 1]
            answer += abs(a - b)  # 지루한 정도 계산 (차이의 절댓값)

            # 승자 결정 (더 실력 높은 사람이 승자)
            if a > b:
                next_round.append(a)
            else:
                next_round.append(b)

        # 다음 라운드에 올라갈 사람들로 업데이트
        numList = next_round
    #출력
    print(f"#{test_case} {answer}")
