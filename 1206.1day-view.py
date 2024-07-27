# SWEA D3
# 1206. [S/W 문제해결 기본] 1일차 - View
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


for test_case in range(1, 11):
    answer = 0
    N = int(input())
    height_list = list(map(int, input().split()))

    #확인해야할 인덱스 추출
    check_list = []
    index = 0
    for i in height_list:
        if i != 0:
            check_list.append(index)
        index += 1

    #확인해야할 인덱스 별 좌, 우 2칸씩 확인
    for i in check_list:
        temp = []
        for j in range(i - 2, i + 2 + 1):
            temp.append(height_list[j])

        sorted_temp = sorted(temp, reverse=True)
        second_max_val = sorted_temp[1]
        if temp[2] == max(temp):
            answer = answer + (max(temp) - second_max_val)

    print(f"#{test_case} {answer}")