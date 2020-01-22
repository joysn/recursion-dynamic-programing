# print longets monotonically incrementing subsequence of an array

import copy
def max_len_print(s1):
	if len(s1) == 0:
		print(0,"No string")
		
	if len(s1) == 1:
		print(1,s1)
		
	curr_l = 0
	max_l = 0
	op = [s1[0]]
	max_op = [s1[0]]
	
	for i in range(1,len(s1)):
		if s1[i] == s1[i-1] +1:
			op.append(s1[i])
			curr_l += 1
			if max_l < curr_l:
				max_l = curr_l
				max_op = copy.deepcopy(op)
		else:
			curr_l = 0
			op = list()
			op.append(s1[i])
			
	return max_l+1,max_op
	
	
debug = True
debug = False
print("####################")
print("##### Using DP #####")
print("####################")
print("[1,2]",max_len_print([1,2]))
print("[1,3]",max_len_print([1,3]))
print("[1,2,4,5]",max_len_print([1,2,4,5]))
print("[1,2,3]",max_len_print([1,2,3]))
print("[1,2,5,4,5,6,7]",max_len_print([1,2,5,4,5,6,7]))
print("[1,2,5,4,-2,-1,0,1,5,6,7]",max_len_print([1,2,5,4,-2,-1,0,1,5,6,7]))