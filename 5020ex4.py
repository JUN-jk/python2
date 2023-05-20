'''
2023.05.20
장준혁
터틀 활용2-입력 , 색 채우기
'''

import turtle
t=turtle.Turtle()
co=turtle.textinput('색상','색상입력')
t.color(co)

r=int(turtle.textinput('반지름','반지름 입력')) #numinput
t.begin_fill()#색 채우기 시작
t.circle(r)#원 그리기
t.end_fill()#색 채우기 끝

input()