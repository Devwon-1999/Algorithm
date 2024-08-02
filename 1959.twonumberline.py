# SWEA D2
# 1959. 두 개의 숫자열
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for test_case in range(1, T + 1):
    #입력
    n, m = map(int, input().split()) #n : 첫번째 숫자열의 길이, m : 두번째 숫자열의 길이
    num_list1 = list(map(int, input().split())) # 첫번째 숫자열
    num_list2 = list(map(int, input().split())) # 두번째 숫자열

    answer = [] # 테스트케이스별 결과를 저장할 list

    if n > m: #첫 번째 숫자열의 숫자의 개수가 많다면 pass
        pass
    elif n < m: #두 번째 숫자열의 숫자의 개수가 많다면 숫자열 상호교환
        num_list1, num_list2 = num_list2, num_list1
        n, m = m, n
    #위 과정을 통해 항상 num_list1의 개수가 더 많아진다.

    #메인 알고리즘
    for i in range(n - m + 1):
        temp = 0

        for j in range(m):# 마주보는 숫자의 누적합
            temp = temp + (num_list1[j] * num_list2[j])

        if n != m: #숫자 위치 변경
            num_list2.insert(0, 0)
            m += 1
        answer.append(temp)

    print(f"#{test_case} {max(answer)}")