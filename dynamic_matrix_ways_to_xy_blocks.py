#####################
### Variation - 2 ###
#####################
# Given a matrix, find no of ways to reach from 0,0 to x,y with blocks


def no_of_ways(sr,sc,dr,dc):
	
	# Origin and destination same
	if sr == dr and sc == dc:
		return 1

	# block at (0,1)
	if sr == 0 and sc == 1:
		return 0
		
	# source and destination in same row or same column
	if sr == dr or sc == dc:
		return 1
		
	ways = 0
	if dr > sr:
		ways += no_of_ways(sr+1,sc,dr,dc)
	if dc > sc:
		ways += no_of_ways(sr,sc+1,dr,dc)
	
	return ways
	
def no_of_ways_helper(dr,dc):
	return(no_of_ways(0,0,dr,dc))

print("########################")
print("## Recursive Solution ##")
print("########################")
print("Ways to go from 0,0 to 0,0",no_of_ways_helper(0,0))
print("Ways to go from 0,0 to 1,1",no_of_ways_helper(1,1))
print("Ways to go from 0,0 to 1,2",no_of_ways_helper(1,2))
print("Ways to go from 0,0 to 2,2",no_of_ways_helper(2,2))


def no_of_ways(dr,dc):
	ways = [[0 for i in range(dc+1)] for j in range(dr+1)]
	
	# Blocked node
	blocked_r = 0
	blocked_c = 1
	
	if (blocked_c != 0) or (blocked_r != 0):
		ways[0][0] = 1
		
	for c in range(1,dc+1):
		ways[0][c] = ways[0][c-1]
		if blocked_r == 0 and blocked_c == c:
			ways[0][c] = 0
		
	for r in range(1,dr+1):
		ways[r][0] = ways[r-1][0]
		if blocked_r == r and blocked_c == 0:
			ways[r][0] = 0
	
	
	for r in range(1,dr+1):
		for c in range(1,dc+1):
			ways[r][c] = ways[r-1][c] + ways[r][c-1]
			if blocked_r == r and blocked_c == c:
				ways[r][c] = 0
				
	#print(ways)
	return ways[dr][dc]
	
print("#################")
print("## DP Solution ##")
print("#################")
print("Ways to go from 0,0 to 0,0",no_of_ways(0,0))
print("Ways to go from 0,0 to 1,1",no_of_ways(1,1))
print("Ways to go from 0,0 to 1,2",no_of_ways(1,2))
print("Ways to go from 0,0 to 2,2",no_of_ways(2,2))



#####################
### Variation - 3 ###
#####################

## Diagonals also allowed
##########################
def no_of_ways(dr,dc):
	ways = [[0 for i in range(dc+1)] for j in range(dr+1)]
	
	# Blocked node details
	blocked_c = 1
	blocked_r = 0
	
	if blocked_c != 0 or blocked_r != 0:
		ways[0][0] = 1
		
	for c in range(1,dc+1):
		ways[0][c] = ways[0][c-1]
		if blocked_r == 0 and blocked_c == c:
			ways[0][c] = 0
			
	for r in range(1,dr+1):
		ways[r][0] = ways[r-1][0]
		if blocked_r == r and blocked_c == 0:
			ways[r][0] = 0
	
	
	for r in range(1,dr+1):
		for c in range(1,dc+1):
			# diagonals also included
			ways[r][c] = ways[r-1][c] + ways[r][c-1] + ways[r-1][c-1]
			if blocked_r == r and blocked_c == c:
				ways[r][c] = 0
	
	return ways[dr][dc]
	
print("#################")
print("## DP Solution ##")
print("#################")
print("Ways to go from 0,0 to 0,0",no_of_ways(0,0))
print("Ways to go from 0,0 to 1,1",no_of_ways(1,1))
print("Ways to go from 0,0 to 1,2",no_of_ways(1,2))
print("Ways to go from 0,0 to 2,2",no_of_ways(2,2))


# (base) D:\>python dynamic_matrix_ways_to_xy_blocks.py
# ########################
# ## Recursive Solution ##
# ########################
# Ways to go from 0,0 to 0,0 1
# Ways to go from 0,0 to 1,1 1
# Ways to go from 0,0 to 1,2 1
# Ways to go from 0,0 to 2,2 3
# #################
# ## DP Solution ##
# #################
# Ways to go from 0,0 to 0,0 1
# Ways to go from 0,0 to 1,1 1
# Ways to go from 0,0 to 1,2 1
# Ways to go from 0,0 to 2,2 3
# #################
# ## DP Solution ##
# #################
# Ways to go from 0,0 to 0,0 1
# Ways to go from 0,0 to 1,1 2
# Ways to go from 0,0 to 1,2 2
# Ways to go from 0,0 to 2,2 8
	