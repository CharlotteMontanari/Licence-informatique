import Ant as A
import Ant_Queen as a_q
import Ant_Scout as a_s
import Ant_Worker as a_w

# Stats worker
FORM_WORKER = "triangle"
LIFE_WORKER = 500
STAMINA_WORKER = 500
STACK_WORKER = 5000
SIZE_WORKER = 4

# Stats scout
FORM_SCOUT = "oval"
LIFE_SCOUT = 100
STAMINA_SCOUT = 1000
STACK_SCOUT = 200
SIZE_SCOUT = 3

# Stats queen
FORM_QUEEN = "rectangle"
LIFE_QUEEN = 5000
STAMINA_QUEEN = 0
STACK_QUEEN = 5000
SIZE_QUEEN = 10


class Nest:
    def __init__(self, x, y, name, Nb_Worker, Nb_Scout, Nb_Queen):
        self.x = x
        self.y = y
        self.species = name

        self.ant_Worker = Nb_Worker
        self.list_Worker = []

        self.ant_Scout = Nb_Scout
        self.list_Scout = []

        self.ant_Queen = Nb_Queen
        self.list_Queen = []

    def __repr__(self) -> str:
        return f"Un nid a été posée en ({self.x}, {self.y}) avec {self.ant_Worker} worker, {self.ant_Scout} scout, {self.ant_Queen} queen"

    def create_worker(self, canvas, species):
        """
        instantiate worker ants
        """
        for _ in range(self.ant_Worker):
            id_tk = canvas.create_oval(
                self.x,
                self.y,
                self.x + SIZE_WORKER,
                self.y + SIZE_WORKER,
                fill=species,
                outline="black",
            )
            self.list_Worker += [
                a_w.Ant_Worker(
                    self.x,
                    self.y,
                    self.species,
                    self,
                    FORM_WORKER,
                    LIFE_WORKER,
                    STAMINA_WORKER,
                    STACK_WORKER,
                    SIZE_WORKER,
                    id_tk,
                )
            ]

    def create_scout(self, canvas, species):
        """
        instantiate scout ants
        """
        for _ in range(self.ant_Scout):
            id_tk = canvas.create_oval(
                self.x,
                self.y,
                self.x + SIZE_SCOUT,
                self.y + SIZE_SCOUT,
                fill=species,
                outline="black",
            )
            self.list_Scout += [
                a_s.Ant_Scout(
                    self.x,
                    self.y,
                    self.species,
                    self,
                    FORM_SCOUT,
                    LIFE_SCOUT,
                    STAMINA_SCOUT,
                    STACK_SCOUT,
                    SIZE_SCOUT,
                    id_tk,
                )
            ]

    def create_queen(self, canvas, species):
        """
        instantiate queen ants
        """
        for _ in range(self.ant_Queen):
            id_tk = canvas.create_oval(
                self.x,
                self.y,
                self.x + SIZE_QUEEN,
                self.y + SIZE_QUEEN,
                fill=species,
                outline="black",
            )
            self.list_Queen += [
                a_q.Ant_Queen(
                    self.x,
                    self.y,
                    self.species,
                    self,
                    FORM_QUEEN,
                    LIFE_QUEEN,
                    STAMINA_QUEEN,
                    STACK_QUEEN,
                    SIZE_QUEEN,
                    id_tk,
                )
            ]

    def get_X(self):
        """
        return the x position of the nest
        """
        return self.x

    def get_Y(self):
        """
        return the y position of the nest
        """
        return self.y

    def get_Species(self):
        """
        return the name of the species
        """
        return self.species

    def get_antWorker(self):
        """
        return the number of worker ants
        """
        return self.ant_Worker

    def get_antScout(self):
        """
        return the number of scout ants
        """
        return self.ant_Scout

    def get_antQueen(self):
        """
        return the number of queen ants
        """
        return self.ant_Queen
