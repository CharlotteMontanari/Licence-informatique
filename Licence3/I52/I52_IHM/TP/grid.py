import tkinter as tk

root = tk.Tk()
height = 700
width = 900


x = 6
y = 6
mat = tk.Canvas(root, height=height, width=width, bg="#ABABAB")
mat.pack()
for _ in range(600):
    if x > 600:
        x = 6
        y += 20
    mat.create_rectangle(x, y, x+20, y+20)
    x += 20


root.mainloop()
