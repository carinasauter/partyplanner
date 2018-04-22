class ShoppingList():
	def __init__(self):
		self.items = []

	def getItems(self):
		return self.items

	def add(self, item):
		self.items.append(item)