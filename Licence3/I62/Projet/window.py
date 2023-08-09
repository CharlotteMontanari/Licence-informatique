import random
import time
import tkinter as tk
from threading import Thread
from tkinter import messagebox, ttk

import Ant_Queen as a_q
import Ant_Scout as a_s
import Ant_Worker as a_w
import Map as m
import Meat
import Nest as n
import Resource as r
import Seed
import Water

###############################
# VARIABLES GLOBALE
root = tk.Tk()
height = 1400  # hauteur
width = 900  # largeur

language = ""

game_pause = True

the_map = m.Map()

species = ""
verification_species = False

number_of_worker = 0
number_of_queen = 0
number_of_scout = 0

validate = [0, 0, 0, 0]

###############################
# CANVAS GAME CONFIGURATION

xx = width + 250
yy = height - 700
cnv = tk.Canvas(root, bg="ivory", width=xx, height=yy)  # canvas for the game
cnv.grid(row=5, column=0)
the_map.choose_the_map(cnv, "test.mde")

# speed1 variable by default
var = tk.IntVar(value=1)


###############################
# FONCTIONS


def my_window() -> None:
    """
    creation of the window
    """
    root.geometry(f"{height}x{width}")
    root.configure(bg="white")
    root.title("Four-me")


def exit_game() -> None:
    """
    configuration of the exit button
    """
    button = tk.Button(
        root,
        text="EXIT",
        font=("Arial", 18),
        padx=30,
        pady=5,
        command=lambda: sure_to_exit(),
    )
    button.grid(row=6, sticky=tk.E)


exit_game()


def help_button() -> None:
    """
    creation of the help button
    """
    messagebox.showinfo(
        title="HELP",
        message="Saississez toutes les valeurs des fourmis pour poser un nid !",
    )


def language_define(event) -> None:
    """
    return the language define by the user
    """
    global language
    language = menu.get()


def nest_define(event) -> str:
    """
    return the species choosen by the user
    """
    global species, validate
    species = Nb_species.get()
    validate[3] = 1
    confirmation_nest()
    cnv.update()
    return species


###############################
# FONCTION QUI VALIDE NOS VALEURS


def validate_worker() -> int:
    global Nb_worker, validate
    w = Nb_worker.get()
    validate[0] = 1
    confirmation_nest()
    return int(w)


def validate_queen() -> int:
    global Nb_queen, validate
    q = Nb_queen.get()
    validate[1] = 1
    confirmation_nest()
    return int(q)


def validate_scout() -> int:
    global Nb_scout, validate
    s = Nb_scout.get()
    validate[2] = 1
    confirmation_nest()
    return int(s)


def pause() -> None:
    """
    put the game in pause
    """
    global game_pause, species
    game_pause = not game_pause
    if (
        species != ""
        and validate_worker() != ""
        and validate_queen() != ""
        and validate_scout() != ""
        and the_map.list_nest != []
    ):
        start()
        cnv.update()


def confirmation_nest() -> None:
    global validate
    somme = 0
    for i in validate:
        if i == 1:
            somme += 1
    if somme == 4:
        ttext = tk.Label(frame1, text="Poser un nid !", font=("Arial", 20), bg="Grey")
        ttext.grid(row=4, column=1)
        cnv.update()


###############################
# EXIT CONFIGURATION
def sure_to_exit() -> None:
    """
    ask to the user if he wants to leave the app
    """
    global index_traduction
    anwser = messagebox.askyesno(
        title=None, message="Êtes-vous sûr de vouloir quitter ?"
    )
    if anwser:
        root.destroy()


def draw_nest(event) -> None:
    """
    draw the nest when you put it on the screen
    """
    global xx, yy, the_map, number_of_queen, number_of_scout, number_of_worker, species
    x, y = event.x, event.y
    size = 20
    if size < x <= xx - size and size < y <= yy - size:
        if (
            species != "" 
            and validate_worker() != ""
            and validate_scout() != ""
            and validate_queen() != ""
        ):
            cnv.create_rectangle(x - size, y - size, x + size, y + size, fill=species)
            number_of_worker = validate_worker()
            number_of_queen = validate_queen()
            number_of_scout = validate_scout()
            nid = n.Nest(
                x, y, species, number_of_worker, number_of_scout, number_of_queen
            )
            nid.create_worker(cnv, species)
            nid.create_queen(cnv, species)
            nid.create_scout(cnv, species)
            print(nid.list_Worker, nid.list_Queen, nid.list_Scout)
            the_map.list_nest += [nid]


cnv.bind("<Button-1>", draw_nest)


def draw_resources() -> None:
    """
    draw the resource on our map
    """
    size = 100
    Meat.Meat(470, 580, 20, 5000)
    cnv.create_oval(470, 580 + size, 470 + size, 580, fill="#834800")

    Seed.Seed(600, 160, 20, 5000)
    cnv.create_oval(600, 160 + size, 600 + size, 160, fill="#FFBE6F")

    Water.Water(100, 100, 20, 5000)
    cnv.create_oval(100, 100 + size, 100 + size, 100, fill="#2BE5FF")


draw_resources()


def destroy_nest(event) -> None:
    """
    destroy the nest when you click on it and delete it from out list of nest
    """
    x = event.x
    y = event.y
    ident = cnv.find_closest(x, y)[0]
    a = the_map.get_list_nest()
    if ident:
        cnv.delete(ident)
        a.pop(ident - 1)


