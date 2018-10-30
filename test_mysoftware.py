from mysoftware import *

def test_square_integers():
	assert square(2) == 4
	assert square(0) == 0
	assert square(-1) == 1
	#assert square(3) == 10

	print("Square passed all tests")

def test_coulomb():
	assert coulomb(1.0) == 1.0
	assert coulomb(2.0) == 0.5
	assert coulomb(-2.0) == 0.5
	assert coulomb(0.0) 

def test_coulomb_throws_error():
	try:
		coulomb(0.0)
		raise Exception("Test failed")
	except ZeroDivisionError:
		raise Exception("Test failed with div0")
	except ValueError:
		pass