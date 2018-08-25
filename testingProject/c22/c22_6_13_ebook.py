import re

IS_NUMERIC="^[-+]?\\d+(\\.\\d+)?$"
book_amt =10000
dis_ratio =0
total_amt =0
final_amt =0
bk_num=input("구매도서의 수를 입력하시요:")

if not re.match(IS_NUMERIC,bk_num):
    print("숫자를 입력하시요:")
else:
    ibk_num=int(bk_num)

    if   ibk_num >=3  and ibk_num <=5:
        dis_ratio=10
    elif ibk_num >=6  and ibk_num <=9:
        dis_ratio=15
    elif ibk_num >=10 and ibk_num <=13:
        dis_ratio=20
    elif ibk_num >=14 and ibk_num <=19:
        dis_ratio=27
    elif ibk_num >=20:
        dis_ratio=30

    total_amt = (ibk_num*book_amt)
    final_amt = total_amt - total_amt*(dis_ratio/100)

    print("도서구입건수는 ",ibk_num,"권이고 할인율은 ",dis_ratio,"%이고 총 구매금액은 ",final_amt,"원입니다.")
