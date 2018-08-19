import math
import re
import os

def cls():
    os.system('cls')
    
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

while 1==1:
    inp=input("input x:")
    if not re.match(IS_NUMERIC,inp):
        print("숫자를 입력하세요")
    else:
        x=float(inp)
        y=0
        if -15>=x or 25<x: 
            y=x-1
        elif x<=-10:
            y=x/math.sqrt(x+30)+(8+x)**2/x+1
        elif x<=0:
            y=abs(40*x)/(x-8)
        elif x<=25:
            if x==9:
                print("9를 입력하면 0으로 나누게 됩니다.계산불가능 ")
                continue
            else:
                y=3*x/math.sqrt(x-9)
        print("y=",y)
