# write finboacci(n) in logn time



cache = []
def fib(n):
	
	l = len(cache)
	#print(cache, l)
	if l >= n+1:
		return cache[n]
	else:	
		if l < 1:
			cache.append(1)
		if l < 2:
			cache.append(1)
		for i in range(len(cache),n+1):
			#print(i,cache[i-1],cache[i-2])
			cache.append(cache[i-1]+cache[i-2])
		#print(cache)
		return cache[n]
		
print("Fib of 0(1) is ",fib(0))
print("Fib of 2(2) is ",fib(2))
print("Fib of 4(5) is ",fib(4))
print("Fib of 8(34) is ",fib(8))

# o(n), o(n)
def fib(n):
	cache = []
	if n == 0 or n == 1:
		return 1
	cache.append(1)
	cache.append(1)
	for i in range(2,n+1):
		cache.append(cache[i-1]+cache[i-2])
	return cache[n]
		
print("Fib of 0(1) is ",fib(0))
print("Fib of 2(2) is ",fib(2))
print("Fib of 4(5) is ",fib(4))
print("Fib of 8(34) is ",fib(8))


# o(n), o(1)
def fib(n):
	
	if n == 0 or n == 1:
		return 1
	a = 1
	b = 1
	for i in range(2,n+1):
		c = a + b
		a = b
		b = c
	return c
		
print("Fib of 0(1) is ",fib(0))
print("Fib of 2(2) is ",fib(2))
print("Fib of 4(5) is ",fib(4))
print("Fib of 8(34) is ",fib(8))

