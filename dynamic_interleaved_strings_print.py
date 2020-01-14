# given 2 strings, print all the interleavings of the string
# e.g INPUT AB XY
# OUTPUT ABXY AXBY AXYB XABY XAYB XYAB

## Recusrive Solution ##
########################

def printInterleavings(str1,str2,ostr,i,output):

	if len(str1) == 0 and len(str2) == 0:
		output.add("".join(ostr))
		
	if len(str1) != 0:
		ostr[i] = str1[0]
		printInterleavings(str1[1:],str2,ostr,i+1,output)
		
	if len(str2) != 0:
		ostr[i] = str2[0]
		printInterleavings(str1,str2[1:],ostr,i+1,output)
		
def printInterleavingsHelper(str1,str2):
	output = set()
	ostr = ['']*(len(str1)+len(str2))
	
	printInterleavings(str1,str2,ostr,0,output)
	
	return output
	
	

print("## Recusrive Solution ##")
print("'AB' & 'XY' :- ",printInterleavingsHelper('AB','XY'))
print("'AB' & 'AB' :- ",printInterleavingsHelper('AB','AB'))


# def printInterleavings(str1,str2):

	# if len(str1) == 0 and len(str2) == 0:
		# return ""
	
	# if len(str1) == 0:
		# return str2
	
	# if len(str2) == 0:
		# return str3
		
	# cache
	