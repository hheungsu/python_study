import re

s_unt   = [63360,36,12]
s_unt_t = ["마일","야드","피트"]
s_dist= []
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"   # 숫자구분을 위한 정규표현식 상수 

while 1==1 :
    wnum = input("input robot walks :(Q/q for stop) ")
    s_dist=[]
    if wnum.upper()=='Q':
        break
    
    if not re.match(IS_NUMERIC,wnum):
        continue
        
    for i in range(len(s_unt)):
        u_val,wnum=divmod(int(wnum),s_unt[i])
        s_dist.append(str(u_val)+s_unt_t[i]+' ') 
    
    s_dist.append(str(wnum)+"인치")     
    print("로봇이 걸어간 거리는 :",s_dist)  