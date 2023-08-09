from logging import root
from random import randint
from turtle import position

from actions import Action
from terrain import Field, ObjectMap, State


class Robot(ObjectMap):
    def __init__(self, name: str, health: int, speciality: str, radar: int = 4) -> None:
        self.name: str = name  # nom
        self.health = health  # point de vie
        self.speciality: str = speciality  # comportement
        self.instruction: list = []  # instructions
        self.radar: int = radar  # distance de reperage
        self.landed_mines: list = []  # mine posee
        self.emergency_circuit: str = ""  # instruction de secours
        self.step = 0  # etape des instructions
        self.type = State.ROBOT

    def __repr__(self) -> str:
        """display for robots"""
        return f"{self.name} has now {self.health} HP"

    def print_hp(self) -> str:
        """display for health into or listbox"""
        return f"has now {self.health} HP"

    def isRobot(self):
        """return true if the object is a robot"""
        return True

    def get_name(self) -> str:
        """return robot's name"""
        return self.name

    def get_health(self) -> int:
        """return robot's health"""
        return self.health

    def get_emergency_circuit(self) -> str:
        """return emergency circuit'"""
        return self.emergency_circuit

    def get_speciality(self) -> str:
        """return robot's speciality"""
        return self.speciality

    def load_program(self) -> None:
        """
        read the file .rbt corresponding to speciality
        the first line corresponding robot's emergency circuit
        and the others corresponding robot's programm
        """
        instruction_list = [
            "MI",
            "DD D",
            "DD G",
            "DD H",
            "DD B",
            "AL",
            "PS",
            "FT",
            "IN",
            "TV",
            "TH",
            "TT"
        ]
        with open(f"data/{self.speciality}.rbt", "r") as f:
            lignes = f.readlines()
            if 6 <= len(lignes) <= 21:
                if lignes[1].rstrip("\n") not in instruction_list:
                    print(f"Corrupted file: {lignes[1]}")
                    exit(1)
                else:
                    self.emergency_circuit = lignes[1].rstrip("\n")
                for ligne in lignes[2:]:
                    if ligne.rstrip("\n") not in instruction_list:
                        print(f"Corrupted file: {ligne}")
                        exit(1)
                    else:
                        self.instruction.append(ligne.rstrip("\n"))
            else:
                print("Corrupted file")
                exit(1)

    def get_next_instruction(self) -> str:
        """
        return the next instruction to execute
        when it's the end of the instruction, we go back to the geggin
        """
        curr_step = self.step % len(self.instruction)
        self.step += 1
        instruction = self.instruction[curr_step]
        return instruction

    def next_instruction(self, radar: bool, insert_str: str) -> tuple:
        """
        get next instruction to do
        check if robot has enough health to execute the instruction
        else, he died
        """
        super().next_instruction()
        a = Action(self.get_next_instruction())
        if insert_str != "":
            insert_str = f"{insert_str}, "
        else:
            insert_str = f"{self.name} "
        insert_str = insert_str + f"played {a.get_move()}"

        if self.health > a.get_cost():
            self.decrease_health(a.get_cost())
            insert_str = insert_str + f", lost {a.get_cost()} HP"
        else:
            self.health = 0
        if a.get_move() == "TT":
            if radar:
                self.next_instruction(radar, insert_str)  # play the first one
            else:
                self.get_next_instruction()  # play the second instruction after TT
                return self.next_instruction(radar, insert_str)

        elif a.get_move() == "IN":
            self.set_type(State.INVISIBLE)

        print(f"{insert_str}")
        return (a.get_move(), insert_str)

    def remember_my_mine(self, position: tuple) -> None:
        """lay the mine"""
        print(f"landed mine at {position}")
        self.landed_mines.append(position)

    def is_my_mine(self, position: tuple) -> bool:
        """return true is it's robot's mine"""
        for mine in self.landed_mines:
            if mine == position:
                return True
        return False

    def is_visible(self) -> bool:
        """
        return true if the robot is not invisible
        """
        return not self.type == State.INVISIBLE

    def set_type(self, type: State) -> None:
        """change robot's state"""
        self.type = type

    def decrease_health(self, health) -> None:
        """decrease robot's health"""
        if self.health > health:
            self.health -= health
        else:
            self.health = 0

    def remove_mine(self, position: tuple) -> None:
        """remove the mine if this is touch by shoot"""
        for mine in self.landed_mines:
            if mine[0] == position[0] and mine[1] == position[1]:
                self.landed_mines.remove(mine)

    def replace_by_emergency(self) -> None:
        """if a robot walk on ennemy's mine, he play emergency circuit"""
        curr_step = self.step % len(self.instruction)
        self.instruction[curr_step] = self.emergency_circuit
