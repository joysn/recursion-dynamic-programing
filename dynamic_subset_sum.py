# given an array of non-negative integers and a postive integer X, determine if there exist a subset of elements
# of array, with sum of X
# Input [3, 2, 7, 1] 6
# Oputput True (because sum(3,2,1) is 6)



def exist_subset(arr,sum,start):
	#print(arr,sum,start)
	if sum == 0:
		return True
		
	if sum < 0:
		return False
		
		
	for i in range(start,len(arr)):
		#print(i)
		sum -= arr[i]
		op = exist_subset(arr,sum,i+1)
		if op == False:
			sum += arr[i]
		
	if sum != 0:
		return False
	else:
		return True
	
print("#####################")
print("## Using Recursion ##")
print("#####################")
for i in range(5):
	print("[1,2] and ",i,":-",exist_subset([1,2],i,0))
for i in range(16):
	print("[3,2,7,1] and ",i,":-",exist_subset([3,2,7,1],i,0))
	

def exist_subset(arr,total):
	
	if total == 0:
		return True
		
	sum = [[False for c in range(total+1)] for j in range(len(arr))]
	sum[0][0] = True
	if arr[0] <= total:
		sum[0][arr[0]] = True
	
	for r in range(len(arr)):
		sum[r][0] = True
	for r in range(1,len(arr)):
		for c in range(total+1):
			#print("(",r,c,arr[r],")")
			if c < arr[r]:
				#print("IF......->",c,r,arr[r],sum[r-1][c])
				sum[r][c] = sum[r-1][c]
			else:
				if sum[r-1][c] != True:
					#print("EL......->",c,r,arr[r],c-arr[r],sum[r-1][c-arr[r]])
					sum[r][c] = sum[r-1][c-arr[r]]
				else:
					sum[r][c] = True
	return sum[len(arr)-1][total]
	
print("##############")
print("## Using DP ##")
print("##############")
for i in range(5):
	print("[1,2] and ",i,":-",exist_subset([1,2],i))
for i in range(16):
	print("[3,2,7,1] and ",i,":-",exist_subset([3,2,7,1],i))
	
	
# (base) D:\>python dynamic_subset_sum.py
# #####################
# ## Using Recursion ##
# #####################
# [1,2] and  0 :- True
# [1,2] and  1 :- True
# [1,2] and  2 :- True
# [1,2] and  3 :- True
# [1,2] and  4 :- False
# [3,2,7,1] and  0 :- True
# [3,2,7,1] and  1 :- True
# [3,2,7,1] and  2 :- True
# [3,2,7,1] and  3 :- True
# [3,2,7,1] and  4 :- True
# [3,2,7,1] and  5 :- True
# [3,2,7,1] and  6 :- True
# [3,2,7,1] and  7 :- True
# [3,2,7,1] and  8 :- True
# [3,2,7,1] and  9 :- True
# [3,2,7,1] and  10 :- True
# [3,2,7,1] and  11 :- True
# [3,2,7,1] and  12 :- True
# [3,2,7,1] and  13 :- True
# [3,2,7,1] and  14 :- False
# [3,2,7,1] and  15 :- False
# ##############
# ## Using DP ##
# ##############
# [1,2] and  1 :- True
# [1,2] and  0 :- True
# [1,2] and  1 :- True
# [1,2] and  2 :- True
# [1,2] and  3 :- True
# [1,2] and  4 :- False
# [3,2,7,1] and  0 :- True
# [3,2,7,1] and  1 :- True
# [3,2,7,1] and  2 :- True
# [3,2,7,1] and  3 :- True
# [3,2,7,1] and  4 :- True
# [3,2,7,1] and  5 :- True
# [3,2,7,1] and  6 :- True
# [3,2,7,1] and  7 :- True
# [3,2,7,1] and  8 :- True
# [3,2,7,1] and  9 :- True
# [3,2,7,1] and  10 :- True
# [3,2,7,1] and  11 :- True
# [3,2,7,1] and  12 :- True
# [3,2,7,1] and  13 :- True
# [3,2,7,1] and  14 :- False
# [3,2,7,1] and  15 :- False
















