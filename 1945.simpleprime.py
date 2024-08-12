# SWEA D2
# 1945. 간단한 소인수분해
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    #변수
    cntList = [0, 0, 0, 0, 0] # 결과값을 저장할 리스트
    prime = [2, 3, 5, 7, 11] # 각 소수들
    index = 0 #인덱싱을 위한 변수

    #입력
    N = int(input())

    while True:
        if N in prime: #N이 prime일때 반복문 종료
            cntList[prime.index(N)] += 1 #종료하며 해당 값도 + 1
            break
        else:
            if N % prime[index] != 0:
                index += 1
            else:
                N //= prime[index]
                cntList[index] += 1

    #출력
    print(f"#{test_case} {' '.join(map(str, cntList))}")

