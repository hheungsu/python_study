tot_num =50000
dec_rat =10
iyear =0
while tot_num>20000:
    tot_num -=tot_num*dec_rat*0.01
    iyear +=1

print(iyear)


