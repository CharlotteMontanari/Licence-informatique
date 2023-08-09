import sys
import tkinter as tk
from turtle import position

sys.path.insert(0, "./src")

from enum import Enum, auto
from math import floor, sqrt
from random import randint

from actions import Action


# https://docs.python.org/3/howto/enum.html
class State(Enum):
    EMPTY = auto()
    ROBOT = auto()
    WALL = auto()
    MINE = auto()
    DEAD = auto()
    INVISIBLE = auto()
    HIT = auto()
    HIT_WALL = auto()
    TV = auto()
    TH = auto()
    WINNER = auto()


class ObjectMap:
    """Object of the map"""

    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0

    def set_position(self, x, y) -> None:
        """set the position in the dictionary"""
        self.x = x
        self.y = y

    def get_position(self) -> tuple:
        """get the position"""
        return self.x, self.y

    def get_name(self):
        pass

    def get_health(self):
        pass

    def get_speciality(self):
        pass

    def next_instruction(self):
        pass

    def isRobot(self):
        return False


# dictionary with all the map's object
enum = {
    "_": State.EMPTY,
    "#": State.WALL,
    "&": State.ROBOT,
    "@": State.MINE,
    "X": State.DEAD,
    "O": State.INVISIBLE,
    ".": State.HIT,
    "°": State.HIT_WALL,
    "|": State.TV,
    "-": State.TH,
    "!": State.WINNER,
}

reverse_enum = {
    State.EMPTY: "_",
    State.WALL: "#",
    State.ROBOT: "&",
    State.MINE: "@",
    State.DEAD: "X",
    State.INVISIBLE: "O",
    State.HIT: ".",
    State.HIT_WALL: "°",
    State.TV: "|",
    State.TH: "-",
    State.WINNER: "!",
}

spawn_positions = [(0, 0), (10, 15), (0, 29), (19, 0), (19, 15), (19, 29)]


