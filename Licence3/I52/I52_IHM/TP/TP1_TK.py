from pickle import FALSE, NONE, TRUE
from re import I, X
import tkinter as tk
from tkinter import BOTTOM, HORIZONTAL, LEFT, RIGHT, TOP, VERTICAL, Y, Canvas, font
import TP1

heigh = 750
width = 750

#affichage fenetre
root = tk.Tk()
root.title("Choix de la couleur")
root.config(background='#C4C4C4')
root.geometry('840x800')

#creation de la frame
cadre = tk.Frame(root, bg='light green', bd=6, relief=tk.RIDGE)
cadre.pack(side=BOTTOM)

#creation boutton ok
bouton_ok = tk.Button(cadre, text="Ok", activeforeground='purple', relief=tk.GROOVE, padx=20, pady=10, bd=0, font=('Arial', 20), bg='plum')
bouton_ok.pack(side=LEFT)

#creation boutton annuler
bouton_annuler = tk.Button(cadre, text="Annuler", activeforeground='purple', relief=tk.GROOVE, padx=20, pady=10, bd=0, font=('Arial', 20), bg='plum')
bouton_annuler.pack(side=RIGHT)

def conversionhexa():
    color_liste = TP1.couleur("rgb.txt")
    liste_hexa = []
    for i in color_liste:
        h = "#"
        for j in i:
            j = hex(int(j))[2:]
            if len(j) == 2:
                h += j
            else:
                h += "0"
                h += j
        liste_hexa += [h]
    return liste_hexa

#creation de la matrice
def matrice():
    x = 15
    y = 0
    mat = Canvas(root, height=heigh, width=width, bg='#787878', relief=tk.SUNKEN)
    mat.pack() 
    color_liste = conversionhexa()
    for i in color_liste:
        if x > 700:
            x = 15
            y += 45
        mat.create_rectangle(x, y, x+40, y+40, fill=i)
        x += 45
print(matrice())

def scroll():
    scrollbar = tk.Scrollbar(root, width=width, orient=HORIZONTAL)
    scrollbar.place(x=800, y=0)
print(scroll())

root.mainloop()