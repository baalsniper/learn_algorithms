def largestdivisor(a,b):
	if b == 0: return a
	else: return largestdivisor(b, a % b)

number = map(int, raw_input().split())
if number[0] > number[1]:
	divisor = largestdivisor(number[0],number[1])
else: divisor = largestdivisor(number[1],number[0])

print ("the largest divisor of {} and {} is {}".format(number[0],number[1], divisor))