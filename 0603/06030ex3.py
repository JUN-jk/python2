'''
2023.06.03
장준혁
리턴값이 있는 함수 정의, 호출
'''

def circle_area(radius): #원의 넚이 구하는 함수
    area=radius*radius*3.14 #원의 넚이 계산
    return area #함수를 호출 한 곳에 area 값을 반환

area1=circle_area(5) #반지름이 5인 원의 넓이 구하기
print('원의 넓이:',area1)

area1=circle_area(10) #반지름이 10인 원의 넓이 구하기
print('원의 넓이:',area1)