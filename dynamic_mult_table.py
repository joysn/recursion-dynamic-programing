# print table of n as recirsive function



def mult(n,i):
	if i <= 0 or i > 10:
		return
	if i >= 1 or i <= 10:
		print(n," * ",i," = ",n*i)
		mult(n,i+1)
		
mult(2,1)
mult(17,1)

# (base) D:\>python dynamic_mult_table.py
# 2  *  1  =  2
# 2  *  2  =  4
# 2  *  3  =  6
# 2  *  4  =  8
# 2  *  5  =  10
# 2  *  6  =  12
# 2  *  7  =  14
# 2  *  8  =  16
# 2  *  9  =  18
# 2  *  10  =  20
# 17  *  1  =  17
# 17  *  2  =  34
# 17  *  3  =  51
# 17  *  4  =  68
# 17  *  5  =  85
# 17  *  6  =  102
# 17  *  7  =  119
# 17  *  8  =  136
# 17  *  9  =  153
# 17  *  10  =  170