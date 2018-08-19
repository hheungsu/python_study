a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

c=a*b+c
if c>0:
    c/=2
    if a>b:
        a*=2
        b*=2
    else:
        c/=20
        if c<=10:
            b*=2
else:
    c/=3
    c/=20
    if c<=10:
        b*=2

print("a,b,c=",a,b,c)
        