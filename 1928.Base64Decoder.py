# SWEA D2
# 1928. Base64 Decoder
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PR4DKAG0DFAUq&categoryId=AV5PR4DKAG0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=3

T = int(input())

array = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P', 'Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        '0','1','2','3','4','5','6','7','8','9','+','/' ]

for test_case in range(1, T + 1):
    string = list(input())
    value = ""
    for i in range(len(string)):
        index = array.index(string[i])
        bin_index = str(bin(index)[2:])

        while len(bin_index) < 6:
            bin_index = '0' + bin_index
        value += bin_index

    answer = ""
    for i in range(len(string) * 6 // 8):
        number = int(value[i * 8 : i * 8 + 8], 2)
        answer += chr(number)

    print(f"#{test_case} {answer}")

