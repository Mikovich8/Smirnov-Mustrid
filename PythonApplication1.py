import tkinter as tk
from tkinter.font import Font
from tkinter import *
from random import *
from functools import partial

def show_bahamas_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height() // 3, fill="cyan")
    canvas.create_rectangle(0, canvas.winfo_height() // 3, canvas.winfo_width(), canvas.winfo_height() * 2 // 3, fill="yellow")
    canvas.create_rectangle(0, canvas.winfo_height() * 2 // 3, canvas.winfo_width(), canvas.winfo_height(), fill="cyan")
    canvas.create_polygon(0, 0, canvas.winfo_width() // 3, canvas.winfo_height() // 2, 0, canvas.winfo_height(), fill="black")

def show_estonia_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height() // 3, fill="Blue")
    canvas.create_rectangle(0, canvas.winfo_height() // 3, canvas.winfo_width(), canvas.winfo_height() * 2 // 3, fill="Black")
    canvas.create_rectangle(0, canvas.winfo_height() * 2 // 3, canvas.winfo_width(), canvas.winfo_height(), fill="White")

def show_lithuanian_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height() // 3, fill="Yellow")
    canvas.create_rectangle(0, canvas.winfo_height() // 3, canvas.winfo_width(), canvas.winfo_height() * 2 // 3, fill="Green")
    canvas.create_rectangle(0, canvas.winfo_height() * 2 // 3, canvas.winfo_width(), canvas.winfo_height(), fill="Red")

def show_malevaljak():
    canvas.delete("all")
    cell_size = canvas.winfo_width() // 8
    for row in range(8):
        for col in range(8):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            if (row + col) % 2 == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")

def show_oval():
    canvas.delete("all")
    colors = ["black", "cyan", "magenta", "red", "blue", "gray", "yellow", "green", "lightblue", "pink", "gold"]
    x0 = 0
    y0 = 0
    x1 = canvas.winfo_width()
    y1 = canvas.winfo_height()
    p = 2
    for i in range(55):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors))

def show_valgusfloor():
    canvas.delete("all")
    canvas.create_line(60, 50, 100, 50, width=45, fill="Red")
    canvas.create_line(60, 100, 100, 100, width=45, fill="Orange")
    canvas.create_line(60, 150, 100, 150, width=45, fill="Green")
    canvas.create_line(80, 180, 80, canvas.winfo_height(), width=8, fill="Black")
    canvas.create_line(30, canvas.winfo_height() - 10, canvas.winfo_width() - 10, canvas.winfo_height() - 10, width=4, fill="Black")

def show_ruutringis():
    canvas.delete("all")
    k = 7
    x0 = 0
    y0 = 0
    x1 = canvas.winfo_width()
    y1 = canvas.winfo_height()
    for i in range(k):
        x0 += canvas.winfo_width() // 10
        y0 += canvas.winfo_height() // 10
        x1 -= canvas.winfo_width() // 10
        y1 -= canvas.winfo_height() // 10
        canvas.create_rectangle(x0, y0, x1, y1, width=1, outline="blue", fill="Red")
        canvas.create_oval(x0, y0, x1, y1, width=1, outline="blue", fill="Yellow")

root = tk.Tk()
root.title("lippud")
root.configure(background="white")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=BOTH, expand=True)

button_frame = tk.Frame(root, bg="white")
button_frame.pack()

create_flag_button = partial(tk.Button, button_frame, font=Font(family="Helvetica", size=14, weight="bold"))

create_flag_button(text="Bahama lipp", command=show_bahamas_flag).pack(side=LEFT, padx=5, pady=10)
create_flag_button(text="Eesti riigi lipp", command=show_estonia_flag).pack(side=LEFT, padx=5, pady=10)
create_flag_button(text="Leedu lipp", command=show_lithuanian_flag).pack(side=LEFT, padx=5, pady=10)
create_flag_button(text="Maleväljak", command=show_malevaljak).pack(side=LEFT, padx=5, pady=10)
create_flag_button(text="Mitmevärviline ovaalne", command=show_oval).pack(side=LEFT, padx=5, pady=10)
create_flag_button(text="Valgusfoor", command=show_valgusfloor).pack(side=LEFT, padx=5, pady=10)
create_flag_button(text="Ruut ringis", command=show_ruutringis).pack(side=LEFT, padx=5, pady=10)

root.mainloop()




