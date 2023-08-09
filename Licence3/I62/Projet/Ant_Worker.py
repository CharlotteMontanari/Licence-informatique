from Ant import Ant


class Ant_Worker(Ant):
    def __init__(self, x, y, name, ident, form, life, stamina, stack, size, id_tk):
      super().__init__(x, y, name, ident)
      self.form = form
      self.life = life
      self.stamina = stamina
      self.stack = stack
      self.size = size
      self.x = 0
      self.y = 0
      self.id_tkinter = id_tk

    def __repr__(self) -> str:
        return f"worker"

    def get_stamina(self):
        """
        return the stamina of the ant worker
        """
        return self.stamina

    def get_stack(self):
        """
        return the stack of ressources of the ant worker
        """
        return self.stack