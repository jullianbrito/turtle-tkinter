import turtle

n = int(input("Insira a quantidade de retangulos: "))

tela = turtle.Screen()

retangulo = turtle.Turtle()

tela.bgcolor("medium aquamarine")

retangulo.penup()
retangulo.setpos(-50,250)
retangulo.pendown()

for _ in range(n):
    retangulo.pensize(2)    #Espessura da caneta
    retangulo.fillcolor('#409EFF')
    retangulo.begin_fill()

    retangulo.forward(100)
    retangulo.left(90)
    retangulo.forward(10)
    retangulo.left(90)
    retangulo.forward(100)
    retangulo.left(90)
    retangulo.forward(10)
    retangulo.left(0)

    retangulo.end_fill()

    retangulo.penup()
    retangulo.forward(20)
    retangulo.left(90)
    retangulo.pendown()

tela.mainloop()