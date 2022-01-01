def fib_recurse(n):
	if n <= 2:
		return 1
	else:
		return fib_recurse(n-1) + fib_recurse(n-2)


my_fib = dict()

def fib_memo(n):
	if n in my_fib.keys():
		return my_fib[n]
	elif n <= 2:
		my_fib[n] = 1
	else:
		my_fib[n] = fib_memo(n-1) + fib_memo(n-2)

	return my_fib[n]

def fib_bot_up(n):

	if n <= 2:
		return 1
	first = 1
	second = 1
	for i in range(3,n+1):
		sum = first + second
		first = second
		second = sum
		
	return second


if __name__ == "__main__":
	for i in range(1,10):
		print(fib_recurse(i),end=" ")
	print("\n")

	for i in range(1,51):
		print(fib_memo(i),end=" ")
	print("\n")

	for i in range(1,51):
		print(fib_bot_up(i),end=" ")
	print("\n")