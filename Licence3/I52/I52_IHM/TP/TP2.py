from pickle import FALSE, NONE, TRUE
from re import I, X
import tkinter as tk
from tkinter import BOTTOM, HORIZONTAL, LEFT, RIGHT, TOP, VERTICAL, Y, Canvas, font

heigh = 600
width = 900
x = 60
y = 90
x1 = 60
y1 = 90
root = tk.Tk()

def window():
    """
    initialisation de la fenetre, taille, couleur, titre
    """
    root.title("Fenêtre graphique")
    root.config(background='grey')
    root.geometry('840x700')

#def nouveau():
    
#def ouvrir():

#def sauver():

#def quitter():

def le_menu():
    """
    creation de la barre menu dans la frame
    """
    #ajout de la barre menu
    menu_barre = tk.Menubutton(root, text="Fichier", bd=0, bg='white', relief=tk.GROOVE, fg='black', activeforeground='black')

    #creation du sous menu et ajout des option dans le menu deroulant
    filemenu = tk.Menu(menu_barre)

    filemenu.add_radiobutton(label="Nouveau")
    filemenu.add_radiobutton(label="Ouvrir")
    filemenu.add_radiobutton(label="Sauver")
    filemenu.add_radiobutton(label="Quitter", command=root.destroy)

    menu_barre["menu"] = filemenu
    menu_barre.pack(side=LEFT, anchor=tk.N)

    #ajout du bouton d'aide
    bouton_aide = tk.Button(root, text="Aide", relief=tk.GROOVE, bd=0, padx=10, pady=2, bg='white')
    bouton_aide.pack(side=RIGHT, anchor=tk.N)


def canvas():
    mat = Canvas(root, heigh=heigh, width=width, bg='white', relief=tk.SUNKEN)
    mat.pack(side=LEFT)
    mat.create_line(x, y, x1, y1, fill='black') 


if __name__ == '__main__':
    window()
    le_menu()
    canvas()

root.mainloop()