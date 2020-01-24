# A sequence is bitonic if it is first monotonically increases and then monotonically decreses
# e.g - (1,4,6,8,3,-2), (9,2,-4,-10,-15), and (1,2,3,4) are Bitonic
# (1,3,12,4,2,10) is not bitonic
# print the longest bitonic sequence

def is_bitonic(s1):
	if len(s1) == 0:
		return False
		
	if len(s1) == 1:
		return True
		
		
	#cache = [0 for i in range(len(s1))]
	curr_cnt = 0
	curr_sequence = 0
	
	if s1[1] >= s1[0]:
		#cache[1] = 1
		curr_cnt = 1
		curr_sequence = 1
	else:
		#cache[1] = 1
		curr_cnt = 1
		curr_sequence = 2
		
	for i in range(2,len(s1)):
		#if s1[i] >= s1[i-1] and curr_sequence == 1:
		#	cache[i] = cache[i-1]
		#elif s1[i] < s1[i-1] and curr_sequence == 2:
		#	cache[i] = cache[i-1]
		#elif s1[i] >= s1[i-1] and curr_sequence == 2:
		if s1[i] >= s1[i-1] and curr_sequence == 2:
			#cache[i] = 1+cache[i-1]
			curr_cnt += 1
			curr_sequence = 1
		elif s1[i] < s1[i-1] and curr_sequence == 1:
			#cache[i] = 1+cache[i-1]
			curr_cnt += 1
			curr_sequence = 2
			
		#if cache[i] > 2:
		if curr_cnt > 2:
			return False
	
	return True
		

def largest_bitonic_seq_print(s1):
	if is_bitonic(s1):
		#print(s1)
		#return is_bitonic(s1)
		return s1
		
	largest_bitonic = s1[0]
	largest_len = 1
	string_len = len(s1)
	
	for i in range(1,len(s1)):
		print(s1[0:i+1],s1[i+1:string_len]) if debug else None
		if (is_bitonic(s1[0:i+1])):
			if largest_len < i+1:
				largest_bitonic = s1[0:i+1]
				largest_len = i+1
			print(i,s1[0:i+1],largest_len) if debug else None
		if (is_bitonic(s1[i+1:string_len])):
			if largest_len < string_len -(i+1):
				largest_bitonic = s1[i+1:string_len]
				largest_len = string_len -(i+1)
			print(i,s1[i+1:string_len],largest_len) if debug else None
	
	return largest_bitonic
	#return is_bitonic(s1)
			
	
		
debug = True
debug = False
print("######################")
print("###### Using DP ######")
print("######################")
print("[1,4,6,8,3,-2] largest bitonic string:-",largest_bitonic_seq_print([1,4,6,8,3,-2]))
print("[9,2,-4,-10,-15] largest bitonic string:-",largest_bitonic_seq_print([9,2,-4,-10,-15]))
print("[1,2,3,4] largest bitonic string:-",largest_bitonic_seq_print([1,2,3,4]))
print("[1,3,12,4,2,10] largest bitonic string:-",largest_bitonic_seq_print([1,3,12,4,2,10]))
print("[1,10,4,9,2,-1,100] largest bitonic string:-",largest_bitonic_seq_print([1,10,4,9,2,-1,100]))