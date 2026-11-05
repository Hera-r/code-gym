import pytest
from workbench.greeting import greet


def test_greet_success():
	assert greet("Luffy") == "Salama, Luffy"
	assert greet("Zoro") == "Salama, Zoro"

@pytest.mark.parametrize("name", ["", " ", "Barbe Noir", "  SpacesBefore"])
def test_greet_invalid_inputs(name):
	with pytest.raises(ValueError, match="The input string cannot be empty or contain any spaces"):
		greet(name)
