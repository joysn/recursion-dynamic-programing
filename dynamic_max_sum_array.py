# Given an array of integers write a function that returns the max sum of sub array such that the elements are contiguos

# i/p array = [-1,-3, 4, -1, -2, 1, 5, -3]
# o/p = 7 => 4-1-2+1+5

def max_sum(): #O (n^2)
	
	sum = [[0 for i in range(0,len(arr))] for j in range(0,len(arr))]
	#print(sum)
	msum = arr[0]
	for i in range(0,len(arr)):
		sum[0][i] = arr[i]
		if msum < arr[i]:
			msum = arr[i]
	for r in range(1, len(arr)):
		for c in range(r,len(arr)):
			sum[r][c] = sum[r][c-1] + arr[c]
			if sum[r][c] > msum:
				msum = sum[r][c]
	return msum
	


arr = [-1,-3]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4,-1]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4,-1,-2]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4,-1,-2,1]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4,-1,-2,4]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4,-1,-2,1,5]
print("Max sum of ",arr," is: ",max_sum())
arr = [-1,-3, 4, -1, -2, 1, 5, -3]
print("Max sum of ",arr," is: ",max_sum())

