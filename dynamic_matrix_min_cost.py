# Find the min cost to reach 2,3
# input = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]

####################################
####### METHODICAL APPROACH ########
####################################

def min_cost_part(dr,dc):
	r = 0
	c = 0
	if dr > dc:
		max_iter = dr
	else:
		max_iter = dc
	min_cost = input[r][c] 
	while r != dr and c != dc:
		m1 = 100000000000000000000
		m2 = 100000000000000000000
		if r+1 <= dr:
			m1 = input[r+1][c]
		if c+1 <= dc:
			m2 = input[r][c+1]
		if m1 < m2:
			r = r + 1
			min_cost += m1
		else:
			c = c + 1
			min_cost += m2
	min_cost += input[dr][dc]
	return min_cost

print("####### METHODICAL APPROACH ########")	
input = [[1, 4],\
         [2, 6]]
print("Should be 9:",min_cost_part(1,1))
input = [[1, 4, 3],\
         [2, 6, 9],\
		 [8, 5, 2]]
print("Should be 16:",min_cost_part(2,2))
# input = [[1, 4, 3,0],[2, 6, 9, 8],[8, 5, 2, 4],[6,10,14,3]]
input = [[1,3,5,8],\
         [4,2,1,7],\
		 [4,3,2,3]]
print("Should be 12:",min_cost_part(2,3))


###########################
######## RECURSION ########
###########################
def min_cost_part(dr,dc):

	if (dr == 0) and (dc == 0):
		return input[dr][dc]
	if dr == 0:
		return min_cost_part(dr,dc-1) + input[dr][dc]
	if dc == 0:
		return min_cost_part(dr-1,dc) + input[dr][dc]
		
	m1 = min_cost_part(dr-1,dc) + input[dr][dc]
	m2 = min_cost_part(dr,dc-1) + input[dr][dc]
	if m1 < m2:
		return m1
	else:
		return m2
		
print("######## RECURSION ########")
input = [[1, 4],\
         [2, 6]]
print("Should be 9:",min_cost_part(1,1))
input = [[1, 4, 3],\
         [2, 6, 9],\
		 [8, 5, 2]]
print("Should be 16:",min_cost_part(2,2))
# input = [[1, 4, 3,0],[2, 6, 9, 8],[8, 5, 2, 4],[6,10,14,3]]
input = [[1,3,5,8],\
         [4,2,1,7],\
		 [4,3,2,3]]
print("Should be 12:",min_cost_part(2,3))


#############################
######## MEMOIZATION ########
#############################
def min_cost_part(dr,dc):

	if cache[dr][dc] is not None:
		return cache[dr][dc]
	if (dr == 0) and (dc == 0):
		cache[dr][dc] = input[dr][dc]
	elif dr == 0:
		cache[dr][dc] = min_cost_part(dr,dc-1) + input[dr][dc]
	elif dc == 0:
		cache[dr][dc] = min_cost_part(dr-1,dc) + input[dr][dc]
	else:	
		m1 = min_cost_part(dr-1,dc) + input[dr][dc]
		m2 = min_cost_part(dr,dc-1) + input[dr][dc]
		if m1 < m2:
			cache[dr][dc] = m1
		else:
			cache[dr][dc] = m2
			
	return cache[dr][dc]
		
print("######## MEMOIZATION ########")		
input = [[1, 4],\
         [2, 6]]

cache = list()
for r in range(len(input)):
	row = list()
	for c in range(len(input[0])):
		row.append(None)
	cache.append(row)
print("Should be 9:",min_cost_part(1,1))

input = [[1, 4, 3],\
         [2, 6, 9],\
		 [8, 5, 2]]
cache = list()
for r in range(len(input)):
	row = list()
	for c in range(len(input[0])):
		row.append(None)
	cache.append(row)
print("Should be 16:",min_cost_part(2,2))
# # input = [[1, 4, 3,0],[2, 6, 9, 8],[8, 5, 2, 4],[6,10,14,3]]
input = [[1,3,5,8],\
         [4,2,1,7],\
		 [4,3,2,3]]
cache = list()
for r in range(len(input)):
	row = list()
	for c in range(len(input[0])):
		row.append(None)
	cache.append(row)
print("Should be 12:",min_cost_part(2,3))





##############################
######## BOTTOM UP DP ########
##############################
def min_cost_part(dr,dc):

	if (dr == 0) and (dc == 0):
		cost[dr][dc] = input[dr][dc]
	
	for c in range(1,dc+1):
		cost[0][c] = input[0][c-1]+ input[0][c]
	for r in range(1,dr+1):
		cost[r][0] = input[r-1][0]+ input[r][0]
	
	for r in range(1,dr+1):
		for c in range(1,dc+1):
			if cost[r-1][c] < cost[r][c-1]:
				cost[r][c] = cost[r-1][c] + input[r][c]
			else:
				cost[r][c] = cost[r][c-1] + input[r][c]
			
	return cost[dr][dc]
		
print("######## BOTTOM UP DP ########")		
input = [[1, 4],\
         [2, 6]]

cost = list()
for r in range(len(input)):
	row = list()
	for c in range(len(input[0])):
		row.append(None)
	cost.append(row)
print("Should be 9:",min_cost_part(1,1))

input = [[1, 4, 3],\
         [2, 6, 9],\
		 [8, 5, 2]]
cost = list()
for r in range(len(input)):
	row = list()
	for c in range(len(input[0])):
		row.append(None)
	cost.append(row)
print("Should be 16:",min_cost_part(2,2))
# # input = [[1, 4, 3,0],[2, 6, 9, 8],[8, 5, 2, 4],[6,10,14,3]]
input = [[1,3,5,8],\
         [4,2,1,7],\
		 [4,3,2,3]]
cost = list()
for r in range(len(input)):
	row = list()
	for c in range(len(input[0])):
		row.append(None)
	cost.append(row)
print("Should be 12:",min_cost_part(2,3))
	