import tkinter as tk

root = tk.Tk()

def window():
    root.geometry("600x600")
    root.config(background='grey')

def button():
    bouton = tk.Button(root, text="Change", bd=0, padx=100, pady=20, command=new_page)
    bouton.pack()

def new_page():
    root.config(background='red')


if __name__ == '__main__':
    window()
    button()
   

root.mainloop()