# longest palindrome
# bbbab babad


def isPalindrome(s):
	s_inv = s[::-1]
	if s == s_inv:
		return True
	return False

def longestPalindrome(s):
	print("called with ",s) if debug else None
	if isPalindrome(s):
		print("return ",s) if debug else None
		return s
	
	if len(s) == 0:
		print("return None") if debug else None
		return None
		
	if len(s) == 1:
		print("return ",s) if debug else None
		return s
		
	if len(s) == 2:
		if s[0] == s[1]:
			print("return ",s) if debug else None
			return s
		else:
			print("return ",s[0]) if debug else None
			return s[0]
	
	longest_s = ''
	s1 = longestPalindrome(s[1:])
	s2 = longestPalindrome(s[:-1])
	s3 = longestPalindrome(s[1:-1])
	
	if len(s1) >= len(s2) and len(s1) >= len(s3):
		print("return s1",s1,s2,s3) if debug else None
		return s1
	elif len(s2) >= len(s3) and len(s2) >= len(s1):
		print("return s2 ",s2,s1,s3) if debug else None
		return s2
	else:
		print("return s3 ",s3,s1,s2) if debug else None
		return s3
		
debug = True
debug = False
print(longestPalindrome('bbbab'))
print(longestPalindrome('babad'))
print(longestPalindrome('bbb'))
print(longestPalindrome('bab'))
print(longestPalindrome('baba'))
print(longestPalindrome('ab'))
print(longestPalindrome('b'))

import copy
def longestPalindrome(s):

	l = len(s)
	print("called with ",s) if debug else None
	
	if l == 0:
		print("return None") if debug else None
		return None
		
	if l == 1:
		print("return ",s) if debug else None
		return s
		
	if l == 2:
		if s[0] == s[1]:
			print("return ",s) if debug else None
			return s
		else:
			print("return ",s[0]) if debug else None
			return s[0]
			
	cache = [[0 for col in range(l)] for row in range(l)]
		
	for r in range(l):
		cache[r][r] = 1
		
	max_len = 1
	max_pal = s[0]
				
				
	for gap in range(l):
		for r in range(l):
			for c in range(r,r+gap+1):
				if c < l:
					if c == r+1:
						if s[c-1] == s[c]:
							cache[r][c] = 1
						else:
							cache[r][c] = 0
					if c > r+1:
						if cache[r+1][c-1] == 1 and s[r] == s[c]:
							cache[r][c] = 1
					
					if cache[r][c] == 1 and max_len < abs(c-r)+1:
						max_len = abs(c-r) + 1
						max_str = s[r:c+1]
	
	return(s,max_len,max_str)
					
					
	
print("################################")
print("###### Dynamic Programing ######")
print("################################")
print(longestPalindrome('bbbab'))
print(longestPalindrome('babad'))
print(longestPalindrome('bbb'))
print(longestPalindrome('bab'))
print(longestPalindrome('baba'))
print(longestPalindrome('ab'))
print(longestPalindrome('b'))
				
			
		
	

