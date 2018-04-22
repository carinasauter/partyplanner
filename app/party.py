class Party():

	def __init__(self):
		self.listOfGuests = []


	def attendedBy(self, guest):
		self.listOfGuests.append(guest)


	def numberOfGuests(self):
		return len(self.listOfGuests)


	def leftBy(self, guest):
		self.listOfGuests.remove(guest)