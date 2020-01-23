# A sequence is bitonic if it is first monotonically increases and then monotonically decreses
# e.g - (1,4,6,8,3,-2), (9,2,-4,-10,-15), and (1,2,3,4) are Bitonic
# (1,3,12,4,2,10) is not bitonic

def is_bitonic(s1): # O(n), O(1)
	if len(s1) == 0:
		return False
	if len(s1) == 1:
		return True
		
	#cache = [0 for i in range(len(s1))]
	curr_cnt = 0
	
	
	curr_sequence = 0
	
	if s1[1] >= s1[0]:
		curr_sequence = 1
		curr_cnt = 1
	else:
		curr_sequence = 2
		curr_cnt = 1
		
	for c in range(2,len(s1)):
		# if s1[c] >= s1[c-1] and curr_sequence == 1:
			# curr_cnt = curr_cnt
		# elif s1[c] < s1[c-1] and curr_sequence == 2:
			# curr_cnt = curr_cnt
		#elif s1[c] >= s1[c-1] and curr_sequence == 2:
		if s1[c] >= s1[c-1] and curr_sequence == 2:
			curr_cnt = 1 + curr_cnt
			curr_sequence = 1
		elif s1[c] < s1[c-1] and curr_sequence == 1:
			curr_cnt = 1 + curr_cnt
			curr_sequence = 2
			
		if curr_cnt > 2:
			return False
			
	return True

print("######################")
print("###### Using DP ######")
print("######################")
print("[1,4,6,8,3,-2] is bitonic?",is_bitonic([1,4,6,8,3,-2]))
print("[9,2,-4,-10,-15] is bitonic?",is_bitonic([9,2,-4,-10,-15]))
print("[1,2,3,4] is bitonic?",is_bitonic([1,2,3,4]))
print("[1,3,12,4,2,10] is bitonic?",is_bitonic([1,3,12,4,2,10]))
print("[1,10,4,9,2,-1,100] is bitonic?",is_bitonic([1,10,4,9,2,-1,100]))


# (base) D:\>python dynamic_bitonic_sequence.py
# ######################
# ###### Using DP ######
# ######################
# [1,4,6,8,3,-2] is bitonic? True
# [9,2,-4,-10,-15] is bitonic? True
# [1,2,3,4] is bitonic? True
# [1,3,12,4,2,10] is bitonic? False
# [1,10,4,9,2,-1,100] is bitonic? False
