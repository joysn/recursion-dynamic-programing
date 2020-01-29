# Given a rod of certain length and price of different size rods, how should the rod be cut to maximize the income

import copy

def cut_rod(size):
	if size == 0:
		return price_list[size],[]
		
	if size == 1:
		return price_list[size],[size]
		
	max_price = 0
	op_list = []
	for s in range(1,len(price_list)):
		if size-s >= 0:
			p1,s1 = cut_rod(size-s)
			price = price_list[s] + p1
			cut_list = [s] + s1
			if price > max_price:
				max_price = price
				op_list = copy.deepcopy(cut_list)
				
	return max_price,op_list
		
#             0 1 2 3 4  5  6  7  8
price_list = [0,1,5,8,9,10,17,17,20]

print("###########################")
print("##### Using Recursion #####")
print("###########################")
for i in range(10):
	print("Max cut and profit from rod of size ",i," is ",cut_rod(i))
	

def cut_rod(size):
	if size == 0:
		return price_list[size],[]
		
	if size == 1:
		return price_list[size],[size]
		
		
	cache = [0 for i in range(size+1)]
	for i in range(size+1):
		cache[i] = 0,[]
		
	cache[1] = price_list[1],[1]
	
	
	for s in range(2,size+1):
		max_price = 0
		op_list = []
		for p in range(1,len(price_list)):
			temp_price = 0
			temp_size = []
			if s-p >= 0:
				p1,s1 = cache[s-p]
				temp_price = p1 + price_list[p]
				temp_size = [p] + s1
				if temp_price > max_price:
					max_price = temp_price
					op_list = copy.deepcopy(temp_size)
				#print(s,p,temp_price,temp_size,max_price,op_list)
		cache[s] = max_price,op_list
		
	return cache[s]
	
	
print("####################")
print("##### Using DP #####")
print("####################")
for i in range(10):
	print("Max cut and profit from rod of size ",i," is ",cut_rod(i))
	
	
# (base) D:\>python dynamic_rod_cut_max.py
# ###########################
# ##### Using Recursion #####
# ###########################
# Max cut and profit from rod of size  0  is  (0, [])
# Max cut and profit from rod of size  1  is  (1, [1])
# Max cut and profit from rod of size  2  is  (5, [2])
# Max cut and profit from rod of size  3  is  (8, [3])
# Max cut and profit from rod of size  4  is  (10, [2, 2])
# Max cut and profit from rod of size  5  is  (13, [2, 3])
# Max cut and profit from rod of size  6  is  (17, [6])
# Max cut and profit from rod of size  7  is  (18, [1, 6])
# Max cut and profit from rod of size  8  is  (22, [2, 6])
# Max cut and profit from rod of size  9  is  (25, [3, 6])
# ####################
# ##### Using DP #####
# ####################
# Max cut and profit from rod of size  0  is  (0, [])
# Max cut and profit from rod of size  1  is  (1, [1])
# Max cut and profit from rod of size  2  is  (5, [2])
# Max cut and profit from rod of size  3  is  (8, [3])
# Max cut and profit from rod of size  4  is  (10, [2, 2])
# Max cut and profit from rod of size  5  is  (13, [2, 3])
# Max cut and profit from rod of size  6  is  (17, [6])
# Max cut and profit from rod of size  7  is  (18, [1, 6])
# Max cut and profit from rod of size  8  is  (22, [2, 6])
# Max cut and profit from rod of size  9  is  (25, [3, 6])