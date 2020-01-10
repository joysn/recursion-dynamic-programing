# A chess piece that can move like a horse(knight) 2H+1V or 2V+1H and like a king (1H or 1V)
# Find minimum # of moves required to reach from sr,sc to dr,dc


# Chess is 8*8 matrix

def min_no_of_moves(sr,sc,dr,dc):
	print(sr,sc,dr,dc) if debug else None
	
	# Invalid criteria
	if sr > 7 or sc > 7 or dr > 7 or dc > 7:
		print(0) if debug else None
		return 0
	if sr < 0 or sc < 0 or dr < 0 or dc < 0:
		print(0) if debug else None
		return 0
		
	# Exit criteria - 1
	if sr == dr and sc == dc:
		print(0) if debug else None
		return 0
		
	#Moves of Horse(Knight)
	if abs(dc-sc)*2 == abs(dr-sr):
		print(abs(dc-sc)) if debug else None
		return abs(dc-sc)
	if abs(dc-sc) == 2*abs(dr-sr):
		print(abs(dr-sr)) if debug else None
		return abs(dr-sr)
		
	# Moves of King
	if sc == dc and abs(dr-sr) == 1:
		print(1) if debug else None
		return 1
	if sr == dr and abs(dc-sc) == 1:
		print(1) if debug else None
		return 1
	if abs(dc-sc) == 1 and abs(dr-sr) == 1:
		print(1) if debug else None
		return 1
	
	
		
	min_ways = 0
	w1 = 1000000000000000000
	w2 = 1000000000000000000
	w3 = 1000000000000000000
	w4 = 1000000000000000000
	w5 = 1000000000000000000
	if dc >= sc and dr >= sr: # 1st quad
		print("Quad 1") if debug else None
		if dr > sr:
			w1 = 1 + min_no_of_moves(sr+1,sc,dr,dc)
		if dc > sc:
			w2 = 1 + min_no_of_moves(sr,sc+1,dr,dc)
		if dr > sr and dc > sc:
			w3 = 1 + min_no_of_moves(sr+1,sc+1,dr,dc)
		if dr > sr and dc > sc+1:
			w4 = 1 + min_no_of_moves(sr+1,sc+2,dr,dc)
		if dr > sr+1 and dc > sc:
			w5 = 1 + min_no_of_moves(sr+2,sc+1,dr,dc)
		
	elif dc < sc and dr >= sr: # 2nd quad
		print("Quad 2") if debug else None
		if dr > sr:
			w1 = 1 + min_no_of_moves(sr+1,sc,dr,dc)
		if dc < sc:
			w2 = 1 + min_no_of_moves(sr,sc-1,dr,dc)
		if dr > sr and dc < sc:
			w3 = 1 + min_no_of_moves(sr+1,sc-1,dr,dc)
		if dr > sr and dc < sc-1:
			w4 = 1 + min_no_of_moves(sr+1,sc-2,dr,dc)
		if dr > sr+1 and dc < sc:
			w5 = 1 + min_no_of_moves(sr+2,sc-1,dr,dc)
		
	elif dc < sc and dr < sr:# 3rd quad 
		print("Quad 3") if debug else None
		if dr < sr:
			w1 = 1 + min_no_of_moves(sr-1,sc,dr,dc)
		if dc < sc:
			w2 = 1 + min_no_of_moves(sr,sc-1,dr,dc)
		if dr < sr and dc < sc:
			w3 = 1 + min_no_of_moves(sr-1,sc-1,dr,dc)
		if dr < sr and dc < sc-1:
			w4 = 1 + min_no_of_moves(sr-1,sc-2,dr,dc)
		if dr < sr-1 and dc < sc:
			w5 = 1 + min_no_of_moves(sr-2,sc-1,dr,dc)
			
	elif dc >= sc and dr < sr: # 4th quad
		print("Quad 4") if debug else None
		if dr < sr:
			w1 = 1 + min_no_of_moves(sr-1,sc,dr,dc)
		if dc > sr:
			w2 = 1 + min_no_of_moves(sr,sc+1,dr,dc)
		if dr < sr and dc > sc:
			w3 = 1 + min_no_of_moves(sr-1,sc+1,dr,dc)
		if dr < sr and dc > sc+1:
			w4 = 1 + min_no_of_moves(sr-1,sc+2,dr,dc)
		if dr < sr-1 and dc > sc:
			w5 = 1 + min_no_of_moves(sr-2,sc+1,dr,dc)
	
	min_ways = min(w1,w2,w3,w4,w5)
	print("[",w1,w2,w3,w4,w5,"]",min_ways) if debug else None
	return(min_ways)


debug = False
print("########################")
print("## Recursive Solution ##")
print("########################")
print("Move from (0,0) to (0,1) [1]:",min_no_of_moves(0,0,0,1))	
print("Move from (0,1) to (0,0) [1]:",min_no_of_moves(0,1,0,0))	
print("Move from (0,0) to (1,0) [1]:",min_no_of_moves(0,0,1,0))	
print("Move from (1,0) to (0,0) [1]:",min_no_of_moves(1,0,0,0))	
print("Move from (0,0) to (1,1) [1]:",min_no_of_moves(0,0,1,1))	
print("Move from (0,0) to (1,2) [1]:",min_no_of_moves(0,0,1,2))	
print("Move from (1,2) to (0,0) [1]:",min_no_of_moves(1,2,0,0))	
print("Move from (0,0) to (2,1) [1]:",min_no_of_moves(0,0,2,1))	
print("Move from (0,0) to (2,2) [2]:",min_no_of_moves(0,0,2,2))	
print("Move from (0,0) to (2,3) [2]:",min_no_of_moves(0,0,2,3))	
print("Move from (2,3) to (0,0) [2]:",min_no_of_moves(2,3,0,0))
print("Move from (0,0) to (4,3) [3]:",min_no_of_moves(0,0,4,3))	
print("Move from (4,3) to (0,0) [3]:",min_no_of_moves(4,3,0,0))	
print("Move from (4,3) to (5,0) [2]:",min_no_of_moves(4,3,5,0))	
print("Move from (5,0) to (4,3) [2]:",min_no_of_moves(5,0,4,3))	


