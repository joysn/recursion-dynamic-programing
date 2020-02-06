# egg problem, 
# given n eggs, x floors, what is the min number of floors required to know at what floor, the eggs can break

import sys

def countDrops(numFloors, numEggs):
	if numFloors == 0 or numFloors == 1 or numEggs == 1:
		return numFloors
		
	min = sys.maxsize
	min_floor = numFloors
	for p in range(1,numFloors+1):
		
		c1 = countDrops(p-1,numEggs-1)
		c2 = countDrops(numFloors-p,numEggs)
		
		c = max(c1,c2)
		if c < min:
			min = c
			min_floor = p
		#print(c,p,min,min_floor)
	return min+1
	
	
print('###########################')
print("##### Using Recursion #####")
print('###########################')

for floor in range(15):
	print("Count of drops needed for ",floor," floors, 2 eggs:",countDrops(floor,2))

import copy
def countDrops(numFloors,numEggs):
	
	if numFloors == 0 or numFloors == 1 or numEggs == 1:
		return numFloors
		
	cache = [[sys.maxsize for f in range(numFloors+1)] for e in range(numEggs+1)]
	
	# For numFloors=0,1, i.e. cache[*][0],cache[*][1]
	for e in range(numEggs+1):
		cache[e][0] = 0	
		cache[e][1] = 1
	print(cache) if debug else None
	
	# For numeggs = 0,1 (i.e. cache[0][*],cache[1][*])
	for f in range(1,numFloors+1):
		cache[0][f] = 0
		cache[1][f] = f
	print(cache) if debug else None
	
	
	# for numEggs >= 1
	for e in range(2,numEggs+1):
		# Floors >= 1
		for f in range(2,numFloors+1):
			for p in range(1,f+1):
				print("Indexes--->",p,f,e) if debug else None
				c1 = cache[e-1][p-1]
				c2 = cache[e][f-p]
				c = max(c1,c2)
				print("--->",c1,c2,c) if debug else None
				if c < cache[e][f]:
					cache[e][f] = c
			cache[e][f] += 1
			print(cache) if debug else None
			#cache[e][f] = minc
				
	print(cache) if debug else None
	return cache[numEggs][numFloors]
				
	
print('####################')
print("##### Using DP #####")
print('####################')

debug = True
debug = False
for floor in range(101):
	print("Count of drops needed for ",floor," floors, 2 eggs:",countDrops(floor,2))	
	
	

