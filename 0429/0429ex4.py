'''
2023.04.29
장준혁
#문제정의
    입력받은 정수가 짝수이면 "짝수 출력", 아니면 "홀수"출력하는 프로그램
#문제분석
    변수: num
#알고리즘
1.변수선언
    num에 정수 입력
2.프로그램 논리
    if num%2 == 0
3.결과출력

'''

num=int(input('정수 입력:')) # 정수 입력

if num%2 == 0 : # 조건식
    print('짝수') # 조건이 짝수라면
else :
    print('홀수') # 조건이 홀수라면
