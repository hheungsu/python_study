inp_alpha=input("6개의 알파벳을 입력하시요: (주의! 더 입력하면 앞에서부터 6자만 들어감)")

if inp_alpha[0].upper()==inp_alpha[0] and inp_alpha[2].upper()==inp_alpha[2] and inp_alpha[4].upper()==inp_alpha[4]:
    print (inp_alpha,"는 두개의 문자마다 대문자입니다.")
elif inp_alpha[1].upper()==inp_alpha[1] and inp_alpha[3].upper()==inp_alpha[3] and inp_alpha[5].upper()==inp_alpha[5]:
    print (inp_alpha,"는 두개의 문자마다 대문자입니다.")
else:
    print ("이도 저도 아닙니다.")
