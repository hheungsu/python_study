#17.4.13 연습문제 (운행 마일수 입력받아 다음 정기점검서비스까지 남은 운행 마일수와 서비스종류출력 : 장기서비스 12000마일,  단기서비스 6000마일) 
# -> 문제를 살짝 바꿔봄  앞으로 받아야할 서비스종류,횟수, 그리고 남은 마일수 

#1.import 패키지
import re

#2.변수선언
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"       # 숫자구분을 위한 정규표현식 상수 
s_unit     = [12000,6000]                  # 서비스별 계산단위 
s_unit_t   = ["장기점검 서비스","단기점검 서비스"]  # 서비스종류
s_rslt     = []                            # 최종결과 

#3. 사용자로부터 마일 입력받아서 앞으로 받을 서비스종류와 횟수 그리고 남은 마일수  출력 (Q 또는 q를 입력하면 중단) 
while 1==1 :
    miles=str(input("운행한 마일을  입력하세요:(중단은 Q또는 q) "))
    
    if miles.upper()=='Q':
        break
    
    if re.match(IS_NUMERIC,miles) :
        rest=float(miles)
    else:
        continue
    
    for i in range(len(s_unit)):
        num,rest=divmod(rest,s_unit[i])
        s_rslt.append(str(s_unit_t[i])+" "+str(round(num))+'회 ') 
        
    print(s_rslt,"외 남은 마일 : "+str(round(rest))+"")
    s_rslt.clear()

print("************** 프로그램을 종료합니다 ***********************")
