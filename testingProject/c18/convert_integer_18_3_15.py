l_num_alpha=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
l_num_int  =[0,1,2,3,4,5,6,7,8,9]

while 1==1 :
    
    num_alpha=str(input("영문 숫자명을 입력하시요 ")).upper()
    
    if num_alpha.upper() == 'Q':
        print("프로그램을 종료합니다. 안녕~^^ ")
        break
    else:
        for i in range(len(l_num_alpha)):
            if l_num_alpha[i]==num_alpha:
                print(l_num_int[i])
                break
            elif l_num_alpha[i]!=num_alpha and i<len(l_num_alpha)-1:
                continue   
            elif i==len(l_num_alpha)-1:
                print("모르는 숫자입니다.")   
            