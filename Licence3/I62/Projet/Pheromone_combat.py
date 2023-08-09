from Pheromone import Pheromone

class Fight_pheromones(Pheromone):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        """
        return the color of the pheromone
        """
        return self.color