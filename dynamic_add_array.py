# Given array of integers, write recursive code to add sum of all previous numbers to each index of the array
# eg
# I/p - 1 2 3 4 5 6
# O/p - 1 3 6 10 15 21

def add_prev(iarr,pos):
	if pos == 0:
		return iarr[pos]
	else:
		return iarr[pos]+add_prev(iarr,pos-1)
		
		
def add_prev_helper(iarr):
	oarr = list()
	for i in range(0,len(iarr)):
		o = add_prev(iarr,i)
		print(i,o) if debug else None
		oarr.append(o)
	return oarr
		

debug = False		
iarr = [1,2,3,4,5,6]
oarr = add_prev_helper(iarr)
print("Array Input",iarr)
print("Array output",oarr)

# (base) D:\>python dynamic_add_array.py
# Array Input [1, 2, 3, 4, 5, 6]
# Array output [1, 3, 6, 10, 15, 21]




