import pytest

def test_calc_addition():
	#fonction test du résultat de 2+4
	output = 2+4
	assert output == 6

def test_calc_substraction():
	#fonction test du résultat de 2-4
	output = 2-4
	assert output == -2
def test_calc_multiply():
	#fonction test du résultat de 2*4
	output = 2*4
	assert output == 8
def test_coucou():
	#Fonction test de renvoi de "hello"
	output = "Hello"
	assert output == "Hello"
