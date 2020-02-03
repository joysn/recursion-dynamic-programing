# longest palindromic subsequence


def is_palindrom(str):
	str_inv = str[::-1]
	if str == str_inv:
		return True
	else:
		return False
		
# print(is_palindrom('aba'))
# print(is_palindrom('abba'))
# print(is_palindrom('a'))
# print(is_palindrom(''))
# print(is_palindrom('abc'))
# print(is_palindrom('abcba'))
# print(is_palindrom('abcda'))


def longest_common_subseq(str1,str2):
	print("Called with - [",str1,"][",str2,"]") if debug else None
	if len(str1) == 0 or len(str2) == 0:
		return 0,''
		
	
	max_size = 0
	l1 = 0
	l2 = 0
	l3 = 0
	op1 = ''
	op2 = ''
	op3 = ''
	print("[",str1[0],"][",str2[0],"]") if debug else None
	if str1[0] == str2[0]:
		l1,op1 = longest_common_subseq(str1[1:],str2[1:])
		l1 = 1 + l1
		op1 = str(op1) + str1[0]
	else:
		
		l2,op2 = longest_common_subseq(str1[1:],str2)
		l3,op3 = longest_common_subseq(str1,str2[1:])
	
	if l1 >= l3 and l1 >= l2:
		return l1,op1
	elif l2 >= l3 and l2 >= l1:
		return l2,op2
	else:
		return l3,op3
	#max_size = max(l1,l2,l3)
	#return max_size
	
def longest_palindromic_subseq(str):
	str_inv = str[::-1]
	l = longest_common_subseq(str,str_inv)
	return l

debug = True
debug = False

print("#######################")
print("### Using Recusrion ###")
print("#######################")
print("a:",longest_palindromic_subseq("a"))	
print("ab:",longest_palindromic_subseq("ab"))	
print("abc:",longest_palindromic_subseq("abc"))
print("aba:",longest_palindromic_subseq("aba"))
print("abbd:",longest_palindromic_subseq("abbd"))
print("abcbd:",longest_palindromic_subseq("abcbd"))
print("bbabcbcab:",longest_palindromic_subseq("bbabcbcab"))

import copy

def longest_common_subseq(str1,str2):
	if len(str1) == 0 or len(str2) == 0:
		return 0
		
	cache = [[0 for c in range(len(str1))] for r in range(len(str2))]
	for r in range(len(str2)):
		for c in range(len(str1)):
			cache[r][c] = 0,''
	
	if str1[0] == str2[0]:
		cache[0][0] = 1,str1[0]
		
	print(cache) if debug else None
	
	for c in range(1,len(str1)):
		if str1[c] == str2[0]:
			cache[0][c] = 1,str1[c]
			#cache[0][c] = max(cache[0][c-1],1)
		else:
			cache[0][c] = copy.deepcopy(cache[0][c-1])
	print(cache) if debug else None		
	
	for r in range(1,len(str2)):
		if str1[0] == str2[r]:
			cache[r][0] = 1,str2[r]
			#cache[r][0] = max(1,cache[r-1][0])
		else:
			cache[r][0] = copy.deepcopy(cache[r-1][0])
	print(cache) if debug else None
	
	for r in range(1,len(str2)):
		for c in range(1,len(str1)):
			l1,op1 = cache[r-1][c]
			l2,op2 = cache[r][c-1]
			if str1[c] == str2[r]:
				l3,op3 = cache[r-1][c-1]
				l3 += 1
				op3 += str1[c]
				if l1 >= l2 and l1 >= l3:
					cache[r][c] = l1,op1
				elif l2 >= l1 and l2 >= l3:
					cache[r][c] = l2,op2
				else:
					cache[r][c] = l3,op3
				#cache[r][c] = max(cache[r-1][c],cache[r][c-1], cache[r-1][c-1] + 1)
			else:
				if l1 >= l2:
					cache[r][c] = l1,op1
				else:
					cache[r][c] = l2,op2
				#cache[r][c] = max(cache[r-1][c],cache[r][c-1])
	print(cache) if debug else None			
	
	return cache[len(str2)-1][len(str1)-1]
				
				
def longest_palindromic_subseq(str):
	str_inv = str[::-1]
	l = longest_common_subseq(str,str_inv)
	return l

debug = True
debug = False

print("################")
print("### Using DP ###")
print("################")
print("a:",longest_palindromic_subseq("a"))	
print("ab:",longest_palindromic_subseq("ab"))	
print("abc:",longest_palindromic_subseq("abc"))
print("aba:",longest_palindromic_subseq("aba"))
print("abbd:",longest_palindromic_subseq("abbd"))
print("abcbd:",longest_palindromic_subseq("abcbd"))
print("bbabcbcab:",longest_palindromic_subseq("bbabcbcab"))

