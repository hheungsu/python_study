import re

#상수
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 
#변수 
l_int=[] #입력 정수 리스트
r_int=[] #음수로 시작하는 정수
f_num=1  #최종결과값 

while True:
    tot_num=input("몇개입력할지 숫자를 입력하시요:")
    if re.match(IS_NUMERIC,tot_num):
        break
    else:
        print("아놔 숫자를 입력하라고  (--+):")

for i in range(int(tot_num)):
    while True:
        inp =input(str(i+1)+"번째 정수입력하시요:")
        if re.match(IS_NUMERIC,inp): 
            break
        else:
            print("아놔 숫자를 입력하라고  (--+):")
    l_int.append(int(inp))

#2.입력한 값중에 음수로 시작하는 숫자 골라내기 
for i in range(len(l_int)):
    if l_int[i]<0:
        r_int.append(l_int[i])

#3. 입력한 값을 계산하여 출력한다.
for i in range(len(r_int)):
    f_num *=r_int[i]

#4.최종결과값
print("음수의 리스트는 :",r_int)
print("곱한 최종결과는 :",str(f_num))   
    