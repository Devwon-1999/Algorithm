# SWEA D2
# 1989. 초심자의 회문 검사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    string = list(input())
    reverse_string = list(reversed(string))

    if string == reverse_string:
        answer = 1

    print(f"#{test_case} {answer}")