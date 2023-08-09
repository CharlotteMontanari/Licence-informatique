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

def bezier(m0, m1, m2, m3, pas) -> list:
    """
    les points m sont des coordonnes, et pas est un float
    """
    # initialisation de la liste pour les points
    liste = [m0, m1, m2, m3]
    nbr_pts = 4
    # formule de sommation
    formule = nbr_pts * (nbr_pts - 1) // 2
    liste += [(0, 0)] * formule
    i = 0
    general = nbr_pts
    pt_courbe = []
    inc = pas
    pas = 0
    while pas <= 1:
        nbr_pts = 4
        i = 0
        while nbr_pts != 1:
            i0 = i
            while i < i0 + nbr_pts - 1:
                x = (1 - pas) * liste[i][0] + pas * liste[i+1][0]
                y = (1 - pas) * liste[i][1] + pas * liste[i+1][1]
                liste[i+general] = (x, y)
                i += 1
            nbr_pts -= 1
        pt_courbe += [liste[-1]]
        pas += inc
    print(pt_courbe)
    return liste

M0 = (0, 0)
M1 = (0, 1)
M2 = (1, 1)
M3 = (1, 0)
bezier(M0, M1, M2, M3, 0.25)

# if __name__ == "__main__":
#     my_window()
#     my_events()
