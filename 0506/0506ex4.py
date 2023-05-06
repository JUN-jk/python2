'''
2023.05.06
장준혁
반복문 - while
'''
#1~10까지 출력하기

i=1 #반복 변수 초기화
while i <= 10:  # 반복 조건
    print(i, end=" ") # i 출력
    i=i+1 #i 1씩 증가(증감식)
    
# 1~10까지 합계 구하기
A=1
B=1
while A<10:
    A=A+1
    B=B+A
print()
print()
print(B)
    
#1~입력받은 숫자 까지 합계 구하기
C=1
B=int(input('숫자 입력'))
A=1
while A<B:
    A=A+1
    C=C+A
print()
print()
print(C)