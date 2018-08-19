import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

inp = input("x값을 입력하세요: ")

if not re.match(IS_NUMERIC,inp):
    print("숫자를 입력하세요")
elif inp in ("0","4"):
    print("x값으로 0이나 4는 입력불가요!")
else:
    x = float(inp)
    y=(5+x)/x - (x+9)/(x-4)        
    print("y=",y)