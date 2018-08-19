a=int(input("a:"))
b=int(input("b:"))
y=a*b

if y>0:
    y-=1
else:
    y+=10

if y>0:
    y/=2
else:
    y*=2

print("y=",y)
########################################
a = float(input()) 
b = float(input()) 
y = a * b 
 
if y > 0:     
    y -= 1     
    y /= 2 
else:     
    y +=10     
    if y > 0:         
        y /= 2     
    else:         
        y *= 2 

print("y=",y)