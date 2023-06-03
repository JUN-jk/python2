'''
2023.06.03
장준혁
사각형 그리기  / 함수로 3개의 사각형 그리기
'''

import turtle

t=turtle.Turtle()

#t.speed(100) #빠르게 보고싶으면 이거

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

t.up()
t.goto(-200,0)
t.down()
square(100)

t.up()
t.goto(0,0)
t.down()
square(100)

t.up()
t.goto(200,0)
t.down()
square(100)

input()