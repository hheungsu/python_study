import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

inp = input("x값을 입력하세요: ")

if not re.match(IS_NUMERIC,inp):
    print("숫자를 입력하세요")
elif inp in ("0" , "3"):
    print("x값으로 0이나  3은 입력불가요!")
else:
    x = float(inp)
    
    if x>=0:
        y=(7+x)/(x-3)+(3-x)/x
    else:
        y=40*x/(x-5)+3
                
    print("y=",y)