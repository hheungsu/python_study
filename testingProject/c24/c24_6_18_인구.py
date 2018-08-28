tot_num =30000
dec_rat =3
iyear =0
while tot_num<=100000:
    tot_num +=tot_num*dec_rat*0.01
    iyear +=1

print(iyear)


