from tkinter import *
import webbrowser
from PIL import Image, ImageTk
import os
 
 
#nom de la fenetre que l'on va gerer
window = Tk()
 
#configuration de la fenetre
window.title("Projet I32")
window.geometry("1400x900")
window.minsize(1400,900)
window.maxsize(1400,900)
window.config(background='black')
img = ImageTk.PhotoImage(Image.open('image_projet.jpeg'))
pannel = Label(window, image=img)
pannel.pack(side = "bottom", fill = "both", expand = "yes")
window.iconbitmap('logo.ico')
 
#ajouter du texte (titre et sous-titre)
label_title = Label(window, text="Projet I32", font=("Arial", 50), bg='black', fg='white')
label_title.place(relx=0.4)
label_subtitles = Label(window, text="Pokémons", font=("Arial", 25), bg='black', fg='white')
label_subtitles.place(x=625, y=80)
 
#ajouter du texte (titre et sous-titre en bas de la page)
label_realise = Label(window, text="Réalisé par Ahmed, Dorian et Charlotte", font=("Arial", 18), bg='black', fg='white')
label_realise.place(relx=0.0, rely=1.0, anchor='sw')
 
label_licence = Label(window, text="L2 Informatique", font=("Arial", 15), bg='black', fg='white')
label_licence.place(relx=0.96, rely=1.0, anchor='se')
 
#frames des bouttons (cadre pour l'emplacement des bouttons)
frame = Frame(window, bg='#1E1E1E')
frame.place(x=250, y=200)
 
#configuration des bouttons
def annexe():
    webbrowser.open("https://docs.google.com/document/d/11I3NB-O2UuRd4Jd5cNhexsULNdLvznCRrRSUeDdSSNg/edit")
 
def open_boutique():
    os.startfile("boutique.py")
 
def open_inventaire():
    os.startfile("inventaire.py")
 
#Bouttons
combat_button = Button(frame, text="Combat", font=("Arial", 30), bg='#1E1E1E', fg='white', relief='sunken',
                       activeforeground='red').grid(row=0, column=0)
 
pokedex_button = Button(frame, text="Pokédex", font=("Arial", 30), bg='#1E1E1E', fg='white', relief='sunken',
                        activeforeground='red').grid(row=0, column=1)
 
boutique_button = Button(frame, text="Boutique", font=("Arial", 30), bg='#1E1E1E', fg='white', relief='sunken',
                         activeforeground='red', command=open_boutique).grid(row=0, column=2)
 
inventaire_button = Button(frame, text="Inventaire", font=("Arial", 30), bg='#1E1E1E', fg='white', relief='sunken',
                           activeforeground='red', command=open_inventaire).grid(row=0, column=3)
 
annexe_button = Button(frame, text="Annexe", font=("Arial", 30), bg='#1E1E1E', fg='white', relief='sunken',
                       activeforeground='red', command=annexe).grid(row=0, column=4)
 
#bouton de sortie
exit_button = Button(window, text="EXIT ->", activeforeground='red', command=window.destroy)
exit_button.place(x=1352, y=874)
 
#affichage a l'ecran
window.mainloop()
