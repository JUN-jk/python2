'''
2023.04.29
장준혁
조건이 여러 개인 경우의 조건문 연습
#문제 정의
    점수가 90이상이면 "A",
    점수가 80이상 90미만 "B",
    점수가 70이상 80미만이면 "C",
    점수가 60미만 이면 "F"를 출력하는 시스템
#문제 분석
    변수:
#알고리즘
    1.변수 선언
    2.프로그램 논리(선택)
 if score>=90 :
        print('A')
elif score>=80 :
    print('B')
elif score>=70 :
    print('c')
else :
    print('F')
    3.결과 출력
'''

score=int(input('당신의 점수:'))

if score>=90 :#조건식 1
    print('A')# 조건식 2# 조건1이 참일때만 실행
elif score>=80 :# 조건식 2
    print('B')#조건식 3#조건 1은 거짓, 조건 2 참일때만 실행
elif score>=70 :#조건식 3
    print('c')#조건 2거짓,조건 3 참 일때만 실행
else :
    print('F')#조건 1,조건 2,조건 3이 모두 거짓일때 실행


