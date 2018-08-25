import re

pay=1000 #임의 설정
vat=19   #부가세
IS_NUMERIC="^[-+]?\\d+(\\.\\d+)?$"

dis_ratio =0
inp =input("구매수량을 입력하시요:")


if not re.match(IS_NUMERIC,inp):
    print("숫자를 입력하시요:")
else:
    inum=float(inp)

    if inum < 0:
        print("양수를 입력하세요.")

    if   inum <50:
        dis_ratio=0
    elif inum >=50  and inum <100:
        dis_ratio=1
    elif inum >=100 and inum <200:
        dis_ratio=2
    elif inum >=200:
        dis_ratio=3

    dis_amt   = pay*dis_ratio*0.01
    final_amt = pay + pay*vat*0.01 - dis_amt


    print("총금액   = ",pay,"원")
    print("할인율   = ",dis_ratio,"%")
    print("부가세   = ",vat,"%")
    print("최종금액 = ",final_amt,"원")

    if dis_amt >0 :
        print("할인금액은 ",dis_amt,"원 입니다.")
    else:
        print("할인혜택이 없습니다.")
