def canSum(target,numbers):

	if target in memo.keys():
		return memo[target]

	if target == 0:
		return True
	if target < 0:
		return False

	for ele in numbers:
		if canSum(target-ele,numbers):
			memo[target] = True
			return True
	
	memo[target] = False
	return False

def canSum_bottomup(target,numbers):
	tab = [False for i in range(target+1)]

	tab[0] = True

	for i in range(target+1):
		if tab[i] == True:
			for num in numbers:
				if i+num <= target:
					tab[i+num] = True
					if i+num == target:
						return tab[i+num]

	return tab[target]

# m = target
# n = number of numbers
# Brute
# Time = O(n^m)
# Space = O(m)
# Memo
# Time = O(n*m)
# Space = O(m)
# Tabular
# Time = O(n*m)
# Space = O(n)
if __name__ == "__main__":

	memo = dict()
	count = 0
	print("True",canSum(7,[4,5,3,7]),count)

	memo = dict()
	count = 0
	print("False",canSum(7,[4,5]),count)

	memo = dict()
	count = 0
	print("True",canSum(7,[2,3]),count)

	memo = dict()
	count = 0
	print("False",canSum(7,[4,2]),count)

	memo = dict()
	count = 0
	print("True",canSum(8,[2,3,5]),count)


	memo = dict()
	count = 0
	print("False",canSum(300,[7,14]),count)

	# for i in range(1,50):
	# 	memo = dict()
	# 	count = 0
	# 	print(i,canSum(i,[4,3,7]),count)

	print("True",canSum_bottomup(7,[4,5,3,7]))
	print("False",canSum_bottomup(7,[4,5]))
	print("True",canSum_bottomup(7,[2,3]))
	print("False",canSum_bottomup(7,[4,2]))
	print("True",canSum_bottomup(8,[2,3,5]))
	print("False",canSum_bottomup(300,[7,14]))


# (base) coding % python canSum.py 
# True True 0
# False False 0
# True True 0
# False False 0
# True True 0
# False False 0
# True True
# False False
# True True
# False False
# True True
# False False