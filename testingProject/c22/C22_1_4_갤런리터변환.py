print("------------------")
print("1.갤런을 리턴으로 변환:")
print("2.리턴을 갤런으로 변환:")
print("------------------")

inp=input("메뉴를 선택하세요 => ")

val=float(input("양을 입력하세요"))
rtn=0

if inp=='1':
    rtn=val*3.785
elif inp=='2':    
    rtn=val/3.785

print("값은: ",rtn)