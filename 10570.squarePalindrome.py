# SWEA D3
# 10570. 제곱 팰린드롬 수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXO72aaqPrcDFAXS&categoryId=AXO72aaqPrcDFAXS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
import math

T = int(input())

def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

for test_case in range(1, T + 1):
    #변수
    answer = 0

    #입력
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        if math.sqrt(i).is_integer():
            if palindrome(str(i)) and palindrome(str(int(math.sqrt(i)))):
                answer += 1

    #출력
    print(f"#{test_case} {answer}")

