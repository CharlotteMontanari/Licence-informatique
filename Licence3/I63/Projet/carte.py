import random
import tkinter as tk
from enum import Enum, auto
from math import cos, pi, radians, sin, sqrt, tan
from re import X

from calcul import bresenham


class State(Enum):
    WALL = auto()
    EMPTY = auto()
    POINT = auto()


enum = {"_": State.EMPTY, "#": State.WALL, ".": State.POINT}

reverse_enum = {State.EMPTY: "_", State.WALL: "#", State.POINT: "."}


class Point:
    def __init__(self) -> None:
        self.type = State.POINT
        self.x = 0
        self.y = 0
        self.angle = 240
        self.distance_vue = 64

    def get_position(self) -> tuple:
        return (self.x, self.y)

    def set_position(self, x, y) -> None:
        self.x = x
        self.y = y

    def set_angle(self, angle):
        self.angle = angle

    def get_angle(self):
        return self.angle

    def isPoint(self):
        return True

    def Avancer(self, test, vitesse):
        """
        if test == 1:
                self.x -= round(sin(self.angle * pi / 180) * vitesse, 3)
        elif test == 2:
                self.y += round(cos(self.angle * pi / 180) * vitesse, 3)
        elif test == 0:
                self.y += round(cos(self.angle * pi / 180) * vitesse, 3)
                self.x -= round(sin(self.angle * pi / 180) * vitesse, 3)
        """
        if not test:
            self.y += round(cos(self.angle * pi / 180) * vitesse, 3)
            self.x -= round(sin(self.angle * pi / 180) * vitesse, 3)

    def Reculer(self, test, vitesse):
        """
        if test == 1:
                self.x += round(sin(self.angle * pi / 180) * vitesse, 3)
        elif test == 2:
                self.y -= round(cos(self.angle * pi / 180) * vitesse, 3)
        elif test == 0:
                self.y -= round(cos(self.angle * pi / 180) * vitesse, 3)
                self.x += round(sin(self.angle * pi / 180) * vitesse, 3)
        """
        if not test:
            self.y -= round(cos(self.angle * pi / 180) * vitesse, 3)
            self.x += round(sin(self.angle * pi / 180) * vitesse, 3)

    def Droite(self, test, vitesse):
        """
        if test == 1:
                self.x -= round(cos(self.angle * pi / 180) * vitesse, 3)
        elif test == 2:
                self.y -= round(sin(self.angle * pi / 180) * vitesse, 3)
        elif test == 0:
                self.x -= round(cos(self.angle * pi / 180) * vitesse, 3)
                self.y -= round(sin(self.angle * pi / 180) * vitesse, 3)
        """
        if not test:
            self.x -= round(cos(self.angle * pi / 180) * vitesse, 3)
            self.y -= round(sin(self.angle * pi / 180) * vitesse, 3)

    def Gauche(self, test, vitesse):
        """
        if test == 1:
                self.x += round(cos(self.angle * pi / 180) * vitesse, 3)
        elif test == 2:
                self.y += round(sin(angle * pi / 180) * vitesse, 3)
        elif test == 0:
                self.x += round(cos(self.angle * pi / 180) * vitesse, 3)
                self.y += round(sin(self.angle * pi / 180) * vitesse, 3)
        """
        if not test:
            self.x += round(cos(self.angle * pi / 180) * vitesse, 3)
            self.y += round(sin(self.angle * pi / 180) * vitesse, 3)


#######################################################################################################
#######################################################################################################
#######################################################################################################


