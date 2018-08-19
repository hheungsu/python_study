import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

print("------------------")
print("1.갤런을 리턴으로 변환:")
print("2.리턴을 갤런으로 변환:")
print("------------------")

inp=input("메뉴를 선택하세요 => ")
    
if inp in ("1","2"):  
    val=input("양을 입력하세요")
    
    if re.match(IS_NUMERIC,val):
        rtn=0
    
        if inp=='1':
            rtn=float(val)*3.785
        elif inp=='2':    
            rtn=float(val)/3.785
            
        print("값은: ",rtn)    
    else:
        print("숫자가 아닙니다. 잘못입력하였습니다.")
else:
    print("올바른 메뉴를 선택하세요![1,2]")    
    
