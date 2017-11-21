"""planets.py:'planets.py' is to present a animation of a simplified planetary 
system.

__author__ = "Zhou Yangfan"
__pkuid__  = "1600017735"
__email__  = "pkuzyf@pku.edu.cn"
"""
import turtle
import math

def planets(alist):
    """This fuction can be used to present a animation of a simplified planetary 
    system.The formal parameter of this function should be a list of turtles wh- 
    -ich you wanna use to represent planets,such as[turtle1,turtle2,...].And the
    list can contain any number of turtles.However,you must put the fixed star 
    as the first one and put the rest in order of distance to the fixed star.
    """
    num = len(alist)
    for i in range(num): 
        t = alist[i]
        t.shape("circle")
        t.speed(0)
        t.pu()
        x = i * (i + 20) ** 1.2 # set the scale of the orbit of each planet.(the fuction is assumed casually...)
        if i % 2 == 1: # set the initial position for each planet according to whether the ordinal number of it is odd or even.
            t.goto(-x * 4 / 5, -x)
        else:
            t.goto(x / 1.2, 0)
            t.lt(90)
        t.pd()
    
    for i in range(1000):
        for x in range(1, num):
            t = alist[x]
            r = 2 * x * (x + 20) ** 1.2 # set the scale of the orbit of each planet.
            a = 2 * math.pi * i / (360 / (num - x))  # "num - x" is to control the speed of each planet.
            l = 2 * math.pi * r / (360 / (num - x))
            if x % 2 == 1:
                t.fd(abs(math.cos(a)) * l)
            else:
                t.fd(abs(math.sin(a)) * l)
            t.lt(num - x)

def main():
    sun, mercury, venus, earth, mars, saturn, jupiter = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
    alist0=[sun, mercury, venus, earth, mars, saturn, jupiter]
    sun.color("orange")
    mercury.color("grey")
    venus.color("yellow")
    earth.color("blue")
    mars.color("red")
    saturn.color("brown")
    jupiter.color("violet")
    
    planets(alist0)
    
if __name__ == '__main__':
    main()
