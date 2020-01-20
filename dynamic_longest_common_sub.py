# find longest common subset given two strings
# S1 = AAACCGTGAGTTATTCGTTCTAGAA
# S2 = CACCCCTAAGGTACCTTTGGTTC

# Common subsequence = ACCTAGTACTTTG (13)
# S1 = ABCD
# S2 = AEBD 
# Longest common subsequence = 3 (ABD)

def longest_common_subsequence(s1,s2):

	len1 = len(s1)
	len2 = len(s2)
	print("Calling ",s1,s2,len1,len2) if debug else None
	if len1 == 0 or len2 == 0:
		return 0		
		
	lcs1 = 0
	lcs2 = 0
	lcs3 = 0
	if s1[0] == s2[0]:
		lcs1 = lcs1 + 1
		if len1 > 0 and len2 > 0:
			lcs1 += longest_common_subsequence(s1[1:],s2[1:])
	else:
		if len1 > 1:
			lcs2 = lcs2 + longest_common_subsequence(s1[1:],s2) 
		if len2 > 1:
			lcs3 = lcs3 + longest_common_subsequence(s1,s2[1:])

	lcs = max(lcs1,lcs2,lcs3)
	
	print(lcs1,lcs2,lcs3,"Returning2 ",lcs) if debug else None
	return lcs
	
debug = False

print("#######################")
print("### Using Recusrion ###")
print("#######################")
print('a','c',longest_common_subsequence('a','c'))
print('a','a',longest_common_subsequence('a','a'))
print('a','ab',longest_common_subsequence('a','ab'))
print('ab','a',longest_common_subsequence('ab','a'))
print('ba','a',longest_common_subsequence('ba','a'))
print('ba','bc',longest_common_subsequence('ba','bc'))
print('ba','ba',longest_common_subsequence('ba','ba'))
print('bac','bac',longest_common_subsequence('bac','bac'))
print('ABCD','AEBD',longest_common_subsequence('ABCD','AEBD'))
print('ABCD','AEBDA',longest_common_subsequence('ABCD','AEBDA'))
#print('AAACCGTGAGTTATTCGTTCTAGAA','CACCCCTAAGGTACCTTTGGTTC',longest_common_subsequence('AAACCGTGAGTTATTCGTTCTAGAA','CACCCCTAAGGTACCTTTGGTTC'))
print('AAACCGTGAG','CACCCCTAAG',longest_common_subsequence('AAACCGTGAG','CACCCCTAAG'))
print('AAACC','C',longest_common_subsequence('AAACC','C'))
print('AAACC','A',longest_common_subsequence('AAACC','A'))
print('AAACC','AC',longest_common_subsequence('AAACC','AC'))
print('AAACC','CACC',longest_common_subsequence('AAACC','CACC'))



def longest_common_subsequence(s1,s2):
	if len(s1) == 0 or len(s2) == 0:
		return 0;
		
		
	cache = [[0 for i in range(len(s1))] for j in range(len(s2))]
	
	
	if s1[0] == s2[0]:
		cache[0][0] = 1
	#print(cache)
	
	
	skip = 0
	for c in range(1,len(s1)):
		if s1[c] == s2[0] and skip != 1 and cache[0][0] != 1:
			cache[0][c] = cache[0][c-1] + 1
			skip = 1
		else:
			cache[0][c] = cache[0][c-1]
	print(cache) if debug else None

	skip = 0
	for r in range(1,len(s2)):
		if s1[0] == s2[r] and skip != 1 and cache[0][0] != 1:
			cache[r][0] = cache[r-1][0] + 1
			skip = 1
		else:
			cache[r][0] = cache[r-1][0]
	print(cache) if debug else None

	for r in range(1,len(s2)):
		for c in range(1,len(s1)):
			if s1[c] == s2[r]:
				cache[r][c] = 1 + cache[r-1][c-1]
			else:
				cache[r][c] = max(cache[r-1][c],cache[r][c-1])
	
	print(cache) if debug else None
	return cache[len(s2)-1][len(s1)-1]
	
	
debug = True
debug = False
print("################")
print("### Using DP ###")
print("################")
print('a','c',longest_common_subsequence('a','c'))
print('a','a',longest_common_subsequence('a','a'))
print('a','ab',longest_common_subsequence('a','ab'))
print('ab','a',longest_common_subsequence('ab','a'))
print('ba','a',longest_common_subsequence('ba','a'))
print('ba','bc',longest_common_subsequence('ba','bc'))
print('ba','ba',longest_common_subsequence('ba','ba'))
print('bac','bac',longest_common_subsequence('bac','bac'))
print('ABCD','AEBD',longest_common_subsequence('ABCD','AEBD'))
print('ABCD','AEBDA',longest_common_subsequence('ABCD','AEBDA'))
print('AAACCGTGAGTTATTCGTTCTAGAA','CACCCCTAAGGTACCTTTGGTTC',longest_common_subsequence('AAACCGTGAGTTATTCGTTCTAGAA','CACCCCTAAGGTACCTTTGGTTC'))
print('AAACCGTGAG','CACCCCTAAG',longest_common_subsequence('AAACCGTGAG','CACCCCTAAG'))
print('AAACC','C',longest_common_subsequence('AAACC','C'))
print('AAACC','A',longest_common_subsequence('AAACC','A'))
print('AAACC','AC',longest_common_subsequence('AAACC','AC'))
print('AAACC','CACC',longest_common_subsequence('AAACC','CACC'))




# (base) D:\>python dynamic_longest_common_sub.py
# #######################
# ### Using Recusrion ###
# #######################
# a c 0
# a a 1
# a ab 1
# ab a 1
# ba a 1
# ba bc 1
# ba ba 2
# bac bac 3
# ABCD AEBD 3
# ABCD AEBDA 3
# AAACCGTGAG CACCCCTAAG 6
# AAACC C 1
# AAACC A 1
# AAACC AC 2
# AAACC CACC 3
# ################
# ### Using DP ###
# ################
# a c 0
# a a 1
# a ab 1
# ab a 1
# ba a 1
# ba bc 1
# ba ba 2
# bac bac 3
# ABCD AEBD 3
# ABCD AEBDA 3
# AAACCGTGAGTTATTCGTTCTAGAA CACCCCTAAGGTACCTTTGGTTC 14
# AAACCGTGAG CACCCCTAAG 6
# AAACC C 1
# AAACC A 1
# AAACC AC 2
# AAACC CACC 3
