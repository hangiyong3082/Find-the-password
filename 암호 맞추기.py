import random

game_re = True

#명령어 설정
easy = "E"
medium = "M"
hard = "H"
yes = "Y"
no = "N"
def input_letter(I, i):
    return I == i or I == i.lower()

while game_re == True:
    # 암호 설정
    a = random.randrange(0,9)
    b = random.randrange(0,9)
    c = random.randrange(0,9)
    d = random.randrange(0,9)
    e = random.randrange(0,9)

    game = 0
    game_win = False

    #난이도 고르기
    enter_dif = None
    while enter_dif != True:
        dif = input(f"난이도를 고르세요 ({easy}, {medium}, {hard}) : ")
        if input_letter(dif, easy):
            try_n = 12
            enter_dif = True
        elif input_letter(dif, medium):
            try_n = 8
            enter_dif = True
        elif input_letter(dif, hard):
            try_n = 6
            enter_dif = True
        else:
            print("(!)입력 오류")
            enter_dif = False

    #설명
    print("-"*50)
    print(f"\n암호 다섯자리를 맞추세요\n맞춘 숫자는 표시됩니다\n")
    print("-"*50)
    print(f"\n각 자리의 숫자들을 모두 더한값은 {a+b+c+d+e} 입니다")
    print(f"기회는 {try_n}번 입니다\n ")

    A = str(a)
    B = str(b)
    C = str(c)
    D = str(d)
    E = str(e)

    while game_win == False: 
        #초기화
        game = 0

        #암호 입력
        enter_code = None
        while enter_code != True:
            code = input("암호를 맞추세요 : ")
            if len(code) == 5:
                enter_code = True
            else:
                print("(!)다섯자리 숫자를 입력하세요")
                enter_code = False

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

        #시도 가능 횟수 감소
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

    #게임 재시작 여부
    Q_ = None
    while Q_ != True:
        Q = input(f"다시하겠습니까? ({yes}, {no}) : ")
        if input_letter(Q, yes):
            r = 50
            Q_ = True
            while r != 0:
                print("")
                r -= 1
            game_re = True
        elif input_letter(Q, no):
            Q_ = True
            game_re = False
        else:
            print("(!)입력 오류")
            Q_ = False
