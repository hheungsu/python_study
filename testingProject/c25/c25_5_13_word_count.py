'''
문제: 26강  연습문제 5-13 
    사용자로부터 문자열 메세지를 입력받은 후, 이 메세지에 포함된 단어 수를 출력하는 파이썬 프로그램을 작성하여라.
    예를 들어, 입력된 문자열 메세지가  "My name is Bill Bouras" 이면 "입력된 메시지는 다섯 개의 단어를
    포함하고 있습니다." 가 출력된다.
'''

cnt=1
inp=input("문장을 입력하시요:")
for w in inp:
    if w ==" ":
        cnt+=1

print("입력된 메세지 ",inp,"는 총  ",cnt,"개의 단어를 포함하고 있습니다.")
