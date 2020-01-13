# String interleaving
# 2 string a = xyz and b = abcd is said to be interleaving c = xabycxd
	

def is_interleaving(stra,strb,strc):
	print(stra,len(stra),strb,len(strb),strc,len(strc)) if debug else None
	
	if (stra == "") and (strb == "") and (strc == ""):
		return True
		
	if (stra == "") and (strb == ""):
		return False
		
	if (strc == "") and (strb == "" or strc == ""):
		return False
		
		
	a = False
	b = False
	
	if len(stra) > 0:
		if stra[0] == strc[0]:
			a = is_interleaving(stra[1:],strb,strc[1:])
	
	if len(strb) > 0:
		if strb[0] == strc[0]:
			b = is_interleaving(stra,strb[1:],strc[1:])
		
	return (a or b)
	
debug = False
print("##########################")
print("### Recursive Solution ###")
print("##########################")
print("Is interleaving 'x','a','xa'", is_interleaving('x','a','xa'))
print("Is interleaving 'xyz','abcd','xabyczd'", is_interleaving('xyz','abcd','xabyczd'))
print("Is interleaving 'xyz','abcd','xabyczde'",is_interleaving('xyz','abcd','xabyczde'))
print("Is interleaving 'x','abcd','axbcd'",is_interleaving('x','abcd','axbcd'))
print("Is interleaving 'bcc','bbca','bbcbcac'",is_interleaving('bcc','bbca','bbcbcac'))
print("Is interleaving 'bcc','bbca','bbcbcaz'",is_interleaving('bcc','bbca','bbcbcaz'))

def is_interleaving(stra,strb,strc):
	
	if len(strc) != len(stra) + len(strb):
		return False
		
	intl = [[False for i in range(len(strb)+1)] for j in range(len(stra)+1)]

	intl[0][0] = True
	
	for c in range(1,len(strb)+1):
		if strb[c-1] == strc[c-1]:
			intl[0][c] = intl[0][c-1]
		else:
			intl[0][c] = False
			
			
	for r in range(1,len(stra)+1):
		if stra[r-1] == strc[r-1]:
			intl[r][0] = intl[r-1][0]
		else:
			intl[r][0] = False
			
	
	for r in range(1,len(stra)+1):
		for c in range(1,len(strb)+1):
			if (strc[r+c-1] == strb[c-1]) and (strc[r+c-1] != stra[r-1]):
				intl[r][c] = intl[r][c-1]
			elif (strc[r+c-1] == stra[r-1]) and (strc[r+c-1] != strb[c-1]):
				intl[r][c] = intl[r-1][c]
			elif (strc[r+c-1] == strb[c-1]) and (strc[r+c-1] == stra[r-1]):
				intl[r][c] = intl[r][c-1] or intl[r-1][c]
				
	return intl[len(stra)][len(strb)]
				
	
	
print("###################")
print("### DP Solution ###")
print("###################")

print("Is interleaving 'x','a','xa'", is_interleaving('x','a','xa'))
print("Is interleaving 'xyz','abcd','xabyczd'", is_interleaving('xyz','abcd','xabyczd'))
print("Is interleaving 'xyz','abcd','xabyczde'",is_interleaving('xyz','abcd','xabyczde'))
print("Is interleaving 'x','abcd','axbcd'",is_interleaving('x','abcd','axbcd'))
print("Is interleaving 'bcc','bbca','bbcbcac'",is_interleaving('bcc','bbca','bbcbcac'))
print("Is interleaving 'bcc','bbca','bbcbcaz'",is_interleaving('bcc','bbca','bbcbcaz'))



# (base) D:\>python dynamic_interleaved_strings.py
# ##########################
# ### Recursive Solution ###
# ##########################
# Is interleaving 'x','a','xa' True
# Is interleaving 'xyz','abcd','xabyczd' True
# Is interleaving 'xyz','abcd','xabyczde' False
# Is interleaving 'x','abcd','axbcd' True
# Is interleaving 'bcc','bbca','bbcbcac' True
# Is interleaving 'bcc','bbca','bbcbcaz' False
# ###################
# ### DP Solution ###
# ###################
# Is interleaving 'x','a','xa' True
# Is interleaving 'xyz','abcd','xabyczd' True
# Is interleaving 'xyz','abcd','xabyczde' False
# Is interleaving 'x','abcd','axbcd' True
# Is interleaving 'bcc','bbca','bbcbcac' True
# Is interleaving 'bcc','bbca','bbcbcaz' False


		