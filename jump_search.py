import time

def check(number,find):
	sqrt = int((len(number))**0.5)
	a = 0
	if number[-1] < find:
		return -1

	while number[a] < find:
		a += sqrt
		if a > len(number): 
			a = len(number)-1

	for i in range(a-sqrt,a+1):
		if number[i] == find: return i
	
	return -1


number = range(-100,100,3)
t0 = time.time()
js = check(number, 80)
print js
t1 = time.time()
print ('Time required: ',t1-t0)