#무늬 
import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length=10

while length <500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length +=5

#알수 있었던것
#turtle클래스
#문자의 배열
#tutle의 이동fd, 팬 띄우기 up
