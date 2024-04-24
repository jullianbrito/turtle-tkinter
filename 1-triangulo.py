import turtle

#Cria uma tela
tela = turtle.Screen()

#Cria uma tartaruga
triangulo = turtle.Turtle()

#Cor da Tela
tela.bgcolor("medium aquamarine")

#Cor do Triangulo 
triangulo.fillcolor('aqua')

triangulo.begin_fill()

for _ in range(3):
    triangulo.forward(250)  # Avança 100 unidades
    triangulo.left(120)     # Vira 120 graus à esquerda

triangulo.end_fill()

#funcao para nao fechar janela
tela.mainloop()