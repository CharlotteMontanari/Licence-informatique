import Resource as r

class Water(r.Resource):
	def __init__(self, x, y, value, quantity) -> None:
		super().__init__(x, y)
		self.value = value
		self.quantity = quantity

	def change_value(cls, n: int):
		"""
		change the water value
		"""
		cls.value = n

	def change_quantity(cls, n: int):
		"""
		change the water quantity 
		"""
		cls.quantity = n
	
	change_value = classmethod(change_value)
	change_quantity = classmethod(change_quantity)
