# given an array, write a program to return the length of the largest monotonically increasing subsequence


def max_len(s1,curr_l): #O(2^n), O(1)
	
	global max_l
	print("Calling with ",s1,curr_l,max_l) if debug else None
	if len(s1) == 0:
		curr_l = 0
		return max(max_l,curr_l)
		
	if len(s1) == 1:
		curr_l = 1
		return max(max_l,curr_l)
		
	if s1[0]+1 == s1[1]:
		curr_l += 1
		max_l = max(max_l,curr_l)
		ml = max_len(s1[1:],curr_l)
	else:
		ml = max_len(s1[1:],1)
		
	max_l = max(max_l,ml)
	print(s1,"ml and max_ml is ",ml,max_l) if debug else None
	
	return max_l
	
debug = True
debug = False
print("###########################")
print("##### Using Recursion #####")
print("###########################")
global max_l
max_l = 0
print("[1,2]",max_len([1,2],1))
max_l = 0
print("[1,3]",max_len([1,3],1))
max_l = 0
print("[1,2,4,5]",max_len([1,2,4,5],1))
max_l = 0
print("[1,2,3]",max_len([1,2,3],1))
max_l = 0
print("[1,2,5,4,5,6,7]",max_len([1,2,5,4,5,6,7],1))
print("[1,2,5,4,-2,-1,0,1,5,6,7]",max_len([1,2,5,4,-2,-1,0,1,5,6,7],1))



def max_len(s1): # O(n), O(1)
	if len(s1) == 0:
		return 0
		
	if len(s1) == 1:
		return 1
		
	#cache = [0 for i in range(len(s1))]
	curr_l = 0
	
	print(cache) if debug else None
	max_l = 0
	for i in range(1,len(s1)):
		if s1[i] == s1[i-1]+1:
			curr_l = curr_l+1
			max_l = max(max_l, curr_l)
		else:
			curr_l = 0
			
	print(cache,max_l) if debug else None
	return max_l+1
	
debug = True
debug = False
print("####################")
print("##### Using DP #####")
print("####################")
print("[1,2]",max_len([1,2]))
print("[1,3]",max_len([1,3]))
print("[1,2,4,5]",max_len([1,2,4,5]))
print("[1,2,3]",max_len([1,2,3]))
print("[1,2,5,4,5,6,7]",max_len([1,2,5,4,5,6,7]))
print("[1,2,5,4,-2,-1,0,1,5,6,7]",max_len([1,2,5,4,-2,-1,0,1,5,6,7]))	
		
	