cnv.bind("<Button-2>", destroy_nest)


def speed_value() -> int:
    global var
    value = var.get()
    return value


speed_value()


def move(ant):
    """
    make the movement of the ant on the map
    """
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    ant.set_xy(ant.x + x, ant.y + y)
    cnv.move(ant.id_tkinter, x, y)


def start():
    """
    start the game when the button is played
    """
    global game_pause, value
    while not game_pause:
        if speed_value() == 1:
            time.sleep(0.5)
        elif speed_value() == 2:
            time.sleep(0.01)
        elif speed_value() == 3:
            time.sleep(0.0001)
        for nest in the_map.list_nest:
            for a_q in nest.list_Queen:
                t = Thread(target=move, args=(a_q,))
                t.start()
            for a_w in nest.list_Worker:
                t = Thread(target=move, args=(a_w,))
                t.start()
            for a_s in nest.list_Scout:
                t = Thread(target=move, args=(a_s,))
                t.start()
            cnv.update()


###############################
# ZONE CONFIGURATION

frame1 = tk.Frame(root, bg="Grey")
frame1.grid(row=0, column=0)

###############################
# HELP BUTON
image_help = tk.PhotoImage(file="help.png")
button_help = tk.Button(frame1, image=image_help, command=lambda: help_button())
button_help.grid(row=0, column=6, sticky=tk.E)

###############################
# LANGUAGE CONFIGURATION

labelChoix = tk.Label(frame1, text="Choisir la langue", font=("Arial", 20), bg="Grey")
labelChoix.grid(row=0, column=0, padx=30)
lang = ["Français", "English"]
menu = ttk.Combobox(frame1, values=lang)
menu.grid(row=1, column=0, padx=30)
menu.current(0)
menu.bind("<<ComboboxSelected>>", language_define)

style = ttk.Style()
style.theme_use("clam")

###############################
# NEST CONFIGURATION

label_nest = tk.Label(frame1, text="Espèces", font=("Arial", 20), bg="Grey")
label_nest.grid(row=0, column=1, padx=30)
species_list = ["red", "blue", "yellow", "pink", "orange", "green", "purple", "brown"]

Nb_species = ttk.Combobox(frame1, values=species_list)
Nb_species.grid(row=1, column=1, padx=30)
Nb_species.bind("<<ComboboxSelected>>", nest_define)

###############################
# WORKER CONFIGURATION

label_worker = tk.Label(
    frame1, text="Nb fourmi travailleuse", font=("Arial", 20), bg="Grey"
)
label_worker.grid(row=0, column=2, padx=30)
Nb_worker = tk.Entry(frame1, bg="white", foreground="black", width=8)
Nb_worker.grid(row=1, column=2, padx=30)
button_ok = tk.Button(frame1, text="OK", font=("Arial", 16), command=validate_worker)
button_ok.grid(row=2, column=2, padx=30)

###############################
# QUEEN CONFIGURATION

label_queen = tk.Label(frame1, text="Nb fourmi reine", font=("Arial", 20), bg="Grey")
label_queen.grid(row=0, column=3, padx=30)
Nb_queen = tk.Entry(frame1, bg="white", foreground="black", width=8)
Nb_queen.grid(row=1, column=3, padx=30)
button_ok = tk.Button(frame1, text="OK", font=("Arial", 16), command=validate_queen)
button_ok.grid(row=2, column=3, padx=30)

###############################
# SCOUT CONFIGURATION

label_scout = tk.Label(
    frame1, text="Nb fourmi éclaireuse", font=("Arial", 20), bg="Grey"
)
label_scout.grid(row=0, column=4, padx=30)
Nb_scout = tk.Entry(frame1, bg="white", foreground="black", width=8)
Nb_scout.grid(row=1, column=4, padx=30)
button_ok = tk.Button(frame1, text="OK", font=("Arial", 16), command=validate_scout)
button_ok.grid(row=2, column=4, padx=30)

###############################
# SPEED CONFIGURATION

label_speed1 = tk.Label(frame1, text="Vitesse", font=("Arial", 20), bg="Grey")
label_speed1.grid(row=0, column=5, padx=30)

speed1 = tk.Radiobutton(
    frame1, text="Lent", bg="Grey", font=("Arial", 16), variable=var, value=1
)
speed1.grid(row=1, column=5, padx=30, sticky=tk.W)

speed2 = tk.Radiobutton(
    frame1, text="Moyen", bg="Grey", font=("Arial", 16), variable=var, value=2
)
speed2.grid(row=2, column=5, padx=30, sticky=tk.W)

speed3 = tk.Radiobutton(
    frame1, text="Rapide", bg="Grey", font=("Arial", 16), variable=var, value=3
)
speed3.grid(row=3, column=5, padx=30, sticky=tk.W)

###############################
# PAUSE / PLAY BUTON
image_pause = tk.PhotoImage(file="pause_play.png")
button_pause = tk.Button(frame1, image=image_pause, command=lambda: pause())
button_pause.grid(row=4, column=0, sticky=tk.W)


def my_events() -> None:
    root.mainloop()


if __name__ == "__main__":
    my_window()
    my_events()
