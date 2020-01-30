# knapsack problem in W[n], int V[n]
# Unlimited # of each items

def knapsack(c):
	if c == 0:
		return 0
		
	max_value = 0
	for i in range(len(W)):
		temp_value = 0
		if c-W[i] >= 0:
			temp_value = V[i] + knapsack(c-W[i])
		if temp_value > max_value:
			max_value = temp_value
			
	return max_value

W = [2,3,4,5]
V = [3,4,5,6]

print("#############################")
print("###### Using Recursion ######")
print("#############################")
for i in range(11):
	print("Capacity:",i," Value: ",knapsack(i))


def knapsack(capacity):
	if capacity == 0:
		return 0
		
	cache = [0 for i in range(capacity+1)]
	for i in range(len(cache)):
		cache[i] = 0,[]
		
	for cap in range(1,capacity+1):
		for i in range(len(Weights)):
			if cap-Weights[i] >= 0:
				v1,l1 = cache[cap]
				v2,l2 = cache[cap-Weights[i]]
				if v1 < v2+Values[i]:
					#print(cap,i,Weights[i],Values[i],cache[cap],cache[cap-Weights[i]])
					v_curr = v2 + Values[i]
					l_curr = l2 + [(Weights[i],Values[i])]
					#cache[cap] = cache[cap-Weights[i]]+Values[i]
					cache[cap] = v_curr,l_curr
			#print(cache)
				
	return cache[capacity]
	
Weights = [2,3,4,5]
Values = [3,4,5,6]

print("######################")
print("###### Using DP ######")
print("######################")
for i in range(11):
	print("Capacity:",i," Value: ",knapsack(i))
	
	
# (base) D:\>python dynamic_knapsack_unlimited.py
# #############################
# ###### Using Recursion ######
# #############################
# Capacity: 0  Value:  0
# Capacity: 1  Value:  0
# Capacity: 2  Value:  3
# Capacity: 3  Value:  4
# Capacity: 4  Value:  6
# Capacity: 5  Value:  7
# Capacity: 6  Value:  9
# Capacity: 7  Value:  10
# Capacity: 8  Value:  12
# Capacity: 9  Value:  13
# Capacity: 10  Value:  15
# ######################
# ###### Using DP ######
# ######################
# Capacity: 0  Value:  0
# Capacity: 1  Value:  (0, [])
# Capacity: 2  Value:  (3, [(2, 3)])
# Capacity: 3  Value:  (4, [(3, 4)])
# Capacity: 4  Value:  (6, [(2, 3), (2, 3)])
# Capacity: 5  Value:  (7, [(3, 4), (2, 3)])
# Capacity: 6  Value:  (9, [(2, 3), (2, 3), (2, 3)])
# Capacity: 7  Value:  (10, [(3, 4), (2, 3), (2, 3)])
# Capacity: 8  Value:  (12, [(2, 3), (2, 3), (2, 3), (2, 3)])
# Capacity: 9  Value:  (13, [(3, 4), (2, 3), (2, 3), (2, 3)])
# Capacity: 10  Value:  (15, [(2, 3), (2, 3), (2, 3), (2, 3), (2, 3)])






















	

