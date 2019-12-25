# Given a matrix of order N*N 
# What are the total number of ways in which we can move from top left cell arr[0][0] to the bottom rigt cell arr[n-1][n-1]
# given that we can move either downward or rightward


# n = 3 (3-2)
# row = 0..2
# col = 0..2
# [1, 4, 3]
# [2, 6, 9]
# [8, 5, 2]

# dr = sr and dc = sc+1
# dr = sr+1 and dc = sc
# -- return 1

# (s,[0,1]) no_of_way([0,1],d)
# +
# (s,[0,2]) no_of_way([0,2],d)
# +
# (s,[1,0]) no_of_way([1,0],d)
# +
# :
# :
# +
# (s,[2,1]) no_of_way([2,1],d)


######################
##### RECUSRSION #####
######################

debug = False

def no_of_ways(sr,sc,dr,dc):
	print("Going [",sr,",",sc,"]->[",dr,",",dc,"]") if debug else None
	#rows = dr - sr
	#columns = dc - sc
	#print(rows,columns) if debug else None
	if (dr == sr) and (dc == sc):
		print("# of Ways 1") if debug else None
		return 1
	if (dr == sr) and (dc == sc+1):
		print("# of Ways 1") if debug else None
		return 1
	if (dr == sr+1) and (dc == sc):
		print("# of Ways 1") if debug else None
		return 1
	noofways = 0
	
	for c in range(sc+1,dc):
		print("value of c is",c) if debug else None
		print("Calling with [",sr,",",sc,"][",sr,",",c,"] AND [",sr,",",c,"][",dr,",",dc,"]") if debug else None
		right = 0
		left = no_of_ways(sr,sc,sr,c)
		right = no_of_ways(sr,c,dr,dc)
		print("Left:",left,"Right:",right) if debug else None
		noofways = noofways + left * right + 1
	
	for r in range(sr+1,dr):
		print("value of r is:",r) if debug else None
		#if sr+1 <= dr:
		left = no_of_ways(sr,sc,r,sc) 
		right = no_of_ways(r,sc,dr,dc)
		print("Calling with [",sr,",",sc,"][",r,",",sc,"] AND [",r,",",sc,"][",dr,",",dc,"]") if debug else None
		noofways = noofways + left * right + 1
			
	return noofways
			
input = [[1, 4],[2, 6]]
print("No of ways to go:- ",no_of_ways(0,0,len(input)-1,len(input)-1))

input = [[1, 4, 3],[2, 6, 9],[8, 5, 2]]
print("No of ways to go:- ",no_of_ways(0,0,len(input)-1,len(input)-1))
input = [[1, 4, 3,0],[2, 6, 9, 8],[8, 5, 2, 4],[6,10,14,3]]
print("No of ways to go:- ",no_of_ways(0,0,len(input)-1,len(input)-1))

# (base) D:\>python dynamic_matrix_parse.py
# No of ways to go:-  0
# No of ways to go:-  4
# No of ways to go:-  40