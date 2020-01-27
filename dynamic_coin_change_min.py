# coin change problem.
# find the min # of coins required to provide the change
# example - [1,2,5,10,20,50], S = 65
# output - 3 (50+10+5)

import copy


def min_coin_change(s):
	if s == 0:
		return 0,None
	if s in coins:
		return 1,s
		
	coins.sort()
	
	min_coin = 100000000000000000
	for coin in coins:
		c_list = []
		if coin < s:
			c_list.append(coin)
			cnt1,c = min_coin_change(s-coin)
			cnt = cnt1 + 1
			if isinstance(c, int):
				c_list.append(c)
			else:
				for e in c:
					c_list.append(e)
		if cnt < min_coin:
			min_coin = cnt
			min_coin_list = copy.deepcopy(c_list)
			
	return min_coin,min_coin_list


coins = [1,2,5,10,20,50]
print("###########################")
print("##### Using Recusrion #####")
print("###########################")
for i in range(21):
	min_coin_list = []	
	num, c = min_coin_change(i)
	print("Min coin required for ",i," is ",num, " having coins ",c)
	
	
def min_coin_change(s):
	if s == 0:
		return 0,None
		
	if s in coins:
		return 1,s
		
	cache = [0 for i in range(s+1)]
	for i in range(s+1):
		cache[i] = 0,[]
	
	for c in coins:
		if c < len(cache):
			cache[c] = 1,[c]
	
	for i in range(1,s+1):
		if cache[i][0] != 1:
			min_cnt = 100000000000000000
			min_cnt_list = []
			for c in coins:
				clist = []
				if i-c > 0:
					cnt,clist = copy.deepcopy(cache[i-c])
					if min_cnt > cnt + 1:
						min_cnt = cnt + 1
						clist += [c]
						min_cnt_list = copy.deepcopy(clist)

						
			temp_list = copy.deepcopy(min_cnt_list)
			cache[i] = min_cnt,temp_list
			
		
	return cache[s]
		
	
coins = [1,2,5,10,20,50]
print("####################")
print("##### Using DP #####")
print("####################")
for i in range(66):
	# min_coin_list = []	
	num, c = min_coin_change(i)
	print("Min coin required for ",i," is ",num, " having coins ",c)
	
	

