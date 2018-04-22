import unittest
from app.party import Party
from app.guest import Guest
from app.shoppingList import ShoppingList

def test_aPartywithNoGuestsShouldHaveNoPartyGuests():
	party = Party()
	assert 0 == party.numberOfGuests()


def test_aPartywithOneGuestShouldHaveOnePartyGuest():
	party = Party()
	lisa = Guest("Lisa", 'female')
	party.attendedBy(lisa)
	assert 1 == party.numberOfGuests()

def test_aPartywithThreeGuestsShouldHaveThreeGuests():
	party = Party()
	lisa = Guest("Lisa", 'female')
	rob = Guest("Rob", 'male')
	susan = Guest("susan", 'female')
	party.attendedBy(lisa)
	party.attendedBy(rob)
	party.attendedBy(susan)
	assert 3 == party.numberOfGuests()

def test_aGuestShouldBeAbleToLeaveAParty():
	party = Party()
	lisa = Guest("Lisa", 'female')
	rob = Guest("Rob", 'male')
	susan = Guest("susan", 'female')
	party.attendedBy(lisa)
	party.attendedBy(rob)
	party.attendedBy(susan)
	party.leftBy(rob)
	assert 2 == party.numberOfGuests()

def test_aPartyShouldHaveALocation():
	party = Party()
	party.setLocation("my House")
	assert "my House" == party.getLocation()


def test_aGuestShouldRevealHerName():
	guest1 = Guest("Lisa", "female")
	assert "Lisa" == guest1.hasName()

def test_weShouldKnowWhoIsAtTheParty():
	party = Party()
	lisa = Guest("Lisa", 'female')
	rob = Guest("Rob", 'male')
	susan = Guest("susan", 'female')
	party.attendedBy(lisa)
	party.attendedBy(rob)
	party.attendedBy(susan)
	assert ["Lisa", "Rob", "susan"] == party.getAttendees()


def test_weShouldBeAbleToCreateAnEmptyShoppingList():
	shoppingList = ShoppingList()
	assert shoppingList.getItems() == []

def test_weShouldBeAbleToAddItemsToShoppingList():
	shoppingList = ShoppingList()
	shoppingList.add("milk")
	assert shoppingList.getItems() == ["milk"]
