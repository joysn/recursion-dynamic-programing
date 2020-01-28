# find total number of ways we can make change of the amount using the coins of given denominations


coins = [1,2,5,10,20,50]

def coin_change_tot_count(amount,count):
	
	if amount == 0:
		return count
		
	for c in coins:
		if amount - c == 0:
			count += 1
		elif amount-c > 0:
			count = coin_change_tot_count(amount-c,count)
			
	return count
	
	
print('###########################')
print("##### Using recursion #####")
print('###########################')
for i in range(6):
	print("Number of ways coins can be counted",i,coin_change_tot_count(i,0))
	
	
def coin_change_tot_count(amount):
	if amount == 0:
		return 0
		
	cache = [0 for i in range(amount+1)]
	
	for c in coins:
		if c <= amount:
			cache[c] = 1
		
	print(cache) if debug else None
	for a in range(2,amount+1):
		for c in coins:
			print(a,c) if debug else None
			if a-c> 0:
				print("-->",a,c,cache[a],cache[a-c]) if debug else None
				cache[a] = cache[a] + cache[a-c]
				
	return cache[amount]
	
debug = True
debug = False
print('####################')
print("##### Using DP #####")
print('####################')
for i in range(6):
	print("Number of ways coins can be counted",i,coin_change_tot_count(i))
	
	
# (base) D:\>python dynamic_coin_change_tot.py
# ###########################
# ##### Using recursion #####
# ###########################
# Number of ways coins can be counted 0 0
# Number of ways coins can be counted 1 1
# Number of ways coins can be counted 2 2
# Number of ways coins can be counted 3 3
# Number of ways coins can be counted 4 5
# Number of ways coins can be counted 5 9
# ####################
# ##### Using DP #####
# ####################
# Number of ways coins can be counted 0 0
# Number of ways coins can be counted 1 1
# Number of ways coins can be counted 2 2
# Number of ways coins can be counted 3 3
# Number of ways coins can be counted 4 5
# Number of ways coins can be counted 5 9


			