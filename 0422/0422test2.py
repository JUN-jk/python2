'''
2023.04.22
장준혁
# 문제
    반지름이 5인 원의 넓이 구하기
#문제분석
    변수-반지름(radius),원의 넚이(area)
    수식- radius*radius*3.14(원주율) , radius**2*3.14
#알고리즘
    1.변수 선언
        radius=5
    2.원의 넓이 계산
        area=radius*radius*3.14
    3.결과출력
'''
# (반지름)×(반지름)×(원주율(3.14)) = 원의 넚이 (area)

radius=5
area=radius*radius*3.14 #원의 넓이
print('반지름이 {}인 원의 넓이는 {}이다'.format(radius,area))


