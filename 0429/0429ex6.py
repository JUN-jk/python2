'''
2023.04.29
장준혁
#문제 정의
    숫자를 입력 받아서 , 양수 ,음수, 0을 구분하는 프로그램 만들기
#문제 분석
    변수
#알고리즘
    1.변수선언 
        num
    2.프로그램 논리
        if num > 0 :
            print('양수')
        el num < 0 :
            print('음수')
        else num == 0 :
            print('0입니다')
        
'''

num=int(input('숫자 입력: '))

if num > 0 :
    print('양수')
elif num < 0 :
    print('음수')
else :
    print('0입니다')