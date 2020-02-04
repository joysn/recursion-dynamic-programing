# dynamic square submatrix
# Given a 2D boolean array, find the largest square subarray of true values. The return value should be the side length of the
# largest square subarray subarray

import copy

def largest_square_sub(inp_mat):
	cols = len(inp_mat[0])
	rows = len(inp_mat)
	cache = [[0 for c in range(cols)] for r in range(rows)]
	
	max_size = 0
	
	for c in range(cols):
		if inp_mat[0][c] == True:
			cache[0][c] = 1
			if max_size < cache[0][c]:
				max_size = copy.deepcopy(cache[0][c])
			
	for r in range(rows):
		if inp_mat[r][0] == True:
			cache[r][0] = 1
			if max_size < cache[r][0]:
				max_size = copy.deepcopy(cache[r][0])
	
	
	for r in range(1,rows):
		for c in range(1,cols):
			if inp_mat[r][c] == True:
				cache[r][c] = min(cache[r-1][c-1],cache[r-1][c],cache[r][c-1]) + 1
				if max_size < cache[r][c]:
					max_size = copy.deepcopy(cache[r][c])
				
				
	return max_size
	
def display_mat(inp_mat):
	for r in range(len(inp_mat)):
		print(inp_mat[r])
		
	return
inp_mat = \
[[False, True, False, False], 
[True,True,True,True],
[False,True,True,False]]
print("Largest sub matrix of ")
display_mat(inp_mat)
print(" is: ",largest_square_sub(inp_mat))


inp_mat = \
[[True,True, True, True, True], 
[True,True,True,True,False],
[True,True,True,True,False],
[True,True,True,True,False],
[True,False,False,False,False]]
print("Largest sub matrix of ")
display_mat(inp_mat)
print(" is: ",largest_square_sub(inp_mat))


inp_mat = \
[[False,True, True, True, True], 
[True,True,True,True,False],
[True,True,True,True,False],
[True,True,True,True,False],
[True,False,False,False,False]]
print("Largest sub matrix of ")
display_mat(inp_mat)
print(" is: ",largest_square_sub(inp_mat))

inp_mat = \
[[True,True, True, True, True], 
[True,True,True,True,False],
[True,True,True,True,False],
[False,True,True,True,False],
[True,False,False,False,False]]

print("Largest sub matrix of ")
display_mat(inp_mat)
print(" is: ",largest_square_sub(inp_mat))



# (base) D:\>python dynamic_largest_square_submatrix.py
# Largest sub matrix of
# [False, True, False, False]
# [True, True, True, True]
# [False, True, True, False]
 # is:  2
# Largest sub matrix of
# [True, True, True, True, True]
# [True, True, True, True, False]
# [True, True, True, True, False]
# [True, True, True, True, False]
# [True, False, False, False, False]
 # is:  4
# Largest sub matrix of
# [False, True, True, True, True]
# [True, True, True, True, False]
# [True, True, True, True, False]
# [True, True, True, True, False]
# [True, False, False, False, False]
 # is:  3
# Largest sub matrix of
# [True, True, True, True, True]
# [True, True, True, True, False]
# [True, True, True, True, False]
# [False, True, True, True, False]
# [True, False, False, False, False]
 # is:  3