import unittest
from app.party import Party
from app.guest import Guest

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
