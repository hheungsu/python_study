import re

IS_NUMERIC="^[-+]?\\d+(\\.\\d+)?$"

# 입력루프
while 1==1:
    inp = input("수입금액을 입력하시요.")
    if not re.match(IS_NUMERIC,inp):
        print("숫자를 입력하세요!")
        continue
    else:
        money=float(inp)

        inp2 = input("자녀수를 입력하세요.")
        if not re.match(IS_NUMERIC,inp):
            print("숫자를 입력하세요!")
            continue
        else:
            num=int(inp2)

            if money <=800:
                tax_ratio=10
            elif money >800 and money <=3000:
                tax_ratio=15
            elif money >3000 and money <=7000:
                tax_ratio=25
            elif money >7000:
                tax_ratio=30

            if num >0:
                tax_ratio=tax_ratio-2

            tot_tax= money*tax_ratio*0.01
            print("총 납부세액은 ",tot_tax,"원 입니다.")

    inp = input("그만 입력하려면 Q/q를, 계속하려면 아무키나 입력: ")
    if inp.upper()=="Q":
        break
