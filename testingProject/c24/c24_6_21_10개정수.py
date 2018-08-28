import re

#상수
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 
#변수 
l_int=[]   #입력 정수 리스트
r_int_1=[] #홀수로 시작하는 세자리 정수리스트
r_int_2=[] #짝수로 시작하는 세자리 정수리스트
f_num_1=0  #홀수 최종결과값 
f_num_2=0  #짝수 최종결과값 

#1.정수만 5개 입력받는데, 숫자 아니면 계속 반복시켜서 5개의 정수만 받도록 한다.
for i in range(10):
    while True:
        inp =input(str(i+1)+"번째 정수입력하시요:")
        if re.match(IS_NUMERIC,inp): 
            break
        else:
            print("아놔 숫자를 입력하라고  (--+):")
    l_int.append(int(inp))

#2.입력한 값중에  짝수와 홀수 구분  
for i in range(len(l_int)):
    if l_int[i]%2!=0:
        r_int_1.append(l_int[i])
    else:
        r_int_2.append(l_int[i])

#3. 입력한 값을 계산하여 출력한다.
for i in range(len(r_int_1)):
    f_num_1 +=r_int_1[i]
for i in range(len(r_int_2)):
    f_num_2 +=r_int_2[i]    

#4.최종결과값
print("홀수로 시작하는  숫자는 :",r_int_1)
print("홀수만 더한 최종결과는 :",str(f_num_1))   
print("짝수로 시작하는  숫자는 :",r_int_2)
print("짝수만 더한 최종결과는 :",str(f_num_2))   
    