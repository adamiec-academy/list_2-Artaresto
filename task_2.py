from turtle import forward, left, right, speed, penup, pendown, exitonclick 
import random

speed("slow")
a = random.randint(1, 5)

for _ in range(random.randint(5, 20)):
    forward(20)
    left(90)
    forward(a)
    left(90)
    forward(20)
    left(90)
    forward(a)
    left(90)
    penup()
    forward(40)
    pendown()
    a += random.randint(-5,  30)

exitonclick()
