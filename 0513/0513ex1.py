'''
2023.05.13
장준혁
#문제정의
    출력을 원하는 단을 입력받아서 구구단 출력하기
#문제분석
    변수 : dan, i
#알고리즘
    1.변수 선언 , 변수 초기화
        dan . i(반복횟수) , dan 변수에 정수 입력
    2.프로그램 논리 : (반복-while)
        (반복조건) while i <=9:
            구구단 출력
'''

dan = int(input('단을 입력하시오 : '))
i=1 # 반복변수 초기화

print("**{}**".format(dan))

while i <=9: # 반복 조건
    print("{}*{}={}".format(dan,i,dan*i)) # 구구간
    i=i+1  #i 1증가
    
#for
print()# 한줄띄우기
dan = int(input('단을 입력하시오 : '))


print("**{}**".format(dan))

for i in range(1,10): # 반복 조건
    print("{}*{}={}".format(dan,i,dan*i)) # 구구간

