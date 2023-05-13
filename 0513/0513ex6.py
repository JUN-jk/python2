'''
2023.05.13
장준혁
#문제정의
    정수 2개와 연산자(+,-,*,/)1개 입력 받아서 사칙연산을 수행하는 계산기 프로그램 만들기
#문제분석
    변수 num1 ,num2 ,op # op는 연산자 의미다
#알고리즘
num1,num2 입력


'''

num1=int(input('num1입력 : '))
num2=int(input('num2입력 : '))
op=input('op입력(+,-,*,/)')

if op=='+':
    print('{}{}{}={}'.format(num1,op,num2,num1+num2))




