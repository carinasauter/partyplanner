import unittest
from app.party import Party

def test_noPartyGuests():
	party = Party()
	assert 0 == party.numberOfGuests()