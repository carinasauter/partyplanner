class Party():

	def __init__(self):
		self.listOfGuests = []


	def attendedBy(self, guest):
		self.listOfGuests.append(guest)


	def numberOfGuests(self):
		return len(self.listOfGuests)


	def leftBy(self, guest):
		self.listOfGuests.remove(guest)

	def getLocation(self):
		return self.location

	def setLocation(self, location):
		self.location = location

	def getAttendees(self):
		result = []
		for guest in self.listOfGuests:
			result.append(guest.hasName())
		return result