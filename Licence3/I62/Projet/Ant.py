class Ant:
    def __init__(self, x, y, name, id_nest):
        self.x = x
        self.y = y
        self.species = name
        self.id_nest = id_nest
        
    def get_ID(self) :
        """
        return the ID of the nest
        """
        return self.id_nest

    def get_X(self) :
        """
        return the x position of the ant
        """
        return self.x

    def get_Y(self) :
        """
        return the y position of the ant
        """
        return self.y

    def set_xy(self, x ,y):
        """
        move the ant
        """
        self.x = x
        self.y = y