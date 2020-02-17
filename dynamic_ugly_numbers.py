# https://www.geeksforgeeks.org/ugly-numbers/
# Ugly Numbers
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

# Given a number n, the task is to find n’th Ugly number.

# Examples:
# Input  : n = 7
# Output : 8

# Input  : n = 10
# Output : 12

# Input  : n = 15
# Output : 24

# Input  : n = 150
# Output : 5832


def ugly_number(n):
	if n == 0:
		return None
	if n == 1:
		return 1
	
	#cache = [0 for i in range(n+1)]
	mydict = dict()
	
	#cache[1] = 1
	prev = 1
	mydict['1'] = 1
	
	for i in range(2,n+1):
		offset = 1
		#prev = cache[i-1]
		while True:
			if (prev+offset)%2 == 0 and str(int((prev+offset)/2)) in mydict.keys():
					#cache[i] = prev+offset
					prev = prev+offset
					#mydict[str(prev+offset)] = 1
					mydict[str(prev)] = 1
					break
			elif (prev+offset)%3 == 0 and str(int((prev+offset)/3)) in mydict.keys():
					#cache[i] = prev+offset
					prev = prev+offset
					#mydict[str(prev+offset)] = 1
					mydict[str(prev)] = 1
					break
			elif (prev+offset)%5 == 0 and str(int((prev+offset)/5)) in mydict.keys():
					#cache[i] = prev+offset
					prev = prev+offset
					#mydict[str(prev+offset)] = 1
					mydict[str(prev)] = 1
					break
			else:
				offset += 1
		
	print(cache[1:]) if debug else None
	print(prev) if debug else None
	#return cache[n]
	return prev
			

debug = True
debug = False
print("The 7th ugly number is",ugly_number(7))
print("The 10th ugly number is",ugly_number(10))
print("The 15th ugly number is",ugly_number(15))
print("The 150th ugly number is",ugly_number(150))

# (base) D:\>python dynamic_ugly_numbers.py
# The 7th ugly number is 8
# The 10th ugly number is 12
# The 15th ugly number is 24
# The 150th ugly number is 5832
