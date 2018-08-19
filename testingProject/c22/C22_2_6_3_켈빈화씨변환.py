import re
import os

def cls():
    os.system('cls')

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

print("######## 온도변환 프로그램 #########")

#전체 loop
while 1==1:
    #메뉴출력
    print("1.켈빈온도를 화씨온도로 변환")
    print("2.화씨온도를 켈빈온도로 변환")
    print("3.화씨온를 섭씨온도로 변환")
    print("4.섭씨온도를 화씨온도로 변환")
    
    #메뉴입력받아 계산로직 들어간다. 만약 종료하고 싶으면  Q또는 q를 입력하여 종료한다.
    inp = input("메뉴를 입력하세요: (1~4):종료는 Q/q ")
    
    if inp.upper()=="Q":
        print("프로그램을 종료합니다.")
        break
    # 메뉴를 1~4가 아닌 다른 숫자나 문자등을 입력하면 메뉴로 돌아가서 다시 선택한다.
    if inp not in ("1","2","3","4"):
        cls()
        print("메뉴는 1~4중에 한가지입니다.")
        continue
    # 메뉴를 1~4중에 하나를 입력했다면 계산로직을 들어간다.
    else:
        
        # 입력 루프 (계속 입력받을수 있도록), 메뉴로 돌아가려면 B 또는 b를 누른다.
        while 1==1:
            temp=input("온도를 입력하세요. 메뉴로 돌아가려면  B 또는 b를 누르세요")
            if temp.upper()=='B':
                break
            if not re.match(IS_NUMERIC,temp):
                print("온도는 숫자를 입력해야합니다.")
                continue
            else:
                if inp=="1":
                    rslt="1.켈빈온도-> 화씨온도: "+str(18*float(temp)-459.67)
                elif inp=="2":
                    rslt="2.화씨온도-> 켈빈온도: "+str((float(temp)+459.67)/1.8)
                elif inp=="3":
                    rslt="3.화씨온도-> 섭씨온도: "+str(5*(float(temp)-32)/9)
                elif inp=="4":      
                    rslt="4.섭씨온도-> 화씨온도: "+str(9*float(temp)/5+32)
                    
                print(rslt)