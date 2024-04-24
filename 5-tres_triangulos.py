import turtle

tela = turtle.Screen()

t = turtle.Turtle()

t.penup()
t.goto(-300,300)
t.pendown()

t.fillcolor('red')

t.begin_fill()

for _ in range(3):
    t.forward(150)
    t.right(120)

t.end_fill()

t.penup()
t.forward(180)
t.right(60)
t.pendown()

t.fillcolor('green')

t.begin_fill()

for _ in range(3):
    
    t.forward(150)
    t.right(120)

t.end_fill()

t.right(-60)
t.penup()
t.forward(30)
t.pendown()

t.fillcolor('blue')

t.begin_fill()

for _ in range(3):
    t.forward(150)
    t.right(120)

t.end_fill()

tela.mainloop()