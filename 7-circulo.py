import tkinter as tk

def circulo(x, y, raio, cor):
    x1 = x
    y1 = y
    x2 = x + raio
    y2 = y + raio

    canvas.create_oval(x1, y1, x2, y2, outline = cor, width=10)

window = tk.Tk()
window.geometry("800x600")
window.title("Circulos")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

circulo(10, 20, 200, "#0885c2")
circulo(240, 20, 200, "#000000")
circulo(470, 20, 200, "#dc143c")
circulo(125, 120, 200, "#daa520")
circulo(355, 120, 200, "#228b22")


window.mainloop()