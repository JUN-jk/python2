'''
2023.06.03
장준혁
삼각형 만들기 함수를 이용하여 
'''

import turtle

t=turtle.Turtle()

t.speed(100)

def n_polygon(n,length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)
        
for i in range(100):
    t.left(20)
    n_polygon(6,100)    
        
input()