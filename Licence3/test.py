import tkinter as tk
import math

# Définit la taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Définit les dimensions du terrain et les positions des obstacles
TERRAIN_WIDTH = 800
TERRAIN_HEIGHT = 600
OBSTACLES = [
    (150, 150, 50, 200),
    (400, 100, 50, 200),
    (600, 400, 200, 50),
    (100, 400, 200, 50),
]

# Crée la fenêtre Tkinter
root = tk.Tk()
root.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))

# Crée le canvas Tkinter
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# Crée le point bleu
point_position = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
point_circle = canvas.create_oval(point_position[0]-10, point_position[1]-10, point_position[0]+10, point_position[1]+10, fill="blue")

# Fonction appelée lors d'un déplacement de la souris
def on_mouse_move(event):
    global point_position
    # Met à jour la position du point en fonction de la souris
    point_position = [event.x, event.y]
    canvas.coords(point_circle, point_position[0]-10, point_position[1]-10, point_position[0]+10, point_position[1]+10)
    update_cone_of_vision()

# Dessine les obstacles sur le canvas Tkinter
def draw_obstacles():
    for obstacle in OBSTACLES:
        canvas.create_rectangle(obstacle[0], obstacle[1], obstacle[0]+obstacle[2], obstacle[1]+obstacle[3], fill="black")

# Fonction pour calculer les coordonnées des intersections entre le cône de vision et les obstacles
def get_intersections():
    intersections = []
    for obstacle in OBSTACLES:
        rect_center = [obstacle[0]+obstacle[2]/2, obstacle[1]+obstacle[3]/2]
        rect_to_point_vector = [point_position[0] - rect_center[0], point_position[1] - rect_center[1]]

        # Calcule la distance entre le point et le rectangle projeté sur l'axe X
        x_proj = abs(rect_to_point_vector[0])
        y_proj = abs(rect_to_point_vector[1])
        half_width = obstacle[2] / 2
        half_height = obstacle[3] / 2

        if x_proj <= half_width and y_proj <= half_height:
            # Le point est à l'intérieur du rectangle
            intersections.append((point_position[0], point_position[1]))
        else:
            # Calcule l'intersection entre le cône de vision et le bord du rectangle
            x_intersect = rect_center[0]
            y_intersect = rect_center[1]
            if x_proj <= half_width:
                y_intersect = rect_center[1] + (half_height * math.copysign(1, rect_to_point_vector[1])) * x_proj / half_width
            elif y_proj <= half_height:
                x_intersect = rect_center[0] + (half_width * math.copysign(1, rect_to_point_vector[0])) * y_proj / half_height
                
            if x_intersect >= 0 and x_intersect <= WINDOW_WIDTH and y_intersect >= 0 and y_intersect <= WINDOW_HEIGHT:
                intersections.append((x_intersect, y_intersect))

    return intersections

# Dessine le cône de vision sur le canvas Tkinter
def draw_cone_of_vision(intersections):
    canvas.delete("cone")
    canvas.create_polygon(point_position[0], point_position[1], *sum(intersections, ()), fill="gray", stipple="gray12", tag="cone")

# Met à jour le cône de vision en fonction de la position du point et des obstacles
def update_cone_of_vision():
    intersections = get_intersections()
    draw_cone_of_vision(intersections)

# Dessine les obstacles sur le canvas Tkinter
draw_obstacles()

# Associe la fonction on_mouse_move à l'événement "B1-Motion" (déplacement de la souris en maintenant le bouton gauche enfoncé)
canvas.bind("<B1-Motion>", on_mouse_move)

# Met à jour le cône de vision au démarrage du programme
update_cone_of_vision()

# Lance la boucle principale Tkinter
root.mainloop()
