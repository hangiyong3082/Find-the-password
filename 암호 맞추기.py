import random

game_re = True

while game_re == True:
    # 암호 설정
    A = str(random.randrange(1,9))
    B = str(random.randrange(1,9))
    C = str(random.randrange(1,9))
    D = str(random.randrange(1,9))
    E = str(random.randrange(1,9))

    game = 0
    game_win = False

    dif = input("난이도를 고르세요 (쉬움, 중간, 어려움) : ")
    if dif == "쉬움":
        try_n = 15
    elif dif == "중간":
        try_n = 10
    elif dif == "어려움":
        try_n = 7

    print("")
    print("암호 다섯자리를 맞추세요")
    print(f"기회는 {try_n}번 입니다")
    print("")

    while game_win == False: 
        game = 0
        code = input("암호를 맞추세요 : ")

        # 입력한 암호 분석
        if code[0] == A:
            a = A
            game += 1
        else:
            a = "X"    

        if code[1] == B:
            b = B
            game += 1
        else:
            b = "X"

        if code[2] == C:
            c = C
            game += 1
        else:
            c = "X"

        if code[3] == D:
            d = D
            game += 1
        else:
            d = "X"

        if code[4] == E:
            e = E
            game += 1
        else:
            e = "X"

        #시도 가능 횟수
        try_n -= 1

        #분석 결과
        if game == 5:
            print("\n정답입니다!!")
            game_win = True

        elif try_n == 0:
            print("\n실패")
            game_win = True

        else:
            print("[ " + a+b+c+d+e + " ]" + " "*5 + f"{try_n}번 남음")
            print("")

    Q = input("다시하겠습니까? (네, 아니요) : ")
    if Q == "네":
        game_re = True
    elif Q == "아니요":
        game_re = False