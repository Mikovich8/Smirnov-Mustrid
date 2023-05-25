import tkinter as tk
from tkinter.font import Font
from tkinter import *
from random import *

root = tk.Tk()
root.title("lippud")
root.configure(background="white")

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

def show_bahamas_flag():
    canvas.delete("all")
    canvas.create_rectangle(30, 50, 300, 150, fill="cyan")
    canvas.create_rectangle(30, 100, 300, 150, fill="yellow")
    canvas.create_rectangle(30, 200, 300, 150, fill="cyan")
    canvas.create_polygon(30, 50, 100, 125, 30, 200, fill="black")

def show_estonia_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 50, 300, 150, fill="Blue")
    canvas.create_rectangle(0, 100, 300, 150, fill="Black")
    canvas.create_rectangle(0, 200, 300, 150, fill="White")

def show_lithuanian_flag():
    canvas.delete("all")
    canvas.create_rectangle(0, 50, 300, 150, fill="Yellow")
    canvas.create_rectangle(0, 100, 300, 150, fill="Green")
    canvas.create_rectangle(0, 200, 300, 150, fill="Red")


def create_flag_button(text, command):
    button_font = Font(family="Helvetica", size=14, weight="bold")
    button = tk.Button(root, text=text, font=button_font, command=command)
    button.pack(side=LEFT, padx=5, pady=10)

def show_malevaljak():
    canvas.delete("all")
    cell_size = 50
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
    colors=["black",
        "cyan",
        "magenta",
        "red",
        "blue",
        "gray",
        "yellow",
        "green",
        "lightblue",
        "pink",
        "gold"]
    x0 = 0
    y0 = 0
    x1 = 500
    y1 = 500
    p = 2
    for i in range(55):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors))



def show_valgusfloor():
    canvas.delete("all")
    canvas.create_line(60, 50, 100, 50, width=45, fill=("Red"))
    canvas.create_line(60, 100, 100, 100, width=45, fill=("Orange"))
    canvas.create_line(60, 150, 100, 150, width=45, fill=("Green"))
    canvas.create_line(80, 180, 80, 300, width=8, fill=("Black"))
    canvas.create_line(30, 310, 140, 310, width=4, fill=("Black"))
    canvas.pack() 


def show_ruutringis():
    canvas.delete("all")
    k=7
    x0=0
    y0=0
    x1=550
    y1=550
    for i in range(k):
        x0+=50
        y0+=50
        x1-=50
        y1-=50
        canvas.create_rectangle(x0,y0,x1,y1,width=1,outline="blue", fill="Red")
        canvas.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="Yellow")
    canvas.pack(row=0, column=0)




create_flag_button("Bahama lipp", show_bahamas_flag)
create_flag_button("Eesti riigi lipp", show_estonia_flag)
create_flag_button("Leedu lipp", show_lithuanian_flag)
create_flag_button("maleväljak", show_malevaljak)
create_flag_button("mitmevärviline ovaalne", show_oval)
create_flag_button("Valgusfoor", show_valgusfloor)
create_flag_button("Ruut ringis", show_ruutringis)


root.mainloop()
