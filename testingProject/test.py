import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 

s=input("write setence:")
#print(s[-1])
#print(s[0])
if s[0].upper()==s[0] and s[-1] in ('.','?','!'):
    print("이상없음")
else:
    print("잘못 씀")