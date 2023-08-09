import tkinter as tk
from re import X

root = tk.Tk()
x = 0
y = 0
etat = 0
liste_de_points = []


def my_window() -> None:
    root.geometry("700x700")
    root.configure(bg="white")
    root.bind("<ButtonPress>", deplacer_fenetre)
    root.bind("<Motion>", move)
    root.bind("<ButtonRelease>", stop)


def my_events() -> None:
    root.mainloop()


canvas = tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()
rectangle = canvas.create_rectangle(
    200, 200, 600, 600, fill="white", outline="black", width=4
)


def deplacer_fenetre(event) -> None:
    """permet de deplacer le rectangle"""
    global x, y, etat
    etat = 1
    x = event.x
    y = event.y


def move(event) -> None:
    global x, y, etat
    if etat:
        canvas.move(rectangle, event.x - x, event.y - y)
        for i in liste_de_points:
            canvas.move(i, event.x - x, event.y - y)
        x = event.x
        y = event.y


def stop(event) -> None:
    global etat
    etat = 0


def matrice(xw1, yw1, xw2, yw2, xv1, yv1, xv2, yv2, He, x, y):
    """
    matrice = [[dxv / dxw,    0,               xv1 - ((dxv * xw1) / dxw)],
               [0,           -dyv / dyw,       He - yv1 + ((yw1*dyv) / dyw)],
               [0,           0,                1]]
    """
    dxv = xv2 - xv1
    dyv = yv2 - yv1
    dxw = xw2 - xw1
    dyw = yw2 - yw1

    return (
        ((dxv / dxw) * x) + (xv1 - (dxv * xw1) / dxw),
        (-dyv / dyw) * y + (He - yv1 + (yw1 * dyv) / dyw),
        1,
    )


print(matrice(2.0, 2.0, 6.0, 6.0, 200, 100, 600, 500, 700, 4.0, 4.0))

pos = matrice(2.0, 2.0, 6.0, 6.0, 200, 100, 600, 500, 700, 4.0, 4.0)


def tous_les_points() -> None:
    global liste_de_points
    with open("texte.txt", "r") as f:
        lignes = f.readlines()
        liste_de_points += lignes
tous_les_points()

print(liste_de_points)

# pts = canvas.create_oval(pos[0] - 5, pos[1] - 5, pos[0] + 5, pos[1] + 5, fill="orange")

if __name__ == "__main__":
    my_window()
    my_events()
