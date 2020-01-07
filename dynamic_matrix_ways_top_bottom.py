# Unique ways to move from top left to bottom right

def no_of_ways(row,col):
	dr = row 
	dc = col 
	
	if dr == 0 or dc == 0:
		return 1
		
	ways = no_of_ways(dr - 1, dc) + no_of_ways(dr, dc - 1)
		
	return ways
	
	
	
	
print("########################")
print("## Recursive Solution ##")
print("########################")
print("No of ways to reach to (0,0):",no_of_ways(0,0))
print("No of ways to reach to (1,1):",no_of_ways(1,1))
print("No of ways to reach to (1,2):",no_of_ways(1,2))
print("No of ways to reach to (2,2):",no_of_ways(2,2))



def no_of_ways(row,col):
	ways = [[0 for i in range(col+1)] for j in range(row+1)]
	
	for c in range(col+1):
		ways[0][c] = 1
		
	for r in range(row+1):
		ways[r][0] = 1
		
	for r in range(1,row+1):
		for c in range(1,col+1):
			ways[r][c] = ways[r-1][c] + ways[r][c-1] 
			
	return ways[row][col]


print("#################")
print("## DP Solution ##")
print("#################")
print("No of ways to reach to (0,0):",no_of_ways(0,0))
print("No of ways to reach to (1,1):",no_of_ways(1,1))
print("No of ways to reach to (1,2):",no_of_ways(1,2))
print("No of ways to reach to (2,2):",no_of_ways(2,2))



# (base) D:\>python dynamic_matrix_ways_top_bottom.py
# ########################
# ## Recursive Solution ##
# ########################
# No of ways to reach to (0,0): 1
# No of ways to reach to (1,1): 2
# No of ways to reach to (1,2): 3
# No of ways to reach to (2,2): 6
# #################
# ## DP Solution ##
# #################
# No of ways to reach to (0,0): 1
# No of ways to reach to (1,1): 2
# No of ways to reach to (1,2): 3
# No of ways to reach to (2,2): 6