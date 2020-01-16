# String interleaving
# 2 string a = xyz and b = abcd is said to be interleaving c = xabycxd
# condition - both string are different, find a solution with Time - O(n+m) and  Space - O(1)

def is_interleaving(stra,strb,strc):
	if len(strc) != len(stra) + len(strb):
		return False
		
	idxa = 0
	idxb = 0
	for i in range(len(strc)):
		if idxa == -1 and idxb == -1:
			return False
		if strc[i] == stra[idxa]:
			if idxa < len(stra)-1:
				idxa += 1
			else:
				idxa = -1
		elif strc[i] == strb[idxb]:
			if idxb < len(strb) -1:
				idxb += 1
			else:
				idxb = -1
		else:
			return False
	
	if idxa == -1 and idxb == -1:	
		return True
	else:
		return False
	
print("###################")
print("### DP Solution ###")
print("###################")

print("Is interleaving 'x','a','xa'", is_interleaving('x','a','xa'))
print("Is interleaving 'xyz','abcd','xabyczd'", is_interleaving('xyz','abcd','xabyczd'))
print("Is interleaving 'xyz','abcd','xabyczde'",is_interleaving('xyz','abcd','xabyczde'))
print("Is interleaving 'x','abcd','axbcd'",is_interleaving('x','abcd','axbcd'))
print("Is interleaving 'xy','abcd','axbcd'",is_interleaving('xy','abcd','axbcd'))
print("Is interleaving 'xy','ab','axcd'",is_interleaving('xy','ab','axcd'))
		