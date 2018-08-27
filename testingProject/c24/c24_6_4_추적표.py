a=2
while a <=10:
    b=a+1
    c=b*2
    d=c-b+1
    if d==4:
        print(b,",",c)
    elif d==5:
        print(c)
    elif d==8:
        print(a,",",b)
    else:
        print(a,",",b,",",d)
    a+=4