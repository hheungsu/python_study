# 입력루프
while 1==1:
    age = int(input("나이를 입력하시요."))

    if age <18:
        print("해당되지 않는 나이입니다.")
        continue

    wgt = float(input("몸무게를 입력하시요."))
    hgh = float(input("키를 입력하시요."))

    # BMI계산
    bmi=(wgt/hgh**2)*100*100
    print(bmi)
    if bmi<15:
        print("매우 마름")
    elif bmi>=15 and bmi<16:
        print("마름")
    elif bmi>=16 and bmi<18.5:
        print("저체중")
    elif bmi>=18.5 and bmi<25:
        print("보통")
    elif bmi>=25 and bmi<30:
        print("과체중")
    elif bmi>=30 and bmi<35:
        print("경도비만")
    elif bmi>=35:
        print("고도비만")

    inp = input("그만 입력하려면 Q/q를, 계속하려면 아무키나 입력: ")
    if inp.upper()=="Q":
        break
