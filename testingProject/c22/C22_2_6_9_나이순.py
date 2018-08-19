''' 337p 연습문제 9번 
  변형문제
     나이와 이름을 입력받아 그 중에 가장 중간나이인 사람의  입력순번, 이름,나이 출력
    중간 나이에 가장 가까운 사람도 마찬가지로 입력순번, 이름, 나이 출력  
  * 세명만 입력받지 않고 여려명을 받을수 있도록 한다. 단 5개 입력할때마다  그만 입력할지 여부를 묻는다.
  * 종료옵션이 들어가야 한다.
  
'''
#패키지 선언부
import re
import os

#함수  :화면 clear
def cls():
    os.system('cls')

#변수 및 초기화
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" 
list_name =[]
list_age  =[]
diff_age  =[]
rslt      =[]
rslt2     =[]
min_age   =0
max_age   =0
i=0

#이름 및 무게 입력 
while 1==1:
    # 이름, 나이 입력받아서 임시변수에 넣기 
    tmp_name = input("이름:")
    tmp_age  = input("나이:")
    
    if not re.match(IS_NUMERIC,tmp_age):
        print("숫자를 입력해주세요.")
        continue
    
    list_name.append(tmp_name)
    list_age.append(int(tmp_age))
    i +=1
    if i==5:
        if input("그만두려면  Q/q,계속하려면 아무키나 ").upper()=='Q':
            break    
        else:
            i =0
'''가장 어린 사람과 나이 많은 사람 찾고 싶다면
min_index=list_age.index(min(list_age)) 
max_index=list_age.index(max(list_age))
min_age = int(min(list_age))
max_age = int(max(list_age))
'''
#나이가 중간인 사람 찾기
tmp_sum=0
for i in range(len(list_age)):
    tmp_sum +=list_age[i] 

mid_val=tmp_sum/len(list_age)

for i in range(len(list_age)):
    tmp_diff=round(abs(mid_val-list_age[i]))
    diff_age.append(tmp_diff)
    
'''제대로 나오는지 테스트
print(mid_val)
print(diff_age)
'''
    
#중간 나이 검색 
min_diff =min(diff_age) # 차이가 제일 적게나는 diff값 
mid_age  =list_age[diff_age.index(min_diff)] #min_diff로 실제 나이값 찾음

# 가장 중간나이와 제일 가까운 나이를 검색
max_diff =max(diff_age) # 차이가 가장 많이나는 diff값 
min_diff2=max_diff      # max값을 넣어서  비교를 수월하게 하기 위함
for i in range(len(list_age)):
    if diff_age[i]>min_diff: #중간 나이사람 자신은 빼고 최소값 diff를 찾는다.
        if min_diff2 > diff_age[i]: #중간나이 diff를 제외한 중에서  더 작은 diff값 찾으면 
            min_diff2 = diff_age[i] #min_diff2에 넣는다 (가장 가까운 나이값 후보)
        
near_age =list_age[diff_age.index(min_diff2)]

# 가장 중간 나이 가진 사람의 정보를 rslt에 저장
for i in range(len(list_age)):
    if mid_age==list_age[i]:
        rslt.append(str(i+1)+"."+list_name[i]+" "+str(list_age[i])+"세 ")
# 가장 중간 나이와 가장 가까운 나이 가진 사람의 정보를 rslt2에 저장
for i in range(len(list_age)):
    if near_age==list_age[i]:
        rslt2.append(str(i+1)+"."+list_name[i]+" "+str(list_age[i])+"세 ")
      
# 결과값 출력
cls()
print("--------------------------")
print("가장 중간 나이인 사람 ")
for i in range(len(rslt)):
    print(rslt[i])

print("가장 중간 나이에 가까운 사람 ")
for i in range(len(rslt2)):
    print(rslt2[i])
print("--------------------------")


    
'''
테스트 데이터 1                
이름    나이    평균나이    차이    순위
a    30    37    7    2
b    34    37    3    1
c    51    37    14    3
d    10    37    27    5
e    61    37    24    4
                
                
테스트 데이터 2                
이름    나이    평균나이    차이    순위
a    35    36    1    1
b    21    36    15    2
c    35    36    1    1
d    19    36    17    3
e    71    36    35    4
                
                
테스트 데이터 3                
이름    나이    평균나이    차이    순위
a    38    42    4    2
b    21    42    21    3
c    41    42    1    1
d    78    42    36    4
e    38    42    4    2
                
                
테스트 데이터 4                
이름    나이    평균나이    차이    순위
a    38    38    0    1
b    38    38    0    1
c    38    38    0    1
d    38    38    0    1
e    38    38    0    1
                
                
테스트 데이터 5                
이름    나이    평균나이    차이    순위
a    18    36    18    2
b    40    36    4    1
c    40    36    4    1
d    40    36    4    1
e    40    36    4    1
                
                
테스트 데이터 6                
이름    나이    평균나이    차이    순위
a    18    31    13    5
b    40    31    9    3
c    19    31    12    4
d    40    31    9    3
e    19    31    12    4
f    40    31    9    3
g    32    31    1    1
h    35    31    4    2
i    51    31    20    7
j    17    31    14    6
'''
    
    