import turtle

t=turtle.Turtle()
t.color("DarkGoldenRod")
t.begin_fill()
t.shape("turtle")

bc=turtle.Screen()
t.up()
t.goto(0,-250)
bc.bgcolor("pink")
t.down()
t.left(90)
t.forward(500)
t.right(90)
t.forward(10)
t.right(90)
t.forward(500)
t.right(90)
t.forward(10)
t.right(90)
t.forward(500)
t.right(90)
t.forward(10)
t.end_fill()


t.color("dodgerblue")
t.begin_fill()
t.forward(290)
t.right(90)
t.forward(60)
t.right(90)
t.forward(290)
t.end_fill()

t.color("red")
t.up()
t.begin_fill()
t.left(180)
t.forward(290)
t.down()
t.right(90)
t.forward(10)
t.right(90)
t.forward(290)
t.end_fill()

t.up()
t.color("white")
t.begin_fill()
t.left(180)
t.forward(290)
t.down()
t.right(90)
t.forward(60)
t.right(90)
t.forward(290)
t.end_fill()

t.color("red")
t.begin_fill()
t.up()
t.left(180)
t.forward(290)
t.down()
t.right(90)
t.forward(10)
t.right(90)
t.forward(290)
t.end_fill()

t.up()
t.color("green")
t.begin_fill()
t.left(180)
t.forward(290)
t.down()
t.right(90)
t.forward(60)
t.right(90)
t.forward(290)
t.end_fill()

t.color("black")
t.up()
t.right(90)
t.forward(200)
t.down()
t.right(90)
t.forward(290)
t.right(90)
t.forward(200)
t.right(90)
t.forward(290)
