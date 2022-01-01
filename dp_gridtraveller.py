
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