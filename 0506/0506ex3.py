'''
2023.05.06
장준혁
반복문 - for
'''
#시퀸스 변수로 반복문 범위 정하기

for i in[1,2,3,4,5,6,7,8,9,10]: # 반복 조건
    print(i,end=' ') #i 출력
    
print() # 줄 바꿈

#range() 함수로 반복문 범위 정하기
for i in range(1,11): # 반복 조건
    print(i,end=' ') # i 출력
    
#1~10까지 합계를 출력하시오
sum=0 # 합계 저장
 
for num in range(1,11):
    sum=sum+num
    
print("1~10 까지의 합계는 {}이다".format(sum))

#1~입력받은 숫자까지 합께 구하기

num=int(input('숫자 입력 :'))
sum=0 # 합계 저장
 
for num in range(1,num+1):
    sum=sum+num
    
print("1~{} 까지의 합계는 {}이다".format(num,sum))

total=0 # 합계
su=int(input("합계를 구하기 원하는 숫자")) # 정수 입력

for i in range(1,su+1):
    total=total+su

print('1~{}까지의 합계는 {}이다'.format(su,total))
