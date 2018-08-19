import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

while 1==1:
    inp=input("세자리 정수를 입력하시요.")
    if not re.match(IS_NUMERIC,inp):
        print("숫자가 아닙니다.")
        continue
    elif len(inp)!=3 and float(inp)!=inp:
        print("세자리 정수가 아닙니다.") 
        continue
    
    n1 = int(inp[0])
    n2 = int(inp[1])
    n3 = int(inp[2])
    
    ams=str(n1**3+n2**3+n3**3)
    print("입력한 계산식은 ")
    print(inp+"="+inp[0]+"**3+"+inp[1]+"**3+"+inp[2],"**3")
    if ams==inp:
        print("암스트롱 숫자입니다!")
    else:
        print("평범한 숫자입니다.")
        
    inp2=input("계속하시겠습니까? (종료는  Q/q 계속하시려면 그외 아무키나 누르세요.)")
    if inp2.upper()=='Q':
        print("프로그램을 종료합니다.")
        break 
    
        
    