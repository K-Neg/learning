x = 0.99
in_min = 0
in_max = 3.57
out_min = 30
out_max = 90

def map(x):
	y =(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
	return y

print(map(x))
