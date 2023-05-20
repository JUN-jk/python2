'''
2023.05.20
장준혁
터틀로 집 그리기
'''

import turtle
t=turtle.Turtle()

turtle.bgcolor("Sky blue")

t.color("pink")
t.begin_fill()
t.down()
t.goto(0,-100)
t.goto(100,-100)
t.goto(100,0)
t.goto(0,0)
t.end_fill()

t.color("yellow")
t.begin_fill()
t.goto(50,50)
t.goto(100,0)
t.end_fill()


t.up()
t.color("red")
t.begin_fill()
t.up()
t.goto(35,-100)
t.up()
t.goto(35,-50)
t.up()
t.goto(65,-50)
t.up()
t.goto(65,-100)
t.end_fill()

input()