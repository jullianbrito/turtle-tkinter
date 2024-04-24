import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
canvas = tk.Canvas(window, width=800, height=600)

canvas.create_polygon([20, 40, 170, 40, 95, 160, 20, 40], # largura 150 e altura 120
outline='black', fill='red')

canvas.create_polygon([200, 40, 125, 160, 275, 160, 200, 40], # distancia 30
outline='black', fill='green')

canvas.create_polygon([230, 40, 380, 40, 305, 160, 230, 40],
outline='black', fill='blue')

canvas.pack()
window.mainloop()