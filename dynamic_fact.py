# Write recursive and nonrecursive function to calculate factorial of n ^ 2


def fact(n):
	if n < 0:
		return 0
	if n == 0 or n == 1:
		return n
	return(n * fact(n-1))


def fact_nonrecursive(n):
	if n == 0 or n == 1:
		return n
	f = 1
	for i in range(1,n+1):
		f = f * i
	return f

print("fact of -1 power 2 is: ",fact(pow(-1,2)))	
print("fact of 0 power 2 is: ",fact(pow(0,2)))
print("fact of 1 power 2 is: ",fact(pow(1,2)))
print("fact of 2 power 2 is: ",fact(pow(2,2)))
print("fact of 3 power 2 is: ",fact(pow(3,2)))


print("Non recursive fact of -1 power 2 is: ",fact_nonrecursive(pow(-1,2)))	
print("Non recursivefact of 0 power 2 is: ",fact_nonrecursive(pow(0,2)))
print("Non recursivefact of 1 power 2 is: ",fact_nonrecursive(pow(1,2)))
print("Non recursivefact of 2 power 2 is: ",fact_nonrecursive(pow(2,2)))
print("Non recursivefact of 3 power 2 is: ",fact_nonrecursive(pow(3,2)))


# (base) D:\>python dynamic_fact.py
# fact of -1 power 2 is:  1
# fact of 0 power 2 is:  0
# fact of 1 power 2 is:  1
# fact of 2 power 2 is:  24
# fact of 3 power 2 is:  362880
# Non recursive fact of -1 power 2 is:  1
# Non recursivefact of 0 power 2 is:  0
# Non recursivefact of 1 power 2 is:  1
# Non recursivefact of 2 power 2 is:  24
# Non recursivefact of 3 power 2 is:  362880

