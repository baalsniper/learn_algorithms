import time

def check(number,l,r,find):
	if number[r] < find:
		return False
	while l <= r:
		mid = l + (r-l)/2
		if number[mid] == find:
			return mid
		elif number[mid] > find:
			r = mid -1
		else:
			l = mid + 1
	return False 
	
i = [i for i in xrange(0,10000000,3)]
t0 = time.time()
number = check(i,0,len(i)-1,9234135)
if number == False: print "No number in list"
else: print number, i[number]
t1 = time.time()
print("Time required: ", t1-t0)

#number = map(int, raw_input().split())
#find = int(raw_input())


