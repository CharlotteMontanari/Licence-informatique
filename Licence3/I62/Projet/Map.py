import tkinter as tk

import Meat
import Nest
import Obstacle
import Seed
import Water

SIZE = 1  # taille des cases
SIZE_ANT = 1  # taille du rayon representant la fourmi
SIZE_OBSTACLE = 40  # taille des murs selon une coordonnées
COLOR_OBSTACLE = "Black"

class Map:
    def __init__(self):
        self.matrix = []
        self.line = 0
        self.column = 0
        self.list_obstacle = []
        self.list_meat = []
        self.list_water = []
        self.list_seed = []
        self.list_nest = []

    # MATRIX
    def init_matrix(self, canvas):
        """
        create the obstacle of the map
        """
        SIZE = 40
        list_obstacles = [
            (10 + SIZE, 10, 10, 10 + SIZE),
            (20, 10 + SIZE, 10 + SIZE, 20),
        ]
        for i in list_obstacles:
            canvas.create_rectangle(i[0], i[1], i[2], i[3], fill="black")

    def print_matrix(self, name=""):
        """
        Print the matrix with a personal form with a name(default empty)
        """
        print("\nMatrice", name, ":")
        temp = ""
        for _ in range(self.column + 2):  # afficher la bordure du haut
            temp = temp + "*"
        print(temp)

        for LINE in self.matrix:
            temp = ""
            for COLUMN in LINE:
                temp = temp + str(COLUMN)  # + ", "
            print(temp + "*")
        temp = ""
        for _ in range(self.column + 2):  # afficher la bordure du bas
            temp = temp + "*"
        print(temp)
    
    def get_list_nest(self):
        """
        return the list nest
        """
        return self.list_nest

    def verification_location(self, x: int, y: int) -> bool:
        """
        check if the location is empty
        """
        if self.matrix[y][x] == "_":
            return True
        else:
            print("Erreur verification emplacement (",x,", ",y,") : l'emplacement n'est pas libre.",)
            return False

    # Obstacle
    def add_obstacle(self, x: int, y: int) -> None:
        """
        add an obstacle
        """
        if self.verification_location(x, y):
            self.matrix[y][x] = "#"
            self.list_obstacle += [Obstacle.Obstacle(x, y)]

    # MEAT
    def add_meat(self, x: int, y: int):
        """
        add meat resource
        """
        if self.verification_location(x, y):
            self.matrix[y][x] = "m"
            self.list_meat += Meat.Meat(x, y)

    # WATER
    def add_water(self, x: int, y: int):
        """
        add water resource
        """
        if self.verification_location(x, y):
            self.matrix[y][x] = "w"
            self.list_water += Water.Water(x, y)

    # SEED
    def add_seed(self, x: int, y: int):
        """
        add seed resource
        """
        if self.verification_location(x, y):
            self.matrix[y][x] = "s"
            self.list_seed += Seed.Seed(x, y)

    def add_on_matrix(self, x: int, y: int, value: str):
        """
        add an element in the matrix
        """
        if self.verification_location(x, y):
            self.matrix[y][x] = value

    # FILE
    def write_matrix(self, filename):
        """
        write the representation of the matrix in a file (don't need to prefix the extension ".mde")
        """
        text = filename + ".mde"
        file = open(text, "w")
        copy = ""
        for line in self.matrix:
            temp = ""
            for column in line:
                temp = temp + str(column)  # + ", "
            copy = copy + temp + "\n"
        file.write(copy)
        file.close

    def choose_the_map(self, canvas, file_map):
        """
        read a file.mde which contain the coordinate of the obstacle
        return true if the file is correct
        """
        if not file_map.endswith(".mde"):
            print("Erreur lecture_fichier() : Extension de fichier incorrecte (.mde)")
            return False
        else:
            file = open(file_map, "r")
            copy = file.readlines()
            file.close()

            # Enlever les "\n" a la fin des readlines
            lines = []
            for line in copy:
                lines = lines + [line[:-1]]

            # Parcours pour créer les obstacles
            value = ""
            for line in lines:
                value = line.split()
                canvas.create_rectangle(
                    int(value[0]),
                    int(value[1]),
                    int(value[0]) + SIZE_OBSTACLE,
                    int(value[1]) + SIZE_OBSTACLE,
                    fill=COLOR_OBSTACLE,
                )
            return True

    # Tkinter
    def show_the_map(self, canvas):
        """
        print the map at the locate x,y of the frame
        """
        for y, row in enumerate(self.matrix):
            for x, _ in enumerate(row):
                x1 = x 
                y1 = y 
                x2 = x1
                y2 = y1
                if self.matrix[y][x] == "#":
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill="black", outline="black"
                    )
                    self.list_obstacle = self.list_obstacle + [
                        Obstacle.Obstacle(x1, y1)
                    ]
                if self.matrix[y][x] == "f1":
                    canvas.create_oval(
                        x1 - SIZE_ANT,
                        y1 - SIZE_ANT,
                        x + SIZE_ANT,
                        y + SIZE_ANT,
                        fill="blue",
                        outline="black",
                    )