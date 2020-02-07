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
		floor_list = [f for f in range(1,numFloors+1)]
		return numFloors,floor_list
		
	cache = [[sys.maxsize for f in range(numFloors+1)] for e in range(numEggs+1)]
	for e in range(numEggs+1):
		for f in range(numFloors+1):
			cache[e][f] = sys.maxsize,[]
	
	# For numFloors=0,1, i.e. cache[*][0],cache[*][1]
	for e in range(numEggs+1):
		cache[e][0] = 0,[0]
		cache[e][1] = 1,[1]
	print(cache) if debug else None
	
	# For numeggs = 0,1 (i.e. cache[0][*],cache[1][*])
	for f in range(1,numFloors+1):
		cache[0][f] = 0,[0]
		floor_list = [f for f in range(1,f+1)]
		cache[1][f] = f,floor_list
	print(cache) if debug else None
	
	
	# for numEggs >= 1
	for e in range(2,numEggs+1):
		# Floors >= 1
		for f in range(2,numFloors+1):
			for p in range(1,f+1):
				print("Indexes--->",p,f,e) if debug else None
				c1,l1 = cache[e-1][p-1]
				c2,l2 = cache[e][f-p]
				#c = max(c1,c2)
				if c1 > c2:
					c = c1
					l = copy.deepcopy(l1)
				else:
					c = c2
					l = copy.deepcopy(l2)
				print("--->",c1,c2,c) if debug else None
				#if c < cache[e][f]:
				temp_c,temp_l = cache[e][f]
				if c < temp_c:
					cache[e][f] = c,l
			final_c,final_l = cache[e][f]
			final_c += 1
			final_l += [f]
			cache[e][f] = final_c,final_l
			print(cache) if debug else None
			#cache[e][f] = minc
				
	print(cache) if debug else None
	return cache[numEggs][numFloors]
				
	
print('####################')
print("##### Using DP #####")
print('####################')

debug = True
debug = False
#for floor in range(101):
for floor in range(6):
	op = countDrops(floor,2)
	print("Count of drops needed on building with ",floor," floors, 2 eggs:",op[0]," from the floor #s:",op[1])	
	
	