# (base) D:\>python dynamic_min_coin_change.py
# ###########################
# ##### Using Recusrion #####
# ###########################
# Min coin required for  0  is  0  having coins  None
# Min coin required for  1  is  1  having coins  1
# Min coin required for  2  is  1  having coins  2
# Min coin required for  3  is  2  having coins  [1, 2]
# Min coin required for  4  is  2  having coins  [2, 2]
# Min coin required for  5  is  1  having coins  5
# Min coin required for  6  is  2  having coins  [1, 5]
# Min coin required for  7  is  2  having coins  [2, 5]
# Min coin required for  8  is  3  having coins  [1, 2, 5]
# Min coin required for  9  is  3  having coins  [2, 2, 5]
# Min coin required for  10  is  1  having coins  10
# Min coin required for  11  is  2  having coins  [1, 10]
# Min coin required for  12  is  2  having coins  [2, 10]
# Min coin required for  13  is  3  having coins  [1, 2, 10]
# Min coin required for  14  is  3  having coins  [2, 2, 10]
# Min coin required for  15  is  2  having coins  [5, 10]
# Min coin required for  16  is  3  having coins  [1, 5, 10]
# Min coin required for  17  is  3  having coins  [2, 5, 10]
# Min coin required for  18  is  4  having coins  [1, 2, 5, 10]
# Min coin required for  19  is  4  having coins  [2, 2, 5, 10]
# Min coin required for  20  is  1  having coins  20
# ####################
# ##### Using DP #####
# ####################
# Min coin required for  0  is  0  having coins  None
# Min coin required for  1  is  1  having coins  1
# Min coin required for  2  is  1  having coins  2
# Min coin required for  3  is  2  having coins  [2, 1]
# Min coin required for  4  is  2  having coins  [2, 2]
# Min coin required for  5  is  1  having coins  5
# Min coin required for  6  is  2  having coins  [5, 1]
# Min coin required for  7  is  2  having coins  [5, 2]
# Min coin required for  8  is  3  having coins  [5, 2, 1]
# Min coin required for  9  is  3  having coins  [5, 2, 2]
# Min coin required for  10  is  1  having coins  10
# Min coin required for  11  is  2  having coins  [10, 1]
# Min coin required for  12  is  2  having coins  [10, 2]
# Min coin required for  13  is  3  having coins  [10, 2, 1]
# Min coin required for  14  is  3  having coins  [10, 2, 2]
# Min coin required for  15  is  2  having coins  [10, 5]
# Min coin required for  16  is  3  having coins  [10, 5, 1]
# Min coin required for  17  is  3  having coins  [10, 5, 2]
# Min coin required for  18  is  4  having coins  [10, 5, 2, 1]
# Min coin required for  19  is  4  having coins  [10, 5, 2, 2]
# Min coin required for  20  is  1  having coins  20
# Min coin required for  21  is  2  having coins  [20, 1]
# Min coin required for  22  is  2  having coins  [20, 2]
# Min coin required for  23  is  3  having coins  [20, 2, 1]
# Min coin required for  24  is  3  having coins  [20, 2, 2]
# Min coin required for  25  is  2  having coins  [20, 5]
# Min coin required for  26  is  3  having coins  [20, 5, 1]
# Min coin required for  27  is  3  having coins  [20, 5, 2]
# Min coin required for  28  is  4  having coins  [20, 5, 2, 1]
# Min coin required for  29  is  4  having coins  [20, 5, 2, 2]
# Min coin required for  30  is  2  having coins  [20, 10]
# Min coin required for  31  is  3  having coins  [20, 10, 1]
# Min coin required for  32  is  3  having coins  [20, 10, 2]
# Min coin required for  33  is  4  having coins  [20, 10, 2, 1]
# Min coin required for  34  is  4  having coins  [20, 10, 2, 2]
# Min coin required for  35  is  3  having coins  [20, 10, 5]
# Min coin required for  36  is  4  having coins  [20, 10, 5, 1]
# Min coin required for  37  is  4  having coins  [20, 10, 5, 2]
# Min coin required for  38  is  5  having coins  [20, 10, 5, 2, 1]
# Min coin required for  39  is  5  having coins  [20, 10, 5, 2, 2]
# Min coin required for  40  is  2  having coins  [20, 20]
# Min coin required for  41  is  3  having coins  [20, 20, 1]
# Min coin required for  42  is  3  having coins  [20, 20, 2]
# Min coin required for  43  is  4  having coins  [20, 20, 2, 1]
# Min coin required for  44  is  4  having coins  [20, 20, 2, 2]
# Min coin required for  45  is  3  having coins  [20, 20, 5]
# Min coin required for  46  is  4  having coins  [20, 20, 5, 1]
# Min coin required for  47  is  4  having coins  [20, 20, 5, 2]
# Min coin required for  48  is  5  having coins  [20, 20, 5, 2, 1]
# Min coin required for  49  is  5  having coins  [20, 20, 5, 2, 2]
# Min coin required for  50  is  1  having coins  50
# Min coin required for  51  is  2  having coins  [50, 1]
# Min coin required for  52  is  2  having coins  [50, 2]
# Min coin required for  53  is  3  having coins  [50, 2, 1]
# Min coin required for  54  is  3  having coins  [50, 2, 2]
# Min coin required for  55  is  2  having coins  [50, 5]
# Min coin required for  56  is  3  having coins  [50, 5, 1]
# Min coin required for  57  is  3  having coins  [50, 5, 2]
# Min coin required for  58  is  4  having coins  [50, 5, 2, 1]
# Min coin required for  59  is  4  having coins  [50, 5, 2, 2]
# Min coin required for  60  is  2  having coins  [50, 10]
# Min coin required for  61  is  3  having coins  [50, 10, 1]
# Min coin required for  62  is  3  having coins  [50, 10, 2]
# Min coin required for  63  is  4  having coins  [50, 10, 2, 1]
# Min coin required for  64  is  4  having coins  [50, 10, 2, 2]
# Min coin required for  65  is  3  having coins  [50, 10, 5]
	

