from turtle import *

value = 500

while value > 0:
    forward(value)
    left(90)
    value -= 10
    write(value)
mainloop() 