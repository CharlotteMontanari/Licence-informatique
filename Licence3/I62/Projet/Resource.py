class Resource:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self) -> tuple:
        """
        return the resource position
        """
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"Une ressource a été posée en ({self.x}, {self.y})"
