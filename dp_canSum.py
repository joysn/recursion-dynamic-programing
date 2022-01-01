
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