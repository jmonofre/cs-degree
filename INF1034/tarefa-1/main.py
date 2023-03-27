import turtle

t = turtle.Turtle()

t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.penup()
t.goto(0, -400)
t.pendown()
t.goto(0, 400)

t.penup()
t.goto(50, 50)
t.pendown()
t.color("blue")
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("red")
for i in range(3):
    t.forward(50)
    t.right(120)
t.penup()
t.goto(-100, -150)
t.pendown()
t.color("green")
t.circle(50)
t.penup()
t.goto(50, -50)
t.pendown()
t.color("purple")
for i in range(5):
    t.forward(50)
    t.right(144)

t.penup()
t.color("orange")
t.goto(-250, -250)
t.pendown()
for i in range(40):
    t.forward(2*i/2)
    t.right(30)

t.reset()

t.penup()
t.goto(-200, 200)
t.pendown()
t.color("red")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.end_fill()
t.penup()
t.goto(-160, 175)
t.color('green')
t.pendown()
for i in range(5):
  t.forward(20)
  t.right(144)

t.penup()
t.goto(200, 200)
t.pendown()
t.color("red")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.end_fill()
t.penup()
t.goto(240, 160)
t.color('white')
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.goto(250, 160)
t.color('red')
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()
t.goto(240, 180)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(20)
  t.right(144)


t.penup()
t.goto(-100, 0)
t.color('green')
t.pendown()
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
t.goto(0, 0)
t.color('yellow')
t.begin_fill()
t.right(27)
t.forward(12500**0.5)
t.right(127)
t.forward(12500**0.5)
t.right(53)
t.forward(12500**0.5)
t.right(127)
t.forward(12500**0.5)
t.end_fill()

t.goto(15, -77)
t.color('blue')
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(30, -35)
t.color('white')
t.pendown()
t.begin_fill()
t.right(15)
t.bk(65)
t.right(90)
t.forward(10)
t.lt(90)
t.forward(65)
t.lt(90)
t.forward(10)
t.end_fill()

t.penup()
t.goto(-10, -30)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(10)
  t.right(144)

t.penup()
t.goto(-10, -60)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

t.penup()
t.goto(-20, -67)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

t.penup()
t.goto(0, -70)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

t.penup()
t.goto(10, -60)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

t.penup()
t.goto(-10, -80)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

t.penup()
t.goto(17, -65)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

t.penup()
t.goto(8, -75)
t.color('white')
t.pendown()
for i in range(5):
  t.forward(7)
  t.right(144)

turtle.done()