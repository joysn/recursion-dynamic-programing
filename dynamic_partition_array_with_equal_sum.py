# https://www.youtube.com/watch?v=BFKbbE9Tpqs 8:55
# Paritioning/divide array such that left and right sums are same
# order can vary
# [3,1,2] -> True 
# [1,3,2] -> True ([3 | 1,2])
# [2, 3, 2] -> False

def canPartition(iplist):
	#print(iplist)
	if len(iplist) == 0:
		return True
	if len(iplist) == 1:
		return False
	if len(iplist) == 2:
		if iplist[0] == iplist[1]:
			return True
		else:
			return False
	
	op = False
	if iplist[0] == iplist[1]:
		op = op or canPartition(iplist[2:])
	if (iplist[0]+iplist[1] == iplist[2]) or (iplist[0]+iplist[2] == iplist[1]) or (iplist[1]+iplist[2] == iplist[0]):
		op = op or canPartition(iplist[3:])

	op = op or canPartition([iplist[0]+iplist[1]]+[iplist[2]]+iplist[3:])
	op = op or canPartition([iplist[0]]+[iplist[1]+iplist[2]]+iplist[3:])
	op = op or canPartition([iplist[1]]+[iplist[0]+iplist[2]]+iplist[3:])
	
	return op
	
print("##################################")
print("####### Recursive Approach #######")
print("##################################")
print("[3,1,2] True",canPartition([3,1,2]))	
print("[1,3,2] True",canPartition([1,3,2]))	
print("[2,3,2] False",canPartition([2,3,2]))	
print("[2,3,1,2] True",canPartition([2,3,1,2]))	
print("[2,3,1,2,1] False",canPartition([2,3,1,2,1]))
print("[2,6,1,2,1] True",canPartition([2,6,1,2,1]))




def canPartition(iplist):

	l = len(iplist)
	if l == 0:
		return True
	if l == 1:
		return False
	if l == 2:
		if iplist[0] == iplist[1]:
			return True
		else:
			return False
			
	sum = 0
	for i in range(l):
		sum += iplist[i]
	
	if sum % 2 != 0:
		return False
	
	sum_to_look_for = int(sum / 2)
	
	cache = [[0 for c in range(l)] for r in range(l)]
	
	for c in range(l):
		cache[0][c] = iplist[c]
		if cache[0][c] == sum_to_look_for:
				return True
		
	for r in range(1,l):
		for c in range(r,l):
			cache[r][c] = cache[r-1][c-1]+iplist[c]
			if cache[r][c] == sum_to_look_for:
				return True
	
	#print(sum_to_look_for)
	#print(cache)
	return False
	
	
print("###########################")
print("####### DP Approach #######")
print("###########################")
print("[3,1,2] True",canPartition([3,1,2]))	
print("[1,3,2] True",canPartition([1,3,2]))	
print("[2,3,2] False",canPartition([2,3,2]))	
print("[2,3,1,2] True",canPartition([2,3,1,2]))	
print("[2,3,1,2,1] False",canPartition([2,3,1,2,1]))
print("[2,6,1,2,1] True",canPartition([2,6,1,2,1]))
	
	
# (base) D:\>python dynamic_partition_array_with_equal_sum.py
# ##################################
# ####### Recursive Approach #######
# ##################################
# [3,1,2] True True
# [1,3,2] True True
# [2,3,2] False False
# [2,3,1,2] True True
# [2,3,1,2,1] False False
# [2,6,1,2,1] True True