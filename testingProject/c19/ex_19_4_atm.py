cnt =0
s_unit     = [50000,10000,5000,1000]        # 금액단위 
s_unit_t   = ["5만원권","1만원권","5천원권","천원권"]
s_rslt     = []                        # 최종결과 

for i in range(4):
    pwd = int(input("비밀번호 입력: "))
    if pwd=='1234':
        cnt=0
        print("환영합니다!")
        break
    else:
        cnt+=1
        print(cnt,"회 잘못 누르셨습니다")      

if cnt ==4:
    exit

n=0
ramt=0
for i in range(len(s_unit)):
    n,ramt=divmod(ramt,s_unit[i])
    s_rslt.append(str(s_unit_t[i])+" "+str(round(n))+'장 ') 
        
print(s_rslt,"외 거스름돈 "+str(round(ramt))+"원")


    