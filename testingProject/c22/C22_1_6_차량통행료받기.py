import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

print("------------------")
print("오토바이(M)")
print("승용차(C)")
print("트럭(T)")
print("------------------")
inp=input("차종을 선택하세요 => ").upper()
    
if inp in ("M","C","T"):  
    if inp=='M':
        rtn=1000
    elif inp=='C':    
        rtn=2000
    else:
        rtn=4000
    
    print("값은: ",rtn)    
else:
    print("올바른 메뉴를 선택하세요![M,C,T]")    
    
