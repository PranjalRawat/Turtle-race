from turtle import *
from random import randint


penup()
goto(-60, 250)
write('Welcome to April Fool Turtle Race')
goto(-80, 250)
pendown()
goto(130, 250)
penup()
goto(130, 245)
pendown()
goto(-80, 245)
penup()
goto(-200, 220)
write('- This race is organised by Prince of Turtle valley')
goto(-200, 205)
write('- Four turtle are participating in the race named -')
goto(-180, 190)
write('1. BOB')
goto(-180, 180)
write('2. STU')
goto(-180, 170)
write('3. JOHN')
goto(-180, 160)
write('4. ROCKY')
goto(-80, 120)
write('Let\'s Go The race begins')

speed(10)  # drawing speed
penup()
goto(-180, 70)
for step in range(21):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

goto(-200, -50)
write('S\nT\nA\nR\nT')

goto(240, -60)
write('F\nI\nN\nI\nS\nH')
penup()


# first turtle

bob = Turtle()
bob.color('red')
bob.shape('turtle')
bob.penup()
bob.goto(-200, 30)
bob.pendown()
goto(-240, 20)
write('BOB')


# second turtle

stu = Turtle()
stu.color('green')
stu.shape('turtle')
stu.penup()
stu.goto(-200, 0)
stu.pendown()
goto(-240, -10)
write('STU')


# third turtle

john = Turtle()
john.color('yellow')
john.shape('turtle')
john.penup()
john.goto(-200, -30)
john.pendown()
goto(-245, -40)
write('JOHN')


# fourth turtle

rocky = Turtle()
rocky.color('blue')
rocky.shape('turtle')
rocky.penup()
rocky.goto(-200, -60)
rocky.pendown()
goto(-250, -70)
write('ROCKY')
goto(240, 75)


a = int(0)
b = int(0)
c = int(0)
d = int(0)
t1 = int(0)
t2 = int(0)
t3 = int(0)
t4 = int(0)


for turn in range(210):
    t1 += a
    t2 += b
    t3 += c
    t4 += d
    a = randint(1, 3)
    bob.forward(a)
    b = randint(1, 3)
    stu.forward(b)
    c = randint(1, 3)
    john.forward(c)
    d = randint(1, 3)
    rocky.forward(d)


goto(-20, -120)
if t1 > t2 and t1 > t3 and t1 > t4:
    write('!!!! BOB WINS !!!!')
elif t2 > t1 and t2 > t3 and t2 > t4:
    write('!!!! STU WINS !!!!')
elif t3 > t1 and t3 > t2 and t3 > t4:
    write('!!!! JOHN WINS !!!!')
elif t4 > t1 and t4 > t2 and t4 > t3:
    write('!!!! ROCKY WINS !!!!')
else:
    write('-----------DRAW-----------')
done()
