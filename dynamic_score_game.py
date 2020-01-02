# In a game, a player can score 3, 5, 10 . Given N, find total number of unique ways to reach N

def no_of_ways_to_score(score):
	#print("Called",score)
	if score == 0:
		return 1
	if score < 0:
		return 0
	
	no_of_ways = no_of_ways_to_score(score-3) + no_of_ways_to_score(score-5) + no_of_ways_to_score(score-10)
	return no_of_ways
		

def no_of_ways_to_score_dp(score):		
	op = [1,0,0,1,0,1,1,0,2,1,2]
	sc = 11
	while sc <= score:
		print(op[sc-3],op[sc-5],op[sc-10]) if debug else None
		op.append( op[sc-3] +  op[sc-5] + op[sc-10])
		sc += 1
		print(op) if debug else None
	
	return op[score]
	
debug = False

print("***************Using Recursion and dp *****************")
for i in range(17):
	print("To score ",i,", no of ways are: ",no_of_ways_to_score(i),"(Using Recursion)",no_of_ways_to_score_dp(i),"(Using DP)")
			
# (base) D:\>python dynamic_score_game.py
# ***************Using Recursion and dp *****************
# To score  0 , no of ways are:  1 (Using Recursion) 1 (Using DP)
# To score  1 , no of ways are:  0 (Using Recursion) 0 (Using DP)
# To score  2 , no of ways are:  0 (Using Recursion) 0 (Using DP)
# To score  3 , no of ways are:  1 (Using Recursion) 1 (Using DP)
# To score  4 , no of ways are:  0 (Using Recursion) 0 (Using DP)
# To score  5 , no of ways are:  1 (Using Recursion) 1 (Using DP)
# To score  6 , no of ways are:  1 (Using Recursion) 1 (Using DP)
# To score  7 , no of ways are:  0 (Using Recursion) 0 (Using DP)
# To score  8 , no of ways are:  2 (Using Recursion) 2 (Using DP)
# To score  9 , no of ways are:  1 (Using Recursion) 1 (Using DP)
# To score  10 , no of ways are:  2 (Using Recursion) 2 (Using DP)
# To score  11 , no of ways are:  3 (Using Recursion) 3 (Using DP)
# To score  12 , no of ways are:  1 (Using Recursion) 1 (Using DP)
# To score  13 , no of ways are:  5 (Using Recursion) 5 (Using DP)
# To score  14 , no of ways are:  4 (Using Recursion) 4 (Using DP)
# To score  15 , no of ways are:  4 (Using Recursion) 4 (Using DP)
# To score  16 , no of ways are:  9 (Using Recursion) 9 (Using DP)