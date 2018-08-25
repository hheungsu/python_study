import re

IS_NUMERIC="^[-+]?\\d+(\\.\\d+)?$"

bof_val=["고요","실바람","남실바람","산들바람","건들바람","흔들바람","된바람","센바람","큰바람","큰셈바람","노대바람","왕바람","싹쓸바람"]

# 입력루프
while 1==1:
    inp = input("풍속을 입력하시요.(숫자만)")
    if not re.match(IS_NUMERIC,inp):
        print("숫자를 입력하세요!")
        continue
    else:
        v=float(inp)
        if v<0:
            print("0이나 양수를 입력하세요!")
            continue
        else:
            if v<1:
                bof_idx=0
            elif v>=1 and v<4:
                bof_idx=1
            elif v>=4 and v<8:
                bof_idx=2
            elif v>=8 and v<13:
                bof_idx=3
            elif v>=13 and v<18:
                bof_idx=4
            elif v>=18 and v<25:
                bof_idx=5
            elif v>=25 and v<31:
                bof_idx=6
            elif v>=31 and v<39:
                bof_idx=7
            elif v>=39 and v<47:
                bof_idx=8
            elif v>=47 and v<55:
                bof_idx=9
            elif v>=55 and v<64:
                bof_idx=10
            elif v>=64 and v<74:
                bof_idx=11
            elif v>=74 :
                bof_idx=12

            print("바람의 세기는 ",bof_val[bof_idx])
            if bof_idx <=3:
                print("산책하기 좋아요!")

    inp = input("그만 입력하려면 Q/q를, 계속하려면 아무키나 입력: ")
    if inp.upper()=="Q":
        break