# DP Solution
def min_no_of_moves(sr,sc,dr,dc):
	rows = abs(dr-sr)
	columns = abs(dc-sc)
	
	if rows == 0 and columns == 0:
		return 0
		
	min_ways = [[10000000000 for i in range(columns+1)] for j in range(rows+1)]
	
	
	min_ways[0][0] = 0
	#print(min_ways)
	#print(min_ways[0])
	if columns >= 1:
		min_ways[0][1] = 1
	if rows >= 1:
		min_ways[1][0] = 1
	if rows >= 1 and columns >= 1:
		min_ways[1][1] = 1
	
	if rows >= 2:
		min_ways[2][1] = 1
		min_ways[2][0] = 2
	if columns >= 2:
		min_ways[1][2] = 1
		min_ways[0][2] = 2
	if columns >= 2 and rows >= 2:
		min_ways[2][2] = 2
	
	for r in range(rows+1):
		for c in range(columns+1):
			if r > 2 or c > 2:
				min_ways[r][c] = min(min_ways[r-1][c]+1, min_ways[r][c-1]+1, min_ways[r-1][c-1]+1, min_ways[r-2][c-1]+1, min_ways[r-1][c-2]+1)
			
	
	#print(min_ways)
	return(min_ways[rows][columns])
	
	
print("#################")
print("## DP Solution ##")
print("#################")
print("Move from (0,0) to (0,1) [1]:",min_no_of_moves(0,0,0,1))	
print("Move from (0,1) to (0,0) [1]:",min_no_of_moves(0,1,0,0))	
print("Move from (0,0) to (1,0) [1]:",min_no_of_moves(0,0,1,0))	
print("Move from (1,0) to (0,0) [1]:",min_no_of_moves(1,0,0,0))	
print("Move from (0,0) to (1,1) [1]:",min_no_of_moves(0,0,1,1))	
print("Move from (0,0) to (1,2) [1]:",min_no_of_moves(0,0,1,2))	
print("Move from (1,2) to (0,0) [1]:",min_no_of_moves(1,2,0,0))	
print("Move from (0,0) to (2,1) [1]:",min_no_of_moves(0,0,2,1))	
print("Move from (0,0) to (2,2) [2]:",min_no_of_moves(0,0,2,2))	
print("Move from (0,0) to (2,3) [2]:",min_no_of_moves(0,0,2,3))	
print("Move from (2,3) to (0,0) [2]:",min_no_of_moves(2,3,0,0))
print("Move from (0,0) to (4,3) [3]:",min_no_of_moves(0,0,4,3))	
print("Move from (4,3) to (0,0) [3]:",min_no_of_moves(4,3,0,0))	
print("Move from (4,3) to (5,0) [2]:",min_no_of_moves(4,3,5,0))	
print("Move from (5,0) to (4,3) [2]:",min_no_of_moves(5,0,4,3))	

# (base) D:\>python dynamic_min_chess_move.py
# ########################
# ## Recursive Solution ##
# ########################
# Move from (0,0) to (0,1) [1]: 1
# Move from (0,1) to (0,0) [1]: 1
# Move from (0,0) to (1,0) [1]: 1
# Move from (1,0) to (0,0) [1]: 1
# Move from (0,0) to (1,1) [1]: 1
# Move from (0,0) to (1,2) [1]: 1
# Move from (1,2) to (0,0) [1]: 1
# Move from (0,0) to (2,1) [1]: 1
# Move from (0,0) to (2,2) [2]: 2
# Move from (0,0) to (2,3) [2]: 2
# Move from (2,3) to (0,0) [2]: 2
# Move from (0,0) to (4,3) [3]: 3
# Move from (4,3) to (0,0) [3]: 3
# Move from (4,3) to (5,0) [2]: 2
# Move from (5,0) to (4,3) [2]: 2
# #################
# ## DP Solution ##
# #################
# Move from (0,0) to (0,1) [1]: 1
# Move from (0,1) to (0,0) [1]: 1
# Move from (0,0) to (1,0) [1]: 1
# Move from (1,0) to (0,0) [1]: 1
# Move from (0,0) to (1,1) [1]: 1
# Move from (0,0) to (1,2) [1]: 1
# Move from (1,2) to (0,0) [1]: 1
# Move from (0,0) to (2,1) [1]: 1
# Move from (0,0) to (2,2) [2]: 2
# Move from (0,0) to (2,3) [2]: 2
# Move from (2,3) to (0,0) [2]: 2
# Move from (0,0) to (4,3) [3]: 3
# Move from (4,3) to (0,0) [3]: 3
# Move from (4,3) to (5,0) [2]: 2
# Move from (5,0) to (4,3) [2]: 2
	
		
		
	
		
