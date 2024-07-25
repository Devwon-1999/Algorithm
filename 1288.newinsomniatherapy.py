# SWEA D2
# 1288. 새로운 불면증 치료법
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV18_yw6I9MCFAZN&categoryId=AV18_yw6I9MCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cnt = 1
    num_set = set()
    while True:
        number = cnt * N

        str_number = str(number)
        for i in str_number:
            num_set.add(i)
        cnt += 1

        if len(num_set) == 10:
            break
    print(f"#{test_case} {number}")