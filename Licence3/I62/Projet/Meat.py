import Resource as r

class Meat(r.Resource):
	def __init__(self, x, y, value, quantity) -> None:
		super().__init__(x, y)
		self.value = value
		self.quantity = quantity

	def __repr__(self) -> str:
		return "Meat was created"

	def change_value(cls, n : int):
		"""
		change the value of a meat resource
		"""
		cls.value = n

	def change_quantity(cls, n : int):
		"""
		change the quantity of a meat resource
		"""
		cls.quantity = n
	change_value = classmethod(change_value)
	change_quantity = classmethod(change_quantity)
