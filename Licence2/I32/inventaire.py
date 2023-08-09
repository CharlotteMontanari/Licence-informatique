from tkinter import *
import tkinter
import webbrowser
from PIL import Image, ImageTk
import tkinter
import webbrowser
from PIL import Image, ImageTk
import psycopg2
from sqlite3 import connect
import sqlite3
import os
 
try:
 
    #nom de la fenetre que l'on va gerer
    window = Tk()
   
    #configuration de la fenetre
    window.title("Inventaire")
    window.geometry("722x451")
    window.minsize(722,451)
    window.maxsize(722,451)
    window.config(background='yellow')
    img = ImageTk.PhotoImage(Image.open('inventaire.png'))
    pannel = Label(window, image=img)
    pannel.place(x=0, y=0)
    window.iconbitmap('logo.ico')
 
    label_title = Label(window, text="Inventaire", font=("Arial", 30), bg='#E8912D', fg='black')
    label_title.place(relx=0.6, rely=0.01)
   
    #bouton de sortie
    exit_button = Button(window, text="EXIT ->", activeforeground='red', command=window.destroy)
    exit_button.place(x=675, y=425)
   
    #mettre la view dans notre inventaire
    requete = "SELECT * FROM view_inventaire"
 
    conn = sqlite3.connect('C:/Users/Dorian/Downloads/TP/PROJET/PROJET POKEMON/Pokemon.db')
    c = conn.cursor()
    c.execute(requete)
    conn.commit()
    resultats = [('objets', 'quantité')] + c.fetchall()
    data = StringVar()
 
    total_rows = len(resultats)
    total_colums = len(resultats[0])
 
    total_rows = len(resultats)
    total_colums = len(resultats[0])
   
    class table_inventaire:
        def __init__(self, window):
            for i in range(1):
                for j in range(total_colums):
                    data.set(resultats[i][j])
                    self.e = Entry(window, width=10, fg='black', font=('Arial Black', 16), bg = '#B96200')
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, data.get())
            for i in range(1,total_rows):
                for j in range(total_colums):
                    data.set(resultats[i][j])
                    self.e = Entry(window, width=10, fg='black', font=('Arial', 19), bg ='#FFBD73')
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, data.get())
 
    table_inventaire(window)
 
    c.close()
    conn.close()
   
    #affichage a l'ecran
    window.mainloop()
 
 
except(Exception, psycopg2.Error) as error:
    print("Erreur PostgreSQL:", error)
 
opg2
from sqlite3 import connect
import sqlite3
import os
 
try:
 
    #nom de la fenetre que l'on va gerer
    window = Tk()
   
    #configuration de la fenetre
    window.title("Inventaire")
    window.geometry("722x451")
    window.minsize(722,451)
    window.maxsize(722,451)
    window.config(background='yellow')
    img = ImageTk.PhotoImage(Image.open('inventaire.png'))
    pannel = Label(window, image=img)
    pannel.place(x=0, y=0)
    window.iconbitmap('logo.ico')
 
    label_title = Label(window, text="Inventaire", font=("Arial", 30), bg='#E8912D', fg='black')
    label_title.place(relx=0.6, rely=0.01)
   
    #bouton de sortie
    exit_button = Button(window, text="EXIT ->", activeforeground='red', command=window.destroy)
    exit_button.place(x=675, y=425)
   
    #mettre la view dans notre inventaire
    requete = "SELECT * FROM view_inventaire"
 
    conn = sqlite3.connect('C:/Users/Puminblood/Downloads/Licence Info/2ème Année/I32/TP/PROJET/PROJET POKEMON/Pokemon.db')
    c = conn.cursor()
    c.execute(requete)
    conn.commit()
    resultats = [('objets', 'quantité')] + c.fetchall()
    data = StringVar()
 
    total_rows = len(resultats)
    total_colums = len(resultats[0])
 
    total_rows = len(resultats)
    total_colums = len(resultats[0])
   
 
    class table_inventaire:
        def __init__(self, window):
            for i in range(1):
                for j in range(total_colums):
                    data.set(resultats[i][j])
                    self.e = Entry(window, width=10, fg='black', font=('Arial Black', 16),bg = '#B96200')
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, data.get())
            for i in range(1,total_rows):
                for j in range(total_colums):
                    data.set(resultats[i][j])
                    self.e = Entry(window, width=10, fg='black', font=('Arial', 19), bg ='#FFBD73')
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, data.get())
 
    table_inventaire(window)
 
    c.close()
    conn.close()
   
    #affichage a l'ecran
    window.mainloop()
 
 
except(Exception, psycopg2.Error) as error:
    print("Erreur PostgreSQL:", error)
 

