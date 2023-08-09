class Pheromone:
    def __init__(self, x, y, quantity) :
        self.x = x
        self.y = y
        self.quantity = quantity

    def get_X(self):
        """
        return the x position of the pheromone
        """
        return self.x

    def get_Y(self):
        """
        return the y posiition of the pheromone
        """
        return self.y

    def get_quantity(self):
        """
        return the pheromones quantity
        """
        return self.quantity

    def set_quantity(self, n: int):
        """
        set the quantity to n
        """
        self.quantity = n
