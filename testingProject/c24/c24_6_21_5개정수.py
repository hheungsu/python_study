import re

#상수
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 
#변수 
l_int=[] #입력 정수 리스트
r_int=[] #5로 시작하는 세자리 정수리스트
f_num=1  #최종결과값 

#1.정수만 5개 입력받는데, 숫자 아니면 계속 반복시켜서 5개의 정수만 받도록 한다.
for i in range(5):
    while True:
        inp =input(str(i+1)+"번째 정수입력하시요:")
        if re.match(IS_NUMERIC,inp): 
            break
        else:
            print("아놔 숫자를 입력하라고  (--+):")
    l_int.append(int(inp))

#2.입력한 값중에 5로 시작하는 세자리 숫자 골라내기  
for i in range(len(l_int)):
    tmp_num=str(l_int[i])
    #print(tmp_num[0:1])    
    if tmp_num[0:1]=='5' and len(tmp_num)==3:
        r_int.append(int(tmp_num))

#3. 입력한 값을 계산하여 출력한다.
for i in range(len(r_int)):
    f_num *=r_int[i]

#4.최종결과값
print("5로 시작하는 세자리 숫자는 :",r_int)
print("곱한 최종결과는 :",str(f_num))   
    