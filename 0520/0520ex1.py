'''
2023.05.20
장준혁         t=turtle.Turtle()  #터틀 별명 만들기
turtle 모듈 활용하기-그래픽 모듈   
'''
import turtle#터틀 모듈을 프로그램에 추가
t=turtle.Turtle() #터틀 별명 만들기
t.shape("turtle") # 커서 모양
t.color 

t.forward(100) # 앞으로 전진
t.left(90) #왼쪽으로 90도 이동
t.forward(50) # 앞으로 전진
t.left(90) #왼쪽으로 90도 이동
t.forward(100) # 앞으로 전진
t.left(90) #왼쪽으로 90도 이동
t.forward(50) # 앞으로 전진
t.left(90) #왼쪽으로 90도 이동

#반복문을 이용한 직사각형 그리기

for i in range(2): #2번 반복(반복조건)
    t.forward(100) # 앞으로 전진
    t.left(90) #왼쪽으로 90도 이동
    t.forward(50) # 앞으로 전진
    t.left(90) #왼쪽으로 90도 이동

#반복문 이용한 정사각형 그리기(한변50)

for i in range(4):#2번 반복(반복조건)
    t.forward(50) # 앞으로 전진
    t.left(90) #왼쪽으로 90도 이동


#정삼각형 그리기
for i in range(3):
    t.forward(100)
    t.left(120)#정삼각형의 외각

#반지름이 100인 원 그리기(r=200)
t.circle(100)

#오각형 그리기(한변100)
for i in range(5):
    t.forward(100)
    t.left(72)




input() # 입력대기
#360/5 72