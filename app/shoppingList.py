class ShoppingList():
	def __init__(self):
		self.items = []

	def getItems(self):
		return self.items

	def add(self, item):
		self.items.append(item)

	def baseOn(self, party):
		self.items.append("wine for " + str(party.numberOfGuests() + 1))
		self.items.append("food for " + str(party.numberOfGuests() + 1))