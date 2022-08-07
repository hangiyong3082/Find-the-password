import random

game_re = True

#명령어 설정
easy = "E"
medium = "M"
hard = "H"
yes = "Y"
no = "N"

while game_re == True:
    # 암호 설정
    a = random.randrange(0,9)
    b = random.randrange(0,9)
    c = random.randrange(0,9)
    d = random.randrange(0,9)
    e = random.randrange(0,9)

    game = 0
    game_win = False

    dif = input(f"난이도를 고르세요 ({easy}, {medium}, {hard}) : ")
    if dif == easy or dif == easy.lower():
        try_n = 12
    elif dif == medium or dif == medium.lower():
        try_n = 8
    elif dif == hard or dif == hard.lower():
        try_n = 6

    print(f"\n암호 다섯자리를 맞추세요\n맞춘 숫자는 표시됩니다\n \n각 자리의 숫자들을 모두 더한값은 {a+b+c+d+e} 입니다")
    print(f"기회는 {try_n}번 입니다\n ")

    A = str(a)
    B = str(b)
    C = str(c)
    D = str(d)
    E = str(e)

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
            print("\n정답입니다!!\n ")
            game_win = True

        elif try_n == 0:
            print("\n실패" + f" (정답은 {A+B+C+D+E}입니다)\n ")
            game_win = True

        else:
            print("[ " + a+b+c+d+e + " ]" + " "*3 + f"{try_n}번 남음\n ")

    Q = input(f"다시하겠습니까? ({yes}, {no}) : ")
    if Q == yes or Q == yes.lower():
        r = 50
        while r != 0:
            print("")
            r -= 1
        game_re = True
    elif Q == no or Q == no.lower():
        game_re = False
