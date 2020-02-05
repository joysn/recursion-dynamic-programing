#Given a sring s, partition sring such that every subsring of the partition is a palindrome. 
# Find the partitioning with minimum cuts in input sring.
# INPUT: s = "aabbcbb"

# OUTPUT:
# partition = 1 : [aa bbcbb]
# partition = 2 : [a a bbcbb]
# partition = 3 : [a a b bcb b]
# partition = 4 : [a a b b c b b]


import sys
import copy
def is_palindrom(s):
	if len(s) == 1:
		return True
		
	s_inv = s[::-1]
	if s == s_inv:
		return True
	else:
		False
		
def largest_palindrom(s):
	print(s) if debug else None
	if is_palindrom(s):
		print("returning:-",s,1,[s]) if debug else None
		return 1,[s]
	
	min_cs = sys.maxsize
	min_s = []
	for cs in range(1,len(s)):
		c1,s1 = largest_palindrom(s[:cs])
		c2,s2 = largest_palindrom(s[cs:])
		temp_c = c1 + c2
		temp_s = s1+s2
		if min_cs > temp_c:
			min_cs = temp_c
			min_s = copy.deepcopy(temp_s)
			
	print("returning:-",s, min_cs,min_s) if debug else None
	return min_cs,min_s
		
debug = True
debug = False
print("###########################")
print("##### Using Recursion #####")
print("###########################")
print("aba",largest_palindrom("aba"))
print("ab",largest_palindrom("ab"))
print("abc",largest_palindrom("abc"))
print("abb",largest_palindrom("abb"))
print("aabb",largest_palindrom("aabb"))
print("aabbcbb",largest_palindrom("aabbcbb"))


def display_cache(cache):
	for r in range(len(cache)):
		print(cache[r])
		

def largest_palindrom(s):

	if len(s) == 0 or len(s) == 1:
		return len(s),[s]
		
	if is_palindrom(s):
		return 1,[s]
		
	rows = len(s)
	cols = len(s)
	cache = [[sys.maxsize for c in range(rows)] for r in range(cols)]
	for r in range(rows):
		for c in range(cols):
			cache[r][c] = sys.maxsize,[]
		
	# start = 0, end = 0
	cache[0][0] = 0,[]
	cache[0][1] = 1,[s[0]]
	cache[1][0] = 1,[s[0]]
	for c in range(1,cols):
		if is_palindrom(s[:c]):
			cache[0][c] = 1,[s[:c]]
		else:
			temp_c,temp_cs = cache[0][c-1]
			cache[0][c] = 1+ temp_c, temp_cs+[s[c-1]]
			
	for r in range(1,rows):
		if is_palindrom(s[:r]):
			cache[r][0] = 1,[s[:r]]
		else:
			emp_c,temp_cs = cache[r-1][0]
			cache[r][0] = 1+ temp_c, temp_cs+[s[r-1]]
	
	display_cache(cache)	
	
	# for r in range(1,rows):
		# for c in range(1,cols):
			# if is_palindrom[c-1:r]:
				# cache[r][c] = 1,[s[c-1:r]]
			# else:
				
		
	
debug = True
debug = False
print("####################")
print("##### Using DP #####")
print("####################")
#print("aba",largest_palindrom("aba"))
#print("ab",largest_palindrom("ab"))
# print("abc",largest_palindrom("abc"))
print("abb",largest_palindrom("abb"))
# print("aabb",largest_palindrom("aabb"))
# print("aabbcbb",largest_palindrom("aabbcbb"))
	