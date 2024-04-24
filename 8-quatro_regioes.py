import tkinter as tk

n = 400

def linha(tam):
    canvas.create_line(n-tam, n, n+tam, n)
    canvas.create_line(n, n+tam, n, n-tam)

def triangulo(tam, j):
    canvas.create_polygon([n+j, n-j, n+j+(tam/2), n-tam, n+tam, n-j, n+j, n-j],
    outline='#3cb371', width=2, fill='#00fa9a')

def circulo(tam, y):  
   canvas.create_oval(n-tam, n+y, n-y, n+tam, outline = "#cd5c5c", width=2, fill="#f08080")

def quadrado(tam, j):
    canvas.create_rectangle(n+j, n+tam, n+tam, n+j, outline='#4169e1', width=2 ,fill='#1e90ff')    

window = tk.Tk()
window.geometry("800x800")
window.title("4 Regiões")
canvas = tk.Canvas(window, width=800, height=800)
canvas.pack()

t = int(input("Digite o valor de T: "))
i = t * 0.09    #area do triangulo e quadrado
k = t * 0.045   #area do circulo

linha(t)
triangulo(t,i)
circulo(t,k)
quadrado(t,i)

window.mainloop()