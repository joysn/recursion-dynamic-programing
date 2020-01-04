# Edit Distance #
# 3 operations  #
# Insert, Replace, Update #
# CAT , CAR = 1
# Saturday , Sunday = 3

########################
## Recursive Solution ##
########################

def edit_distance(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	print("Calling",str1, str2,len1, len2) if debug else None
	
	if len1 == 0:
		return len2
		
	if len2 == 0:
		return len1
	
	if len1 < len2:
		s1 = str1
		s2 = str2
	else:
		s1 = str2
		s2 = str1
		
	while (s1[0] == s2[0]):
		s1 = s1[1:] if len(s1) > 0 else None
		s2 = s2[1:] if len(s2) > 0 else None
		print("Trimmed Str",s1, len(s1), s2, len(s2)) if debug else None
		if len(s1) == 0 or len(s2) == 0:
			break
	
	if len(s1) == len(s2) == 0:
		return 0
			
	print("Modified Calling",s1, s2) if debug else None
	d = i = r = 0
	# delete
	if len(s1) > 1:
		print("Delete",s1[1:], s2) if debug else None
		d = edit_distance(s1[1:], s2) + 1
	else:
		print("Delete",'', s2) if debug else None
		d = edit_distance('', s2) + 1
	
	# replace
	if len(s1) > 1:
		print(s1,s2) if debug else None
		print("Replace",s2[0]+s1[1:], s2) if debug else None
		r = edit_distance(s2[0]+s1[1:], s2) + 1
	else:
		print(s1,s2) if debug else None
		print("Replace",s2[0], s2) if debug else None
		r = edit_distance(s2[0], s2) + 1
	
	# insert
	if len(s2) > 1:
		print("Insert",s1, s2[1:]) if debug else None
		i = edit_distance(s1, s2[1:]) + 1
	else:
		print("Insert",s1, '') if debug else None
		i = edit_distance(s1, '') + 1
	
	print(d,r,i) if debug else None
	if d <= r and d <= i:
		return d
	elif r <= d and r <= i:
		return r
	else:
		return i
			
	
debug = False
print("########################")
print("## Recursive Solution ##")
print("########################")
print("cat and car - 1",edit_distance('cat','car'))
print("car and care - 1",edit_distance('car','care'))
print("cat and care - 2",edit_distance('cat','care'))
print("saturday and sunday - 3",edit_distance('saturday','sunday'))
print("a and bc - 2",edit_distance('a','bc'))
print("edb and dabc - 3",edit_distance('edb','dabc'))
print("ttelli and attller - 4",edit_distance('ttelli','attller'))
print("attll and tteller - 4",edit_distance('attll','tteller'))


#################
## DP Solution ##
#################

def edit_distance(str1, str2):
		
	dist = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]
	
	for	i in range(len(str1)+1):
		dist[0][i] = i
	for	i in range(len(str2)+1):
		dist[i][0] = i
		
	print(dist) if debug else None
	for r in range(1, len(str2)+1):
		for c in range(1,len(str1)+1):
			print(r,c) if debug else None
			if str1[c-1] == str2[r-1]:
				dist[r][c] = dist[r-1][c-1]
			else:
				dist[r][c] = 1+ min(dist[r-1][c-1],dist[r-1][c],dist[r][c-1])
	print(dist) if debug else None
	return(dist[len(str2)][len(str1)])
	
	
	
debug = False	
print("#################")
print("## DP Solution ##")
print("#################")
print("cat and car - 1",edit_distance('cat','car'))
print("car and care - 1",edit_distance('car','care'))
print("cat and care - 2",edit_distance('cat','care'))
print("saturday and sunday - 3",edit_distance('saturday','sunday'))
print("a and bc - 2",edit_distance('a','bc'))
print("edb and dabc - 3",edit_distance('edb','dabc'))
print("ttelli and attller - 4",edit_distance('ttelli','attller'))
print("attll and tteller - 4",edit_distance('attll','tteller'))






