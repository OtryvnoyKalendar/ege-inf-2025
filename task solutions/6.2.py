from turtle import *

# базовые настройки
k = 30
left(90)
speed(0)
tracer(0)
screensize(2000, 2000)
onkeypress(bye, "Escape")
listen()

down()
for _ in range(7):
    fd(10 * k)
    right(120)

# сетка
up()
a = 30
for x in range(-a, a):
    for y in range(-a, a):
        goto(x * k, y * k)
        dot(4, "red")

# базовые настройки
update()
done()

"ответ: 38"
