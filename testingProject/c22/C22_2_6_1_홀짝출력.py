import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

inp1 = input("숫자1을 입력하세요: (정수만) ")

if not re.match(IS_NUMERIC,inp1):
    print("숫자가 아닙니다. 숫자입력하세요")
else:
    inp2 = input("숫자2를 입력하세요: (정수만) ")   
    if not re.match(IS_NUMERIC,inp2):
        print("숫자가 아닙니다. 숫자입력하세요")
    else:
        num1=int(inp1)
        num2=int(inp2)
        if num1%2==0 and num2%2==0:
            print("둘다 짝수에요.")
        else:
            print("특별하지 않네요.")
               
