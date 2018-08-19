#13.2.6 연습문제 (ATM기 입력금액을 5만원 1만원 1천원 단위로 환산하여 메세지출력
#1.import 패키지
import re

#2.변수선언
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"   # 숫자구분을 위한 정규표현식 상수 
s_unit     = [50000,10000,1000]        # 금액단위 
s_unit_t   = ["5만원","만원","천원"]
s_rslt     = []                        # 최종결과 

#3. 사용자로부터  금액읍 입력받아 금액단위로 출력 (Q 또는 q를 입력하면 중단) 
while 1==1 :
    samt=str(input("금액을 입력하세요:(중단은 Q또는 q) "))
    
    if samt.upper()=='Q':
        break
    
    if re.match(IS_NUMERIC,samt) :
        ramt=float(samt)
    else:
        continue
    
    for i in range(len(s_unit)):
        n,ramt=divmod(ramt,s_unit[i])
        s_rslt.append(str(s_unit_t[i])+" "+str(round(n))+'장 ') 
        
    print(s_rslt,"외 거스름돈 "+str(round(ramt))+"원")
    s_rslt.clear()

print("이용해주셔서 캄사요 ^ㅛ^ 거스름돈은 내꺼 ")
