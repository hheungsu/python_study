import re 

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"   # 숫자구분을 위한 정규표현식 상수 
x=str(input("x: "))

if re.match(IS_NUMERIC,x):
    if int(x)%10==0:
        print("마지막 자릿수는 0입니다.")
    elif int(x)%10==1:
        print("마지막 자릿수는 1입니다.")
    else:
        print("특별하지 않네요.")
else:
    if x=="Exit" :
        print("끝")
    else:
        print("올바르지 않은 수입니다.")

exit