# (base) D:\>python dynamic_egg_floor_problem_print.py
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
# Count of drops needed on building with  0  floors, 2 eggs: 0  from the floor #s: [0]
# Count of drops needed on building with  1  floors, 2 eggs: 1  from the floor #s: [0, 1]
# Count of drops needed on building with  2  floors, 2 eggs: 2  from the floor #s: [1, 2]
# Count of drops needed on building with  3  floors, 2 eggs: 2  from the floor #s: [1, 3]
# Count of drops needed on building with  4  floors, 2 eggs: 3  from the floor #s: [1, 3, 4]
# Count of drops needed on building with  5  floors, 2 eggs: 3  from the floor #s: [1, 3, 5]
# Count of drops needed on building with  6  floors, 2 eggs: 3  from the floor #s: [1, 3, 6]
# Count of drops needed on building with  7  floors, 2 eggs: 4  from the floor #s: [1, 3, 6, 7]
# Count of drops needed on building with  8  floors, 2 eggs: 4  from the floor #s: [1, 3, 6, 8]
# Count of drops needed on building with  9  floors, 2 eggs: 4  from the floor #s: [1, 3, 6, 9]
# Count of drops needed on building with  10  floors, 2 eggs: 4  from the floor #s: [1, 3, 6, 10]
# Count of drops needed on building with  11  floors, 2 eggs: 5  from the floor #s: [1, 3, 6, 10, 11]
# Count of drops needed on building with  12  floors, 2 eggs: 5  from the floor #s: [1, 3, 6, 10, 12]
# Count of drops needed on building with  13  floors, 2 eggs: 5  from the floor #s: [1, 3, 6, 10, 13]
# Count of drops needed on building with  14  floors, 2 eggs: 5  from the floor #s: [1, 3, 6, 10, 14]
# Count of drops needed on building with  15  floors, 2 eggs: 5  from the floor #s: [1, 3, 6, 10, 15]
# Count of drops needed on building with  16  floors, 2 eggs: 6  from the floor #s: [1, 3, 6, 10, 15, 16]
# Count of drops needed on building with  17  floors, 2 eggs: 6  from the floor #s: [1, 3, 6, 10, 15, 17]
# Count of drops needed on building with  18  floors, 2 eggs: 6  from the floor #s: [1, 3, 6, 10, 15, 18]
# Count of drops needed on building with  19  floors, 2 eggs: 6  from the floor #s: [1, 3, 6, 10, 15, 19]
# Count of drops needed on building with  20  floors, 2 eggs: 6  from the floor #s: [1, 3, 6, 10, 15, 20]
# Count of drops needed on building with  21  floors, 2 eggs: 6  from the floor #s: [1, 3, 6, 10, 15, 21]
# Count of drops needed on building with  22  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 22]
# Count of drops needed on building with  23  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 23]
# Count of drops needed on building with  24  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 24]
# Count of drops needed on building with  25  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 25]
# Count of drops needed on building with  26  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 26]
# Count of drops needed on building with  27  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 27]
# Count of drops needed on building with  28  floors, 2 eggs: 7  from the floor #s: [1, 3, 6, 10, 15, 21, 28]
# Count of drops needed on building with  29  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 29]
# Count of drops needed on building with  30  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 30]
# Count of drops needed on building with  31  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 31]
# Count of drops needed on building with  32  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 32]
# Count of drops needed on building with  33  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 33]
# Count of drops needed on building with  34  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 34]
# Count of drops needed on building with  35  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 35]
# Count of drops needed on building with  36  floors, 2 eggs: 8  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36]
# Count of drops needed on building with  37  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 37]
# Count of drops needed on building with  38  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 38]
# Count of drops needed on building with  39  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 39]
# Count of drops needed on building with  40  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 40]
# Count of drops needed on building with  41  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 41]
# Count of drops needed on building with  42  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 42]
# Count of drops needed on building with  43  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 43]
# Count of drops needed on building with  44  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 44]
# Count of drops needed on building with  45  floors, 2 eggs: 9  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45]
# Count of drops needed on building with  46  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 46]
# Count of drops needed on building with  47  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 47]
# Count of drops needed on building with  48  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 48]
# Count of drops needed on building with  49  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 49]
# Count of drops needed on building with  50  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 50]
# Count of drops needed on building with  51  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 51]
# Count of drops needed on building with  52  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 52]
# Count of drops needed on building with  53  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 53]
# Count of drops needed on building with  54  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 54]
# Count of drops needed on building with  55  floors, 2 eggs: 10  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
# Count of drops needed on building with  56  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 56]
# Count of drops needed on building with  57  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 57]
# Count of drops needed on building with  58  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 58]
# Count of drops needed on building with  59  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 59]
# Count of drops needed on building with  60  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 60]
# Count of drops needed on building with  61  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 61]
# Count of drops needed on building with  62  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 62]
# Count of drops needed on building with  63  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 63]
# Count of drops needed on building with  64  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 64]
# Count of drops needed on building with  65  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 65]
# Count of drops needed on building with  66  floors, 2 eggs: 11  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]
# Count of drops needed on building with  67  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 67]
# Count of drops needed on building with  68  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 68]
# Count of drops needed on building with  69  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 69]
# Count of drops needed on building with  70  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 70]
# Count of drops needed on building with  71  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 71]
# Count of drops needed on building with  72  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 72]
# Count of drops needed on building with  73  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 73]
# Count of drops needed on building with  74  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 74]
# Count of drops needed on building with  75  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 75]
# Count of drops needed on building with  76  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 76]
# Count of drops needed on building with  77  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 77]
# Count of drops needed on building with  78  floors, 2 eggs: 12  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
# Count of drops needed on building with  79  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 79]
# Count of drops needed on building with  80  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 80]
# Count of drops needed on building with  81  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 81]
# Count of drops needed on building with  82  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 82]
# Count of drops needed on building with  83  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 83]
# Count of drops needed on building with  84  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 84]
# Count of drops needed on building with  85  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 85]
# Count of drops needed on building with  86  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 86]
# Count of drops needed on building with  87  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 87]
# Count of drops needed on building with  88  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 88]
# Count of drops needed on building with  89  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 89]
# Count of drops needed on building with  90  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 90]
# Count of drops needed on building with  91  floors, 2 eggs: 13  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
# Count of drops needed on building with  92  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 92]
# Count of drops needed on building with  93  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 93]
# Count of drops needed on building with  94  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 94]
# Count of drops needed on building with  95  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 95]
# Count of drops needed on building with  96  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 96]
# Count of drops needed on building with  97  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 97]
# Count of drops needed on building with  98  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 98]
# Count of drops needed on building with  99  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 99]
# Count of drops needed on building with  100  floors, 2 eggs: 14  from the floor #s: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 100]






























