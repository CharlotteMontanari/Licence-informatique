import tkinter as tk

root = tk.Tk()


def my_window() -> None:
    root.geometry("700x700")
    root.configure(bg="white")


def my_events() -> None:
    root.mainloop()


canvas = tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()

a1 = 50
a2 = 50
width = 550
heigh = 550
rectangle = canvas.create_rectangle(a1, a2, a1 + width, a2 + heigh, fill="lightgrey")


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


# xv1: coord en x du pt en bas à gauche de la fenetre -> a1
# yv1: pareil mais en y -> taille fenetre - a2 - heigh

# xv2: coord en x du pt en haut à droite de la fenetre -> a1 + width
# yv2: pareil mais en y -> taille fenetre - a2
pos1 = matrice(
    0.0, 0.0, 10.0, 10.0, a1, 700 - a2 - heigh, a1 + width, 700 - a2, 700, 3.0, 2.0
)
pos2 = matrice(
    0.0, 0.0, 10.0, 10.0, a1, 700 - a2 - heigh, a1 + width, 700 - a2, 700, 6.0, 6.0
)

pts1 = canvas.create_oval(
    pos1[0] - 5, pos1[1] - 5, pos1[0] + 5, pos1[1] + 5, fill="orange"
)
pts2 = canvas.create_oval(
    pos2[0] - 5, pos2[1] - 5, pos2[0] + 5, pos2[1] + 5, fill="orange"
)


def allumer_pixel(x, y):
    canvas.create_line(x, y, x + 1, y, fill="orange", width=5)


# Algo de Bresenham dans le premier octant
# def bresenham(p1, p2):
#     dx = abs(p2[0] - p1[0])
#     dy = abs(p2[1] - p1[1])
#     dec = dx - 2 * dy
#     x = p1[0]
#     y = p1[1]
#     while x <= dx + p1[0]:
#         allumer_pixel(x, y)
#         if dec < 0:
#             dec += 2 * dx
#             y -= 1
#         dec += 2 * dy
#         x += 1

# Algo de Bresenham dans le deuxième octant
def bresenham(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dec = dy - 2 * dx
    x = p1[0]
    y = p1[1]
    while y >= p2[1]:
        allumer_pixel(x, y)
        if dec > 0:
            dec -= 2 * dy
            x += 1
        dec -= 2 * dx
        y -= 1


# Algo de Bresenham généralisé
# def bresenham(px1, px2, py1, py2):
#     # calcul de la différence entre les coordonnées x et y
#     dx = abs(px2 - px1)
#     dy = abs(py2 - py1)

#     # détermine le signe de la distance à parcourir dans chaque direction en fonction de la position des deux points
#     # Si px2 est plus grand que px1, la distance en x sera positive, sinon elle sera négative. Pareil pour y
#     sx = 1 if px1 < px2 else -1
#     sy = 1 if py1 < py2 else -1

#     # initialisation de la variable d'erreur à la différence entre la distance en x et la distance en y.
#     err = dx - dy

#     # tant qu'on est pas arrive aux points de fin
#     while px1 != px2 or py1 != py2:
#         allumer_pixel(px1, py1)
#         e2 = err * 2
#         if e2 > -dy:
#             err -= dy
#             px1 += sx
#         if e2 < dx:
#             err += dx
#             py1 += sy
# Ces lignes mettent à jour la variable d'erreur en fonction de la distance parcourue en x et en y
# depuis le pixel courant. Si la distance parcourue en x est plus grande que l'erreur multipliée par 2,
# cela signifie que le pixel suivant doit être dessiné en direction de l'axe horizontal, donc l'erreur est mise à
# jour en soustrayant la distance en y. Sinon, le pixel suivant doit être dessiné en direction de l'axe vertical,
# donc l'erreur est mise à jour en ajoutant la distance en x. Dans les deux cas, la position courante est mise à jour
# en fonction de la direction de la ligne (déterminée par sx et sy).

bresenham(pos1, pos2)


if __name__ == "__main__":
    my_window()
    my_events()
