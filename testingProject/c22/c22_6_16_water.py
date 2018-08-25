import re

IS_NUMERIC="^[-+]?\\d+(\\.\\d+)?$"
tax=10 #지방세

# 입력루프
while 1==1:
    inp = input("물사용량을 입력하시요.")

    if not re.match(IS_NUMERIC,inp):
        print("숫자를 입력하세요!")
        continue
    else:
        w_usage=float(inp)

        if w_usage <0:
            print("0또는 양수를 입력하세요.")
        else:
            if w_usage <=10:
                fee=3000*w_usage
            elif w_usage >=11 and w_usage <=20:
                fee=5000*w_usage
            elif w_usage >=21 and w_usage <=35:
                fee=7000*w_usage
            elif w_usage >=36:
                fee=9000*w_usage

            fee+fee*tax*0.01
            print("수도세 요금은 = ",fee,"원 입니다.")

    inp = input("그만 입력하려면 Q/q를, 계속하려면 아무키나 입력: ")
    if inp.upper()=="Q":
        break
