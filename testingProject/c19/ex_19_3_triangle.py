#1.세변의 길이 입력 
a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))

#2.삼각형 가능한지 체크  : 어느 한변의 길이는 다룬 2변의 길이의 합보다 짧다.
if not (a<b+c and b<c+a and c<a+b):
    print("삼각형이 될수 없습니다.")
#3.삼각형이 가능하다면 정삼각형,직각삼각형 또는 그외 삼각형인지 구별하기
else:
    if a==b==c: #정삼각형이면 
        print("정삼각형!")
    elif (a**2==b**2+c**2) or (b**2==c**2+a**2) or (c**2==a**2+b**2):
        print("직각삼각형!")
    else:
        print("보통삼각형!")     