'''
2023.05.13
장준혁
#문제정의
    정수를 입력받아서 직각삼각형 별 출력하기
#문제분석
    변수 - 정수(num),줄반복(i),별 찍기반복(j)
#알고리즘
    1.변수 초기화
        num에 줄수 입력받기
    2.논리(중첩반복)
        (줄반복) for i in range(1,num+1):
            (별 찍기 반복)for  j inrange(1,i+1):
                별 출력
'''
num=int(input('num입력받기'))

for i in range(1,num+1): # 불 반복
    for j in range(1,i+1): # 별 찍기 반복
        print('*',end=" ") # 별 출력
    print()# 줄 바꿈