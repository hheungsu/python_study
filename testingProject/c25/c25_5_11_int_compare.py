'''
    문제: 26강  연습문제 5-11 
    사용자로부터 start와 finish 두개 정수를 입력받은후 , start와 finish 사이에 5의 배수인
    모든 정수를 출력하는 순서도와  파이썬 프로그램을 작성하여라. 
    먼저 ,프로그램의 시작부분에서 start변수값이 finish 변수값보다 큰 지를 검사해야 한다.
    이런경우가 발생하면 두 값을 서로 맞바꾼다.       
'''
rslt=[]
while True:
    try:
        start =int(input("start 정수값을 입력하시요:"))
        finish=int(input("finish 정수값을 입력하시요:"))
    except ValueError:
        ("정수인 숫자를 입력하세요:")
        continue
    else:
        if start>finish:
            tmp_int=finish
            finish=start
            start=tmp_int
             
        for i in  range(start,finish+1):
            if i%5==0:
                rslt.append(i)
        print("입력한 정수 ",start," 와 ",finish," 사이의 숫자 중  5의 배수는 ")
        print(rslt)    
        rslt.clear()
        if "Q"==input("그만두려면  Q/q를 누르고 계속하려면 그외 아무거나:").upper():
            break
                 
                    
                    