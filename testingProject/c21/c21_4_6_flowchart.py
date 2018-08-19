x=int(input("x: "))
y=int(input("y: "))

if x!=100 or y<=10:
    z=int(input("z:"))
    if z<=x+y:
        x=x-3
        y=x+4

    
print("x,y=",x,y)