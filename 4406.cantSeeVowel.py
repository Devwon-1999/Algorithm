# SWEA D3
# 4406. 모음이 보이지 않는 사람
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWNcD_66pUEDFAV8&categoryId=AWNcD_66pUEDFAV8&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    #입력
    str = input()


    for i in vowel:
        if i in str:
            str = str.replace(i,"")

    #출력
    print(f"#{test_case} {str}")