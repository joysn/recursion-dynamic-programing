# https://www.youtube.com/watch?v=BFKbbE9Tpqs 30:20
# Many cities
# Many buses and circular routes
# Given two cities can we reach from city1 to city2 using public transport

# cities = [0,1,2,3,4]
# 3 buses
# bus1 = (1,2,4)
# bus2 = (3,5)
# bus3 = (4,6)
# tarnsport = [(1,2,4),(3,5),(4,6)]
# canUsePublicTransport(0,2) -> True
# canUsePublicTransport(2,3) -> False
# canUsePublicTransport(0,4) -> False
# canUsePublicTransport(3,4) -> True

import copy

def canUsePublicTransport(transport,s,d):
	if s == d:
		return True
	
	for i in range(len(transport)):
		if s in transport[i] and d in transport[i]:
			return True
		for j in range(i+1,len(transport)):
			if len(transport[i].intersection(transport[j])) > 0:
				transport[i] = copy.deepcopy(transport[i].union(transport[j]))
				transport[j] = ()
			if s in transport[i] and d in transport[i]:
				return True
		
	#optional piece
	# for i in range(len(transport)):
		# if len(transport[i]) == 0:
			# del transport[i]
			
	# print(transport) if debug else None
	
	# for i in range(len(transport)):
		# if s in transport[i] and d in transport[i]:
			# return True
			
	return False
	
debug = True
debug = False
transport = [{1,2,4},{3,5},{4,6}]

for gap in range(1,5):
	print(gap," Station Difference")
	for s in range(1,7):
		print("From:",s," To:",s+gap,canUsePublicTransport(transport,s,s+gap))
		
# (base) D:\>python dynamic_public_transport.py
# 1  Station Difference
# From: 1  To: 2 True
# From: 2  To: 3 False
# From: 3  To: 4 False
# From: 4  To: 5 False
# From: 5  To: 6 False
# From: 6  To: 7 False
# 2  Station Difference
# From: 1  To: 3 False
# From: 2  To: 4 True
# From: 3  To: 5 True
# From: 4  To: 6 True
# From: 5  To: 7 False
# From: 6  To: 8 False
# 3  Station Difference
# From: 1  To: 4 True
# From: 2  To: 5 False
# From: 3  To: 6 False
# From: 4  To: 7 False
# From: 5  To: 8 False
# From: 6  To: 9 False
# 4  Station Difference
# From: 1  To: 5 False
# From: 2  To: 6 True
# From: 3  To: 7 False
# From: 4  To: 8 False
# From: 5  To: 9 False
# From: 6  To: 10 False
	
	
	