# Empty plot 2 * n (n is the input)
# Fill the plot with tiles of size 2 * 1
# Find the number of such ways to cover the plot


tileWidth = 1
tileHeight = 2
def no_of_ways_to_fill_plot(width):
	print("Called with Breadth is:",width) if debug else None
	if width == 0:
		return 1
	if width == 1:
		return 1
		
	no_of_ways = 0
	# print("1. Calling with Breadth is:",width-tileWidth)  if debug else None
	# no_of_ways += no_of_ways_to_fill_plot(width-tileWidth)
	# print("2. Calling with Breadth is:",width-tileHeight)  if debug else None
	# no_of_ways += no_of_ways_to_fill_plot(width-tileHeight)
	no_of_ways = no_of_ways_to_fill_plot(width-tileWidth) + no_of_ways_to_fill_plot(width-tileHeight)
	return no_of_ways


debug = False
print("############# Using recursion (2 * n) #############")
print("No of ways to fill plot of size 2 * 1 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(1))
print("No of ways to fill plot of size 2 * 2 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(2))
print("No of ways to fill plot of size 2 * 3 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(3))
print("No of ways to fill plot of size 2 * 4 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(4))
print("No of ways to fill plot of size 2 * 5 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(5))

tileWidth = 1
tileHeight = 2
def no_of_ways_to_fill_plot(plotWidth):
	
	if plotWidth == 0:
		return 0
	if plotWidth == tileWidth:
		return tileWidth
	if plotWidth == tileHeight:
		return tileHeight
		
	a = tileWidth
	b = tileHeight
	no_of_ways = 0
	for i in range(3,plotWidth+1):
		no_of_ways = a + b
		a = b
		b = no_of_ways
	return no_of_ways


print("############# Using DP (2 * n) #############")
print("No of ways to fill plot of size 2 * 1 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(1))
print("No of ways to fill plot of size 2 * 2 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(2))
print("No of ways to fill plot of size 2 * 3 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(3))
print("No of ways to fill plot of size 2 * 4 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(4))
print("No of ways to fill plot of size 2 * 5 by tiles of size 2 * 1 is: ",no_of_ways_to_fill_plot(5))


## Plot Height is now = 3, i.e. plot is of size 3 * n

tileHeight = 2
tileWidth = 1

# Only even width can be fiiled,
def no_of_ways_to_fill_plot(plotWidth):
	if plotWidth == 0:
		return 0
	if plotWidth%2 != 0:
		return 0
	if plotWidth == 2:
		return 2
	if plotWidth == 4:
		return 6
		
	a = 2
	b = 6
	no_of_ways = 0
	for i in range(6,plotWidth+1,2):
		no_of_ways = a * b
		b = no_of_ways
		
	return no_of_ways
	

print("############# Using DP (3 * n) #############")
print("No of ways to fill plot of size 2 * 1 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(1))
print("No of ways to fill plot of size 2 * 2 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(2))
print("No of ways to fill plot of size 2 * 3 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(3))
print("No of ways to fill plot of size 2 * 4 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(4))
print("No of ways to fill plot of size 2 * 5 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(5))
print("No of ways to fill plot of size 2 * 6 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(6))
print("No of ways to fill plot of size 2 * 12 by tiles of size 3 * 1 is: ",no_of_ways_to_fill_plot(12))


# (base) D:\>python dynamic_fill_plot.py
# ############# Using recursion (2 * n) #############
# No of ways to fill plot of size 2 * 1 by tiles of size 2 * 1 is:  1
# No of ways to fill plot of size 2 * 2 by tiles of size 2 * 1 is:  2
# No of ways to fill plot of size 2 * 3 by tiles of size 2 * 1 is:  3
# No of ways to fill plot of size 2 * 4 by tiles of size 2 * 1 is:  5
# No of ways to fill plot of size 2 * 5 by tiles of size 2 * 1 is:  8
# ############# Using DP (2 * n) #############
# No of ways to fill plot of size 2 * 1 by tiles of size 2 * 1 is:  1
# No of ways to fill plot of size 2 * 2 by tiles of size 2 * 1 is:  2
# No of ways to fill plot of size 2 * 3 by tiles of size 2 * 1 is:  3
# No of ways to fill plot of size 2 * 4 by tiles of size 2 * 1 is:  5
# No of ways to fill plot of size 2 * 5 by tiles of size 2 * 1 is:  8
# ############# Using DP (3 * n) #############
# No of ways to fill plot of size 2 * 1 by tiles of size 3 * 1 is:  0
# No of ways to fill plot of size 2 * 2 by tiles of size 3 * 1 is:  2
# No of ways to fill plot of size 2 * 3 by tiles of size 3 * 1 is:  0
# No of ways to fill plot of size 2 * 4 by tiles of size 3 * 1 is:  6
# No of ways to fill plot of size 2 * 5 by tiles of size 3 * 1 is:  0
# No of ways to fill plot of size 2 * 6 by tiles of size 3 * 1 is:  12
# No of ways to fill plot of size 2 * 12 by tiles of size 3 * 1 is:  96