class Field:
    def __init__(self, lines: int = 20, columns: int = 30) -> None:
        self.lines = lines
        self.columns: int = columns
        self.map: list = []
        self.objects_list: list = []  # list(ObjectMap)
        self.position_robots: list = []  # list(tuple)

    def __repr__(self) -> str:
        """print for the field"""
        return f"The map has {self.lines} lines and {self.columns} columns: {len(self.objects_list)} robots are fighting !!"

    def add_object(self, robot: ObjectMap) -> None:
        """add the object on the list"""
        print(
            f"{robot.get_name()} with {robot.get_health()} HP, {robot.get_speciality()} speciality is in game"
        )
        print()

        self.objects_list.append(robot)

    def load_map(self, file: str) -> None:
        """load the map"""
        self.map = list()
        with open(f"data/{file}.txt", "r") as f:
            rows = f.readlines()
            for row in rows:
                cols = []
                for col in row.strip():
                    cols.append(enum[col])
                self.map.append(cols)

    def print_map(self, frame, icons, x, y) -> None:
        """show the map"""
        size = 25
        height = size * self.lines
        width = size * self.columns

        canvas = tk.Canvas(frame, height=height, width=width, bg="#ABABAB")
        canvas.place(x=x, y=y)
        pad = 1
        for y, row in enumerate(self.map):
            for x, _ in enumerate(row):
                x1 = pad + x * size
                y1 = pad + y * size
                x2 = x1 + size
                y2 = y1 + size

                if self.map[y][x] == State.WALL:
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill="black", outline="black"
                    )

                elif self.map[y][x] == State.WINNER:
                    canvas.create_image(
                        x1 + 2, y1 + 2, anchor=tk.NW, image=icons["crown"]
                    )

                else:
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill="white", outline="black"
                    )

                if self.map[y][x] == State.ROBOT:
                    canvas.create_oval(x1, y1, x2, y2, fill="blue", outline="black")

                elif self.map[y][x] == State.INVISIBLE:
                    canvas.create_oval(x1, y1, x2, y2, fill="White", outline="black")

                elif self.map[y][x] == State.MINE:
                    canvas.create_image(
                        x1 + 2, y1 + 2, anchor=tk.NW, image=icons["bomb"]
                    )

                elif self.map[y][x] == State.DEAD:
                    canvas.create_image(
                        x1 + 2, y1 + 2, anchor=tk.NW, image=icons["dead"]
                    )

                elif self.map[y][x] == State.HIT:
                    canvas.create_oval(x1, y1, x2, y2, fill="red", outline="black")
                    self.set_state((y, x), State.ROBOT)

                elif self.map[y][x] == State.HIT_WALL:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black")
                    self.set_state((y, x), State.WALL)

                elif self.map[y][x] == State.TV or self.map[y][x] == State.TH:
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill="yellow", outline="black"
                    )

                    self.set_state((y, x), State.EMPTY)

        frame.update()

    def get_map(self) -> list:  # list(list(State))
        """get the map"""
        return self.map

    def define_robots_position(self) -> None:
        """position the robots on the map"""
        for obj in self.objects_list:
            if obj.isRobot():
                line, col = spawn_positions[randint(0, len(spawn_positions) - 1)]
                spawn_positions.remove((line, col))
                while not self.map[line][col] is State.EMPTY:
                    if line < self.lines - 1:
                        line += 1
                    elif col < self.columns - 1:
                        col += 1
                    elif col > 1:
                        col -= 1
                    elif line > 1:
                        line -= 1
                obj.set_position(line, col)
                print(f"Position {obj.name} at position ({line}, {col})")
                print()
                self.map[line][col] = State.ROBOT

    def compute_distance(self, r1: tuple, r2: tuple) -> int:
        """returns the distance between two robots"""
        x1, y1 = r1
        x2, y2 = r2
        x = abs((x1 - x2) * (x1 - x2))
        y = abs((y1 - y2) * (y1 - y2))
        return floor(sqrt(x + y))

    def is_a_robot_close(self, robot) -> tuple:
        """return true if a robot is close"""
        for obj in self.objects_list:
            if obj.isRobot() and obj.is_visible():
                distance = self.compute_distance(
                    robot.get_position(), obj.get_position()
                )
                if 0 < distance <= robot.radar:
                    print(f"{obj.name} is close to {robot.name} ({distance})")
                    return True, robot
        return False, None

    def move_robot(self, instruction, robot) -> tuple:
        """performs random robot movement: AL, DD"""
        movement_list = ["D", "G", "H", "B"]
        x, y = robot.get_position()
        line, col = robot.get_position()
        move = "NOOP"
        if instruction == "AL":
            move = movement_list[randint(0, len(movement_list) - 1)]
        elif "DD" in instruction:
            move = instruction.split(" ")[1]
        if (
            move == "D"
            and col < self.columns - 1
            and self.map[line][col + 1] is State.EMPTY
        ):
            x = line
            y = col + 1
            self.map[line][col] = State.EMPTY

        elif move == "G" and col > 1 and self.map[line][col - 1] is State.EMPTY:
            x = line
            y = col - 1
            self.map[line][col] = State.EMPTY

        elif move == "H" and line > 1 and self.map[line - 1][col] is State.EMPTY:
            x = line - 1
            y = col
            self.map[line][col] = State.EMPTY

        elif (
            move == "B"
            and line < self.lines - 1
            and self.map[line + 1][col] is State.EMPTY
        ):
            x = line + 1
            y = col
            self.map[line][col] = State.EMPTY
        else:
            print(f"{robot.name} cannot move {move}")

        if (x, y) != (line, col):
            print(f"{robot.name} is now at ({x}, {y}) with {move}")
            # Check if there is a mine
            if self.map[x][y] == State.MINE:
                # Check if this is my mine
                if not robot.is_my_mine((x, y)):
                    # Not my mine, getting damage
                    robot.decrease_health(Action("MI").get_damage())
                    robot.replace_by_emergency()
            # Moving robot to new position
            self.map[x][y] = State.ROBOT
            robot.set_position(x, y)
            return (x, y)

        return (-1, -1)

    def set_state(self, position: tuple, state: State) -> None:
        """set the state at position"""
        x, y = position
        self.map[x][y] = state

    def get_mine_position(self, position: tuple) -> tuple:
        """get mine position"""
        line, col = position
        x, y = position

        if line < self.lines - 1 and self.map[line + 1][col] is State.EMPTY:
            x = line + 1
            y = col

        elif col < self.columns - 1 and self.map[line][col + 1] is State.EMPTY:
            x = line
            y = col + 1

        elif col > 1 and self.map[line][col - 1] is State.EMPTY:
            x = line
            y = col - 1

        elif line > 1 and self.map[line - 1][col] is State.EMPTY:
            x = line - 1
            y = col

        if (x, y) != (line, col):
            return (x, y)

        return (-1, -1)

    def shoot(self, robot, instruction) -> tuple:
        """play shooting instruction: TV, TH"""
        tv = ["up", "down"]
        th = ["right", "left"]
        x, y = robot.get_position()
        if instruction == "TV":
            direction_tv = tv[randint(0, len(tv) - 1)]
            if direction_tv == "up":
                x -= 1
                while x >= 0:
                    if self.map[x][y] == State.WALL:
                        print(f"{robot.get_name()} hit a wall at ({x},{y})")
                        self.set_state((x, y), State.HIT_WALL)
                        return (-2, -2)

                    elif self.map[x][y] == State.ROBOT:
                        self.set_state((x, y), State.HIT)
                        return x, y

                    elif self.map[x][y] == State.MINE and not robot.is_my_mine((x, y)):
                        self.set_state((x, y), State.EMPTY)
                        for robot in self.objects_list:
                            if robot.isRobot() and robot.is_my_mine((x, y)):
                                robot.remove_mine((x, y))
                        return x, y

                    elif self.map[x][y] == State.EMPTY:
                        self.set_state((x, y), State.TV)

                    x -= 1
            else:
                x += 1
                while x < self.lines:
                    if self.map[x][y] == State.WALL:
                        print(f"{robot.get_name()} hit a wall at ({x},{y})")
                        self.set_state((x, y), State.HIT_WALL)
                        return (-2, -2)

                    elif self.map[x][y] == State.ROBOT:
                        self.set_state((x, y), State.HIT)
                        return x, y

                    elif self.map[x][y] == State.MINE and not robot.is_my_mine((x, y)):
                        self.set_state((x, y), State.EMPTY)
                        for robot in self.objects_list:
                            if robot.isRobot() and robot.is_my_mine((x, y)):
                                robot.remove_mine((x, y))
                        return x, y

                    elif self.map[x][y] == State.EMPTY:
                        self.set_state((x, y), State.TV)

                    x += 1

        elif instruction == "TH":
            direction_th = th[randint(0, len(th) - 1)]
            if direction_th == "right":
                y += 1
                while y < self.columns:
                    if self.map[x][y] == State.WALL:
                        print(f"{robot.get_name()} hit a wall at ({x},{y})")
                        self.set_state((x, y), State.HIT_WALL)
                        return (-2, -2)

                    elif self.map[x][y] == State.ROBOT:
                        self.set_state((x, y), State.HIT)
                        return x, y

                    elif self.map[x][y] == State.MINE and not robot.is_my_mine((x, y)):
                        self.set_state((x, y), State.EMPTY)
                        for robot in self.objects_list:
                            if robot.isRobot() and robot.is_my_mine((x, y)):
                                robot.remove_mine((x, y))
                        return x, y

                    else:
                        self.set_state((x, y), State.TH)

                    y += 1
            else:
                y -= 1
                while y >= 0:
                    if self.map[x][y] == State.WALL:
                        print(f"{robot.get_name()} hit a wall at ({x},{y})")
                        self.set_state((x, y), State.HIT_WALL)
                        return (-2, -2)

                    elif self.map[x][y] == State.ROBOT:
                        self.set_state((x, y), State.HIT)
                        return x, y

                    elif self.map[x][y] == State.MINE and not robot.is_my_mine((x, y)):
                        self.set_state((x, y), State.EMPTY)
                        for robot in self.objects_list:
                            if robot.isRobot() and robot.is_my_mine((x, y)):
                                robot.remove_mine((x, y))
                        return x, y

                    else:
                        self.set_state((x, y), State.TH)

                    y -= 1

        print(f"{robot.get_name()} hit nothing")
        return (-1, -1)

    def get_closest_position(self, position_r1: tuple, position_r2: tuple) -> tuple:
        """returns the closest position of the target robot during instruction PS"""
        x, y = position_r1
        possible_position = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
        ]
        closer_position = x, y
        minimum = 600
        for position in possible_position:
            x1, y1 = position
            if (
                0 < x1 < self.lines
                and 0 < y1 < self.columns
                and self.map[x1][y1] == State.EMPTY
            ):
                min_distance = self.compute_distance(position, position_r2)
                if minimum > min_distance:
                    minimum = min_distance
                    closer_position = position
        print("Closer: ", closer_position)
        return closer_position

    def get_farthest_position(self, position_r1: tuple, position_r2: tuple) -> tuple:
        """returns the farthest position of the target robot during instruction PS"""
        x, y = position_r1
        possible_position = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
        ]
        farthest_position = x, y
        maximum = 0
        for position in possible_position:
            x1, y1 = position
            if (
                0 < x1 < self.lines
                and 0 < y1 < self.columns
                and self.map[x1][y1] == State.EMPTY
            ):
                max_distance = self.compute_distance(position, position_r2)
                if maximum < max_distance:
                    maximum = max_distance
                    farthest_position = position
        print("Farthest: ", farthest_position)
        return farthest_position
