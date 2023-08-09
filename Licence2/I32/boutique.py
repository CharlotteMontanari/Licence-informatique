from tkinter import *
import tkinter
import webbrowser
from PIL import Image, ImageTk
import psycopg2
from sqlite3 import connect
import sqlite3
import os
 
class Root:
 
    def __init__(self):
        self.window = Tk()
        #nom de la fenetre que l'on va gerer
 
        #configuration de la fenetre
        self.window.title("Boutique")
        self.window.geometry("800x600")
        self.window.minsize(800,600)
        self.window.maxsize(800,600)
        self.window.config(background='black')
        img = ImageTk.PhotoImage(Image.open('fond_boutique.png'))
        pannel = Label(self.window, image=img)
        pannel.place(x=0, y=0)
        self.window.iconbitmap('logo.ico')
 
        self.frame = Frame(self.window, bg='#1E1E1E')
        self.frame.place(x=576, y=34)
 
 
        #ajouter du titre
        label_title = Label(self.window, text="Boutique", font=("Arial", 50), bg='#EAE9E8', fg='black')
        label_title.place(relx=0.6, rely=0.4)
 
        #bouton de sortie
        exit_button = Button(self.window, text="EXIT ->", activeforeground='red', bg='#A0A0A0', command=self.window.destroy)
        exit_button.place(x=752, y=574)
 
        self.loadBoutique()
 
        pokeball = self.createButton("pokeball", 0, 0)
        potion = self.createButton("potion", 1, 0)
        super_potion = self.createButton("super_potion", 2, 0)
        hyper_potion = self.createButton("hyper_potion", 3, 0)
        potion_max = self.createButton("potion_max", 4, 0)
 
        self.window.mainloop()
 
    def loadBoutique(self):
 
        #mettre la view dans notre boutique
        requete = "SELECT * FROM boutique"
        conn = sqlite3.connect('C:/Users/Dorian/Downloads/TP/PROJET/PROJET POKEMON/Pokemon.db')
        c = conn.cursor()
        c.execute(requete)
        conn.commit()
        resultats = [('objet','type','prix','argent')] + c.fetchall()
        data = StringVar()
 
        total_rows = len(resultats)
        total_colums = len(resultats[0])
 
        c.close()
        conn.close()
 
        for i in range(1):
            for j in range(total_colums):
                data.set(resultats[i][j])
                self.e = Entry(self.window, width=10, fg='black', font=('Arial Black', 16),bg = 'grey')
                self.e.grid(row=i, column=j)
                self.e.insert(END, data.get())
        for i in range(1, total_rows):
            for j in range(total_colums):
                data.set(resultats[i][j])
                self.e = Entry(self.window, width=10, fg='black', font=('Arial', 19), bg ='#CECECE')
                self.e.grid(row=i, column=j)
                self.e.insert(END, data.get())
 
    def achat_item(self, itemName):
        connexion = sqlite3.connect('C:/Users/Dorian/Downloads/TP/PROJET/PROJET POKEMON/Pokemon.db')
        com = connexion.cursor()
        requete_buy = f"update inventaire set quantite = quantite + 1 where nom_objet = '{itemName}';"
        com.execute(requete_buy)
        connexion.commit()
        com.close()
        connexion.close()
        self.loadBoutique()
 
    def createButton(self, itemName, rowNumber, columnNumber):
        button = Button(self.frame, text="Buy", font=('Arial', 12), bg ='#CECECE', fg='black', relief='raised', activeforeground='red', command=lambda: self.achat_item("pokeball")).grid(row=rowNumber, column=columnNumber)

if __name__=="__main__":
    Root()