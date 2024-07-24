# SWEA D2
# 1284. 수도 요금 경쟁
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # P: A사의 리터당 요금
    # Q: B사의 기본요금
    # R: 기본 리터
    # S: 기본요금 초과 이후 맅터당 요금
    # W: 수도 사용량

    #A사의 요금
    price_of_Acompany = P * W

    #B사의 요금
    if R >= W: # 수도 사용량 W가 기본 요금 R보다 작거나 같은 경우
        price_of_Bcompany = Q # 기본 요금만 부과

    elif R < W: # 수도 사용량 W가 기본 요금 R을 초과한 경우
        price_of_Bcompany = Q + ((W - R) * S)
        # (Q) 기본 요금 부과 후 (W - R) (초과량) * (S) (리터당 요금량)

    print(f"#{test_case} {min(price_of_Acompany, price_of_Bcompany)}")