def howSum(target,numbers):
	if target in memo.keys():
		return memo[target]

	if target == 0:
		return []
	if target < 0:
		return None

	for ele in numbers:
		res = howSum(target-ele,numbers)
		if res is not None:
			res.append(ele)
			memo[target] = res
			return res

	memo[target] = None
	return None

# n = len(numbers)
# m = targetSum

# Brute Force
# Time = O(n^m)
# Space = O(m)

# Memoization
# Time = O(n*m)  
# Space = O(m*m)

if __name__ == "__main__":

	memo = dict()
	count = 0
	print("7,[4,5,3,7] True",howSum(7,[4,5,3,7]))

	memo = dict()
	count = 0
	print("7,[4,5] False",howSum(7,[4,5]))

	memo = dict()
	count = 0
	print("7,[2,3] True",howSum(7,[2,3]))

	memo = dict()
	count = 0
	print("7,[4,2] False",howSum(7,[4,2]))

	memo = dict()
	count = 0
	print("8,[2,3,5] True",howSum(8,[2,3,5]))

	memo = dict()
	count = 0
	print("0,[2,3,5] False",howSum(0,[2,3,5]))

	memo = dict()
	count = 0
	print("300,[7,14] False",howSum(300,[7,14]))

	# for i in range(1,50):
	# 	memo = dict()
	# 	count = 0
	# 	print(i,howSum(i,[4,3,7]),count)