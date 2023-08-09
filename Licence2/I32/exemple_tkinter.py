from tkinter import *
import tkinter as tk
import webbrowser

def ouvre_lien():
    webbrowser.open_new("https://docs.google.com/spreadsheets/d/1yDZSaYvA0GlG143RYmQhAC89gHlO9LDMlOs47ev2DyI/edit#gid=0")

#convertir une image
#https://image.online-convert.com/fr/convertir-en-ico

#cree une fenetre
window = Tk()

#personalisee cette fenetre
window.title("Our projet")
window.geometry("500x500")
#changer le logo
#window.iconbitmap("nom de l'image")

#creation d'une boite frame
frame = Frame(window)

window.config(background='red')
#ajouter du texte
label_title = Label(window, text="Hello les dresseurs", font=("Arial", 80), bg='white')
label_title.pack(expand=YES)

#ajouter un boutton
button = Button(frame, text="Accès vers les tables", command=ouvre_lien)
button.pack()

#afficher cette fenetre
window.mainloop()