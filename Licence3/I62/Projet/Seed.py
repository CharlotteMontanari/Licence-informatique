import Resource as r

class Seed(r.Resource):
	def __init__(self, x, y, value, quantity) -> None:
		super().__init__(x, y)
		self.value = value
		self.quantity = quantity

	def change_value(cls, n : int):
		"""
		change the seed value
		"""
		cls.value = n

	def change_quantity(cls, n : int):
		"""
		change the seed quantity
		"""
		cls.quantity = n
	change_value = classmethod(change_value)
	change_quantity = classmethod(change_quantity)
