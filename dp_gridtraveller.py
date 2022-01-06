def grid_traveller(n,m):
	if n <= 0 or m <= 0:
		return 0
	if n == 1 or m == 1:
		return 1

	return grid_traveller(n-1,m) + grid_traveller(n,m-1)

def grid_traveller_memo(row,col):

	if row <= 0 or col <= 0:
		return 0
	if row == 1 or col == 1:
		return 1

	if memo[row-1][col-1] is not None:
		return memo[row-1][col-1]

	memo[row-1][col-1] = grid_traveller_memo(row-1,col) + grid_traveller_memo(row,col-1)
	return memo[row-1][col-1]

def grid_traveller_tabular(row,col):

	tab = [[0 for c in range(col+1)] for r in range(row+1)]
	#print(tab)

	# Base case
	tab[1][1] = 1

	for r in range(1,row+1):
		for c in range(1,col+1):
			if r+1 <= row:
				tab[r+1][c] += tab[r][c]
			if c+1 <= col:
				tab[r][c+1] += tab[r][c]

	return tab[r][c]

# Brute
# Time = O(2^(n+m)))
# Space = O(n+m)
# Memo
# Time = O(m*n)
# Space = O(n+m)
# Tabular
# Time = O(m*n)
# Space = O(m*n)

if __name__ == "__main__":
	print(grid_traveller(1,1))
	print(grid_traveller(2,2))
	print(grid_traveller(2,3))
	print(grid_traveller(3,2))
	print(grid_traveller(3,3))

	row = 2
	col = 3
	memo = [[(None) for j in range(col)] for i in range(row)]
	# print(memo)
	print("Row:",row,"Col:",col,"Output:",grid_traveller_memo(row,col))

	row = 3
	col = 3
	memo = [[(None) for j in range(col)] for i in range(row)]
	print("Row:",row,"Col:",col,"Output:",grid_traveller_memo(row,col))

	row = 18
	col = 18
	memo = [[(None) for j in range(col)] for i in range(row)]
	print("Row:",row,"Col:",col,"Output:",grid_traveller_memo(row,col))


	row = 2
	col = 3
	memo = [[(None) for j in range(col)] for i in range(row)]
	print("Tabular Way - Row:",row,"Col:",col,"Output:",grid_traveller_tabular(row,col))

	row = 3
	col = 3
	memo = [[(None) for j in range(col)] for i in range(row)]
	print("Tabular Way - Row:",row,"Col:",col,"Output:",grid_traveller_tabular(row,col))

	row = 18
	col = 18
	memo = [[(None) for j in range(col)] for i in range(row)]
	print("Tabular Way - Row:",row,"Col:",col,"Output:",grid_traveller_tabular(row,col))


# (base) coding % python gridTraveller.py
# 1
# 2
# 3
# 3
# 6
# Row: 2 Col: 3 Output: 3
# Row: 3 Col: 3 Output: 6
# Row: 18 Col: 18 Output: 2333606220
# Tabular Way - Row: 2 Col: 3 Output: 3
# Tabular Way - Row: 3 Col: 3 Output: 6
# Tabular Way - Row: 18 Col: 18 Output: 2333606220