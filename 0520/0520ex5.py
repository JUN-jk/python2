'''
2023.05.20
장준혁
터틀을 이용한 다각형 그리기
그리기 원하는 다각형을 입력 받아서 해당하는 다각형 그리기
'''
import turtle
t=turtle.Turtle()


c=int(turtle.textinput(".","몆각형"))
co=turtle.textinput('색상','색상입력')
t.begin_fill()

t.color(co)

for i in range(c):
    t.forward(100)
    t.left(360/c)
t.end_fill()
input()







