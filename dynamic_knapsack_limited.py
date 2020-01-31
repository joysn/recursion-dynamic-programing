# knapsack problem in Weights[n], int Values[n]
# Only given # of each items

def knapsack(capacity,idxw):
	if capacity == 0:
		return 0
		
	max_value = 0
	for i in range(idxw,len(Weights)):
		if capacity-Weights[i] >= 0:
			temp_value = Values[i] + knapsack(capacity-Weights[i],i+1)
			if temp_value > max_value:
				max_value = temp_value
			
	return max_value
		
		
Weights = [2,3,4,5]
Values = [3,4,5,6]

print("#############################")
print("###### Using Recursion ######")
print("#############################")
for i in range(11):
	print("Capacity:",i," Value: ",knapsack(i,0))
	
	
import copy

def knapsack(capacity):
	if capacity == 0:
		return 0
	
	cache = [[0 for i in range(capacity+1)] for j in range(len(Weights)+1)]
	
	for r in range(len(Weights)+1):
		for c in range(capacity+1):
			cache[r][c] = 0,[]
	#print(cache)

	for it in range(1,len(Weights)+1):
		for cp in range(1,capacity+1):
			if cp - Weights[it-1] >= 0:
				v1,l1 = cache[it-1][cp]
				v2,l2 = cache[it-1][cp-Weights[it-1]]
				if v1 > Values[it-1]+v2:
					cache[it][cp] = copy.deepcopy(cache[it-1][cp])
				else:
					v3 = Values[it-1]+v2
					l3 = l2 + [(Weights[it-1],Values[it-1])]
					cache[it][cp] = v3,l3
				#cache[it][cp] = max(cache[it-1][cp], Values[it-1]+cache[it-1][cp-Weights[it-1]])
			else:
				cache[it][cp] = copy.deepcopy(cache[it-1][cp])
				
	#print(cache)
	return cache[len(Weights)][capacity]
			
print("######################")
print("###### Using DP ######")
print("######################")
for i in range(11):
	print("Capacity:",i," Value: ",knapsack(i))	
	
	
# (base) D:\>python dynamic_knapsack_limited.py
# #############################
# ###### Using Recursion ######
# #############################
# Capacity: 0  Value:  0
# Capacity: 1  Value:  0
# Capacity: 2  Value:  3
# Capacity: 3  Value:  4
# Capacity: 4  Value:  5
# Capacity: 5  Value:  7
# Capacity: 6  Value:  8
# Capacity: 7  Value:  9
# Capacity: 8  Value:  10
# Capacity: 9  Value:  12
# Capacity: 10  Value:  13
# ######################
# ###### Using DP ######
# ######################
# Capacity: 0  Value:  0
# Capacity: 1  Value:  (0, [])
# Capacity: 2  Value:  (3, [(2, 3)])
# Capacity: 3  Value:  (4, [(3, 4)])
# Capacity: 4  Value:  (5, [(4, 5)])
# Capacity: 5  Value:  (7, [(2, 3), (3, 4)])
# Capacity: 6  Value:  (8, [(2, 3), (4, 5)])
# Capacity: 7  Value:  (9, [(2, 3), (5, 6)])
# Capacity: 8  Value:  (10, [(3, 4), (5, 6)])
# Capacity: 9  Value:  (12, [(2, 3), (3, 4), (4, 5)])
# Capacity: 10  Value:  (13, [(2, 3), (3, 4), (5, 6)])

