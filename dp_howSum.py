import copy
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

def howSum_bottomup(target,numbers):

	tab = [None for i in range(target+1)]
	
	tab[0] = []
	for i in range(target+1):
		if tab[i] is not None:
			for num in numbers:
				if i+num <= target:
					tab[i+num] = copy.deepcopy(tab[i])
					tab[i+num].append(num)
					if i+num == target:
						return tab[i+num]

	return tab[target]

# n = len(numbers)
# m = targetSum

# Brute Force
# Time = O(n^m)
# Space = O(m)

# Memoization
# Time = O(n*m)  
# Space = O(m*m)

# Bottom Up
# Time = O(n*m*m) - last m is due to copying m array everytime
# Space = O(m*m) - last m is due to time required to copy m sized array

if __name__ == "__main__":

	memo = dict()
	print("7,[4,5,3,7] True",howSum(7,[4,5,3,7]))

	memo = dict()
	print("7,[4,5] False",howSum(7,[4,5]))

	memo = dict()
	print("7,[2,3] True",howSum(7,[2,3]))

	memo = dict()
	print("7,[4,2] False",howSum(7,[4,2]))

	memo = dict()
	print("8,[2,3,5] True",howSum(8,[2,3,5]))

	memo = dict()
	print("0,[2,3,5] False",howSum(0,[2,3,5]))

	memo = dict()
	print("300,[7,14] False",howSum(300,[7,14]))

	# for i in range(1,50):
	# 	memo = dict()
	# 	count = 0
	# 	print(i,howSum(i,[4,3,7]),count)

	print("7,[4,5,3,7] True",howSum_bottomup(7,[4,5,3,7]))
	print("7,[4,5] False",howSum_bottomup(7,[4,5]))
	print("7,[2,3] True",howSum_bottomup(7,[2,3]))
	print("7,[4,2] False",howSum_bottomup(7,[4,2]))
	print("8,[2,3,5] True",howSum_bottomup(8,[2,3,5]))
	print("0,[2,3,5] False",howSum_bottomup(0,[2,3,5]))
	print("300,[7,14] False",howSum_bottomup(300,[7,14]))

# (base) coding % python howSum.py 
# 7,[4,5,3,7] True [3, 4]
# 7,[4,5] False None
# 7,[2,3] True [3, 2, 2]
# 7,[4,2] False None
# 8,[2,3,5] True [2, 2, 2, 2]
# 0,[2,3,5] False []
# 300,[7,14] False None
# 7,[4,5,3,7] True [7]
# 7,[4,5] False None
# 7,[2,3] True [2, 2, 3]
# 7,[4,2] False None
# 8,[2,3,5] True [3, 5]
# 0,[2,3,5] False []
# 300,[7,14] False None