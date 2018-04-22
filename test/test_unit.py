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