'''
2023.05.20
장준혁
터틀 모듈 활용
'''

import turtle
t=turtle.Turtle()
t.shape("classic")#터틀 모양
t.color("pink") #선의 색상
t.width(2) # 선의 굵기

t.down() #팬 내리기
t.goto(100,0) #100,0으로 이동하면서 선 그리기
t.up()
t.goto(0,200) #0,200으로 선을 그리지 않으면서 이동하기
t.down()
t.goto(100,200)
t.up()
t.goto(0,200)
t.down()
t.goto(0,0)
t.up()
t.goto(100,200)
t.down()
t.goto(100,0)

input()