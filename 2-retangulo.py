import turtle

tela = turtle.Screen()

retangulo = turtle.Turtle()

tela.bgcolor("medium aquamarine")


retangulo.pensize(2)    #Espessura da caneta
retangulo.fillcolor('#409EFF')
retangulo.begin_fill()

retangulo.forward(200)
retangulo.left(90)
retangulo.forward(20)
retangulo.left(90)
retangulo.forward(200)
retangulo.left(90)
retangulo.forward(20)
retangulo.left(0)

retangulo.end_fill()

#Retira caneta do papel e abaixa
retangulo.penup()
retangulo.forward(40)
retangulo.left(90)
retangulo.pendown()

retangulo.fillcolor('#3AD66B')
retangulo.begin_fill()

retangulo.forward(200)
retangulo.left(90)
retangulo.forward(20)
retangulo.left(90)
retangulo.forward(200)
retangulo.left(90)
retangulo.forward(20)
retangulo.left(0)

retangulo.end_fill()

tela.mainloop()