class Map:
    def __init__(self, p: Point, f) -> None:  # , lines: int = 8, columns: int = 8) -> None:
        self.lines = 16  # lines
        self.columns: int = 16  # columns
        self.map: list = []
        self.objects_list: list = []
        self.taille_case = 5
        self.nombre_case = 10
        self.size = 32
        self.vitesse = 3
        self.vitesse_rotation = 5
        self.perso = p
        self.position_map = (650, 150)
        self.frame = f
        self.canvas = None

    def add_object(self, point) -> None:
        self.objects_list.append(point)

    def load_map(self, file: str) -> None:
        """load the map"""
        self.map = list()
        with open(f"{file}.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                cols = []
                for col in row.strip():
                    cols.append(enum[col])
                self.map.append(cols)

    def print_map(self) -> None:
        """show the map"""
        height = self.size * self.lines
        width = self.size * self.columns
        self.canvas = tk.Canvas(self.frame, height=height, width=width, bg="white")
        self.canvas.place(x=self.position_map[0], y=self.position_map[1])
        pad = 0
        for y, row in enumerate(self.map):
            for x, _ in enumerate(row):
                x1 = pad + x * self.size
                y1 = pad + y * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size

                if self.map[y][x] == State.WALL:
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="black", outline="black"
                    )
                elif self.map[y][x] == State.EMPTY:
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill="white", outline="black"
                    )
        x, y = self.perso.get_position()
        # print("X :",x,"Y :", y)
        self.canvas.create_oval(
            x - 10, y - 10, x + 10, y + 10, fill="blue", outline="black"
        )
        # self.canvas.create_oval(self.xv - 5, self.yv - 5, self.xv + 5, self.yv + 5, fill = 'red')
        # self.canvas.create_oval(self.xh - 5, self.yh - 5, self.xh + 5, self.yh + 5, fill = 'red')
        # self.canvas.create_line(self.perso.x, self.perso.y, self.xv, self.yv, fill = 'red')
        self.frame.update()

    def define_camera_position(self) -> None:
        line, col = 0, 0
        while not self.map[line][col] is State.EMPTY:
            line = random.randint(1, self.lines - 2)
            col = random.randint(1, self.columns - 2)
        pos_x = (col + 0.5) * self.size
        pos_y = (line + 0.5) * self.size
        self.perso.set_position(pos_x, pos_y)
        self.map[line][col] = State.POINT
        self.xh, self.yh = self.PremiereInterHori()
        self.xv, self.yv = self.PremiereInterVert()

    def set_state(self, position: tuple, state: State) -> None:
        """set the state at position"""
        x, y = position
        self.map[x][y] = state

    def Avancer(self, event):
        x, y = self.perso.get_position()
        x -= sin(self.perso.get_angle() * pi / 180) * self.vitesse
        y += cos(self.perso.get_angle() * pi / 180) * self.vitesse
        test = self.Detection_collision(x, y)

        self.perso.Avancer(test, self.vitesse)
        self.print_map()

    def Reculer(self, event):
        x, y = self.perso.get_position()
        x += sin(self.perso.get_angle() * pi / 180) * self.vitesse
        y -= cos(self.perso.get_angle() * pi / 180) * self.vitesse

        test = self.Detection_collision(x, y)

        self.perso.Reculer(test, self.vitesse)
        self.print_map()

    def Droite(self, event):
        x, y = self.perso.get_position()
        x -= cos(self.perso.get_angle() * pi / 180) * self.vitesse
        y -= sin(self.perso.get_angle() * pi / 180) * self.vitesse

        test = self.Detection_collision(x, y)

        self.perso.Droite(test, self.vitesse)
        self.print_map()

    def Gauche(self, event):
        x, y = self.perso.get_position()
        x += cos(self.perso.get_angle() * pi / 180) * self.vitesse
        y += sin(self.perso.get_angle() * pi / 180) * self.vitesse

        test = self.Detection_collision(x, y)

        self.perso.Gauche(test, self.vitesse)
        self.print_map()

    def TournerDroite(self, event):
        angle = self.perso.get_angle()
        angle = (angle + 5) % 360
        self.perso.set_angle(angle)
        self.print_map()

    def TournerGauche(self, event):
        angle = self.perso.get_angle()
        angle = (angle - 5) % 360
        self.perso.set_angle(angle)
        self.print_map()
        self.print_map()

    def Detection_collision(self, x, y):
        x_ = (x - self.size / 2) / self.size
        y_ = (y - self.size / 2) / self.size
        # print("X :",x_, "Y :", y_)
        if self.map[int(y_)][int(x_)] and self.map[int(y_)][int(x_)] != State.WALL:
            return 0
        return 1

    def PremiereInterVert(self):
        x, y = self.perso.get_position()
        print(self.perso.angle)
        xv = int(x / self.size) * self.size
        if 180 <= self.perso.angle <= 359:
            xv += self.size

        yv = y - abs(x - xv) * tan(radians(self.perso.angle))
        return xv, yv

    def PremiereInterHori(self):
        x, y = self.perso.get_position()

        yh = int(y / self.size) * self.size
        if -90 <= self.perso.angle <= 90:
            yh += self.size

        xh = x + (abs(y - yh) / tan(radians(self.perso.angle)))
        return xh, yh

    def AffichageCone(self):
        distance = self.perso.distance_vue
        x, y = self.perso.get_position()

        pass
