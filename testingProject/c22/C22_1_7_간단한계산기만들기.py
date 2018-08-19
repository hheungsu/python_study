import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

print("** 계산기 프로그램  **")
i =0
while 1==1:
    if i==3:
        print("프로그램을 종료합니다! 똑바로 숫자를 입력하라고!!")
        break
    
    num1=input("첫번째  숫자를 입력하세요 : ")   
    oper=input("연산자를 입력하세요 : ")
    num2=input("두번째 숫자를 입력하세요 : ")
    
    if not re.match(IS_NUMERIC,num1) or not re.match(IS_NUMERIC,num2):
        print("숫자를 잘못 입력하였습니다.")
        i +=1
        continue
    elif oper not in ("+","-","*","/"):        
        print("연산자를 잘못 입력하였습니다.")
        i +=1
        continue
    elif oper =="/" and num2=="0" :   
        i +=1
        print("0으로 나눌수가 없습니다.")
        continue    
     
    if oper=="+":
        rtn=float(num1)+float(num2)
    elif oper=="-":
        rtn=float(num1)-float(num2)
    elif oper=="*":
        rtn=float(num1)*float(num2)
    elif oper=="/": 
        rtn=float(num1)/float(num2) 
    
    print("계산식 결과: ",num1,oper,num2,"= ",rtn)    
    q=input("그만두려면  Q를 누르고 계속하려면 아무키나 누르시요").upper()
    if q=='Q':    
        break
     