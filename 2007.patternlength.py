# SWEA D2
# 2007. 패턴 마디의 길이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    for i in range(10):
        temp_str = string[:i]
        temp_str = temp_str * 30
        temp_str = temp_str[:30]

        if string == temp_str:
            print(f"#{test_case} {i}")
            break