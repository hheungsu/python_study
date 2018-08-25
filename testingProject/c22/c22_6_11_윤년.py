import re

IS_NUMERIC="^[-+]?\\d+(\\.\\d+)?$"
i_year  =0
i_mon   =0
rslt_days=''

inp_yyyymm=input("년월을 입력하세요:(YYYYMM)")

if not re.match(IS_NUMERIC,inp_yyyymm):
    print("잘못된 입력입니다.")
else:
    i_year = int(inp_yyyymm[0:4])
    i_mon  = int(inp_yyyymm[4:])

    if i_mon in (4,6,9,11):
        rslt_days='30'
    elif i_mon==2:
        if ((i_year %4==0)  and (i_year %100!=0)) or (i_year%400==0):
            #print("윤년")
            rslt_days='29'
        else:
            #print("윤년아님")
            rslt_days='28'
    else:
        rslt_days='31'

    print("입력하신 ",inp_yyyymm,"의 남은 일수는 [",rslt_days,"] 입니다")
