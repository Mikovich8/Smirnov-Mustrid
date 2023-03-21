from tkinter import *

# Funktsioon, mis kuvab Bahama lippu
def show_bahamas_lipp():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 200, 133, fill="#00A5E3")
    canvas.create_polygon(0, 0, 200, 0, 200, 44.3, 0, 44.3, fill="#FCD116")
    canvas.create_polygon(0, 88.7, 200, 88.7, 200, 133, 0, 133, fill="#CE1126")

# Funktsioon, mis kuvab Eesti lippu
def show_eesti_lipp():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 200, 133, fill="#0072C6")
    canvas.create_rectangle(0, 0, 66.6, 133, fill="#000000")
    canvas.create_rectangle(66.6, 0, 133.3, 133, fill="#FFFFFF")
    canvas.create_rectangle(133.3, 0, 200, 133, fill="#D50F25")

# Funktsioon, mis kuvab Itaalia lippu
def show_itaalia_lipp():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 200, 133, fill="#009246")
    canvas.create_rectangle(0, 0, 66.6, 133, fill="#FFFFFF")
    canvas.create_rectangle(66.6, 0, 133.3, 133, fill="#F1BF00")
    canvas.create_rectangle(133.3, 0, 200, 133, fill="#CE2B37")

# loo tkinter akna
root = Tk()
root.title("Lipud")

# loo tkinter canvas (ristkülik)
canvas = Canvas(root, width=200, height=133, bg="white")
canvas.pack()

# loo tkinter nupud
Button(root, text="Bahama saarte lipp", command=show_bahamas_lipp).pack()
Button(root, text="Eesti riigi lipp", command=show_eesti_lipp).pack()
Button(root, text="Itaalia riigi lipp", command=show_itaalia_lipp).pack()

# käivita tkinter akna sündmuste tsükkel
root.mainloop()


def draw(canvas, x, y, width, height, num_squares, num_circles):
    if num_squares == 0 and num_circles == 0:
        return
    elif num_squares > 0:
        canvas.create_rectangle(x, y, x+width, y+height)        
        draw(canvas, x+width, y, width, height, num_squares-1, num_circles)
    elif num_circles > 0:
        canvas.create_oval(x, y, x+width, y+height)
        draw(canvas, x+width, y, width, height, num_squares, num_circles-1)

def on_submit():
    num_squares = int(square_entry.get())
    num_circles = int(circle_entry.get())
    draw(canvas, 0, 0, 50, 50, num_squares, num_circles)

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

square_label = Label(root, text="Squares:")
square_label.pack(side=LEFT)
square_entry = Entry(root)
square_entry.pack(side=LEFT)

circle_label = Label(root, text="Circles:")
circle_label.pack(side=LEFT)
circle_entry = Entry(root)
circle_entry.pack(side=LEFT)

submit_button = Button(root, text="Draw", command=on_submit)
submit_button.pack(side=LEFT)

root.mainloop()