# (base) D:\>python dynamic_egg_floor_problem.py
# ###########################
# ##### Using Recursion #####
# ###########################
# Count of drops needed for  0  floors, 2 eggs: 0
# Count of drops needed for  1  floors, 2 eggs: 1
# Count of drops needed for  2  floors, 2 eggs: 2
# Count of drops needed for  3  floors, 2 eggs: 2
# Count of drops needed for  4  floors, 2 eggs: 3
# Count of drops needed for  5  floors, 2 eggs: 3
# Count of drops needed for  6  floors, 2 eggs: 3
# Count of drops needed for  7  floors, 2 eggs: 4
# Count of drops needed for  8  floors, 2 eggs: 4
# Count of drops needed for  9  floors, 2 eggs: 4
# Count of drops needed for  10  floors, 2 eggs: 4
# Count of drops needed for  11  floors, 2 eggs: 5
# Count of drops needed for  12  floors, 2 eggs: 5
# Count of drops needed for  13  floors, 2 eggs: 5
# Count of drops needed for  14  floors, 2 eggs: 5
# ####################
# ##### Using DP #####
# ####################
# Count of drops needed for  0  floors, 2 eggs: 0
# Count of drops needed for  1  floors, 2 eggs: 1
# Count of drops needed for  2  floors, 2 eggs: 2
# Count of drops needed for  3  floors, 2 eggs: 2
# Count of drops needed for  4  floors, 2 eggs: 3
# Count of drops needed for  5  floors, 2 eggs: 3
# Count of drops needed for  6  floors, 2 eggs: 3
# Count of drops needed for  7  floors, 2 eggs: 4
# Count of drops needed for  8  floors, 2 eggs: 4
# Count of drops needed for  9  floors, 2 eggs: 4
# Count of drops needed for  10  floors, 2 eggs: 4
# Count of drops needed for  11  floors, 2 eggs: 5
# Count of drops needed for  12  floors, 2 eggs: 5
# Count of drops needed for  13  floors, 2 eggs: 5
# Count of drops needed for  14  floors, 2 eggs: 5
# Count of drops needed for  15  floors, 2 eggs: 5
# Count of drops needed for  16  floors, 2 eggs: 6
# Count of drops needed for  17  floors, 2 eggs: 6
# Count of drops needed for  18  floors, 2 eggs: 6
# Count of drops needed for  19  floors, 2 eggs: 6
# Count of drops needed for  20  floors, 2 eggs: 6
# Count of drops needed for  21  floors, 2 eggs: 6
# Count of drops needed for  22  floors, 2 eggs: 7
# Count of drops needed for  23  floors, 2 eggs: 7
# Count of drops needed for  24  floors, 2 eggs: 7
# Count of drops needed for  25  floors, 2 eggs: 7
# Count of drops needed for  26  floors, 2 eggs: 7
# Count of drops needed for  27  floors, 2 eggs: 7
# Count of drops needed for  28  floors, 2 eggs: 7
# Count of drops needed for  29  floors, 2 eggs: 8
# Count of drops needed for  30  floors, 2 eggs: 8
# Count of drops needed for  31  floors, 2 eggs: 8
# Count of drops needed for  32  floors, 2 eggs: 8
# Count of drops needed for  33  floors, 2 eggs: 8
# Count of drops needed for  34  floors, 2 eggs: 8
# Count of drops needed for  35  floors, 2 eggs: 8
# Count of drops needed for  36  floors, 2 eggs: 8
# Count of drops needed for  37  floors, 2 eggs: 9
# Count of drops needed for  38  floors, 2 eggs: 9
# Count of drops needed for  39  floors, 2 eggs: 9
# Count of drops needed for  40  floors, 2 eggs: 9
# Count of drops needed for  41  floors, 2 eggs: 9
# Count of drops needed for  42  floors, 2 eggs: 9
# Count of drops needed for  43  floors, 2 eggs: 9
# Count of drops needed for  44  floors, 2 eggs: 9
# Count of drops needed for  45  floors, 2 eggs: 9
# Count of drops needed for  46  floors, 2 eggs: 10
# Count of drops needed for  47  floors, 2 eggs: 10
# Count of drops needed for  48  floors, 2 eggs: 10
# Count of drops needed for  49  floors, 2 eggs: 10
# Count of drops needed for  50  floors, 2 eggs: 10
# Count of drops needed for  51  floors, 2 eggs: 10
# Count of drops needed for  52  floors, 2 eggs: 10
# Count of drops needed for  53  floors, 2 eggs: 10
# Count of drops needed for  54  floors, 2 eggs: 10
# Count of drops needed for  55  floors, 2 eggs: 10
# Count of drops needed for  56  floors, 2 eggs: 11
# Count of drops needed for  57  floors, 2 eggs: 11
# Count of drops needed for  58  floors, 2 eggs: 11
# Count of drops needed for  59  floors, 2 eggs: 11
# Count of drops needed for  60  floors, 2 eggs: 11
# Count of drops needed for  61  floors, 2 eggs: 11
# Count of drops needed for  62  floors, 2 eggs: 11
# Count of drops needed for  63  floors, 2 eggs: 11
# Count of drops needed for  64  floors, 2 eggs: 11
# Count of drops needed for  65  floors, 2 eggs: 11
# Count of drops needed for  66  floors, 2 eggs: 11
# Count of drops needed for  67  floors, 2 eggs: 12
# Count of drops needed for  68  floors, 2 eggs: 12
# Count of drops needed for  69  floors, 2 eggs: 12
# Count of drops needed for  70  floors, 2 eggs: 12
# Count of drops needed for  71  floors, 2 eggs: 12
# Count of drops needed for  72  floors, 2 eggs: 12
# Count of drops needed for  73  floors, 2 eggs: 12
# Count of drops needed for  74  floors, 2 eggs: 12
# Count of drops needed for  75  floors, 2 eggs: 12
# Count of drops needed for  76  floors, 2 eggs: 12
# Count of drops needed for  77  floors, 2 eggs: 12
# Count of drops needed for  78  floors, 2 eggs: 12
# Count of drops needed for  79  floors, 2 eggs: 13
# Count of drops needed for  80  floors, 2 eggs: 13
# Count of drops needed for  81  floors, 2 eggs: 13
# Count of drops needed for  82  floors, 2 eggs: 13
# Count of drops needed for  83  floors, 2 eggs: 13
# Count of drops needed for  84  floors, 2 eggs: 13
# Count of drops needed for  85  floors, 2 eggs: 13
# Count of drops needed for  86  floors, 2 eggs: 13
# Count of drops needed for  87  floors, 2 eggs: 13
# Count of drops needed for  88  floors, 2 eggs: 13
# Count of drops needed for  89  floors, 2 eggs: 13
# Count of drops needed for  90  floors, 2 eggs: 13
# Count of drops needed for  91  floors, 2 eggs: 13
# Count of drops needed for  92  floors, 2 eggs: 14
# Count of drops needed for  93  floors, 2 eggs: 14
# Count of drops needed for  94  floors, 2 eggs: 14
# Count of drops needed for  95  floors, 2 eggs: 14
# Count of drops needed for  96  floors, 2 eggs: 14
# Count of drops needed for  97  floors, 2 eggs: 14
# Count of drops needed for  98  floors, 2 eggs: 14
# Count of drops needed for  99  floors, 2 eggs: 14
# Count of drops needed for  100  floors, 2 eggs: 14


