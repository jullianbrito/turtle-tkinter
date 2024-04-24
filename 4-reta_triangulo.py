import turtle

tela = turtle.Screen()

reta = turtle.Turtle()

w = 600

n = int(input("Insira a quantidade de triangulos: "))

reta.penup()
reta.setpos(-(w/2),0)
reta.pendown()

reta.pensize(2)

s = (w/(n+1))
l = (s/3)

reta.forward(s - (l/2))
reta.right(0)
reta.right(-45)
reta.forward(l) 

for _ in range(n-1):
    reta.right(90)
    reta.forward(l)
    reta.right(-45)
    reta.forward(s-l)
    reta.right(-45)
    reta.forward(l)

reta.right(90)
reta.forward(l)
reta.right(-45)
reta.forward(s - (l/2))


tela.mainloop()