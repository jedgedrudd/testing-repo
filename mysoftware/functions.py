def square(x):
	return x*x

def coulomb(x):
	#if abs(x) == 0:
#		return 0
#	else:
#		return 1 / abs(r)
	assert type(x) in [float, int], "Invalid argument"
	try:
		return 1/abs(x)
	except ZeroDivisionError:
		return 0

def CentralDifference(f,x,h):
	# f(x+h) - f(x-h)
	# --------------- \approx f'(x)
	#       2*h
	return (f(x+h) - f(x-h))/(2*h)

for i in range(2,8):
	h = 10**(-i)
	print(h, abs(CentralDifferenv(np.sin,0.0,h) - 1.0))