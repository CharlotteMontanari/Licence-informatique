import tkinter as tk
from OpenGL import GL
# from pyopengltk import OpenGLFrame
import carte as c
from carte import Map, Point, State

root = tk.Tk()
height = 700  # hauteur
width = 1200  # largeur

frame = tk.Frame(root, bg="white")  # game
frame.pack(expand=True, fill=tk.BOTH)

frame2 = tk.Frame(frame, bg="red")  # red line to separate my screen
frame2.pack(expand=True, fill=tk.Y)
p = Point()
t = Map(p, frame)


def my_window() -> None:
	"""
	parametrage de la fenetre
	"""
	root.geometry(f"{width}x{height}")
	root.configure(bg="white")
	root.title("Raycasting")
	root.bind("<KeyPress-z>", t.Avancer)
	root.bind("<KeyPress-s>", t.Reculer)
	root.bind("<KeyPress-q>", t.Gauche)
	root.bind("<KeyPress-d>", t.Droite)
	root.bind("<Right>", t.TournerDroite)
	root.bind("<Left>", t.TournerGauche)
    

def start() -> None:
	t.load_map("field")
	t.define_camera_position()
	t.print_map()
	t.add_object(p)
	x, y = p.get_position()
start()


def my_events() -> None:
    root.mainloop()


if __name__ == "__main__":
    my_window()
    my_events()
