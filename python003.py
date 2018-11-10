#터틀 그래픽 선언
import turtle
t = turtle.Turtle()
t.shape("turtle")

#집 크기를 받아와 변수에 저장, input 사용
size = int(input("원하는 집크기를 입력하세요: "))

#집 그리기
t.fd(size)
t.right(90)
t.fd(size)
t.right(90)
t.fd(size)
t.right(90)
t.fd(size)
t.right(90)

#지붕그리기
t.fd(size)
t.left(120)
t.fd(size)
t.left(120)
t.fd(size)
