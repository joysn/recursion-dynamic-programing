# https://www.youtube.com/watch?v=BFKbbE9Tpqs
# Mock interview with a Google engineer: Partition array and public transportation
# R B B B G
# R B G G R
# R B R R G
# Find the color with largest continuous string
# '0R':1 '1B':1 '1B':2, '1B':3
# Recursive dfs
 
def find_longest_cont_color(colors):

	cache = [[0 for c in range(len(colors[0]))] for r in range(len(colors))]
	
	colors_dict = dict()
	key = '0'+'0'+str(colors[0][0])
	colors_dict[key] = 1
	cache[0][0] = (colors_dict[key], key)
	max_size = 1
	max_color = str(colors[0][0])
	
	for c in range(1,len(colors[0])):
		if colors[0][c-1] == colors[0][c]:
			key = cache[0][c-1][1]
			colors_dict[key] += 1
			cache[0][c] = cache[0][c-1]
		else:
			key = '0'+str(c)+str(colors[0][c])
			colors_dict[key] = 1
			cache[0][c] = (colors_dict[key], key)
		if max_size < cache[0][c][0]:
			max_size = cache[0][c][0]
			max_color = colors[0][c]
	
	for r in range(1,len(colors)):
		if colors[r-1][0] == colors[r][0]:
			key = cache[r-1][0][1]
			colors_dict[key] += 1
			cache[r][0] = cache[r-1][0]
		else:
			key = str(r)+'0'+str(colors[0][0])
			colors_dict[key] = 1
			cache[r][0] = (colors_dict[key], key)	
		if max_size < cache[r][0][0]:
			max_size = cache[r][0][0]
			max_color = colors[r][0]
			
	
	for r in range(1,len(colors)):
		for c in range(1,len(colors[0])):
			if colors[r][c] == colors[r-1][c] and colors[r][c] == colors[r][c-1]:
				if cache[r-1][c][0] > cache[r][c-1][0]:
					key = cache[r-1][c][1]
					colors_dict[key] += 1
					cache[r][c] = cache[r-1][c]
				else:
					key = cache[r][c-1][1]
					colors_dict[key] += 1
					cache[r][c] = cache[r][c-1]
					
			elif colors[r][c] == colors[r-1][c]:
				key = cache[r-1][c][1]
				colors_dict[key] += 1
				cache[r][c] = cache[r-1][c]
			elif colors[r][c] == colors[r][c-1]:
				key = cache[r][c-1][1]
				colors_dict[key] += 1
				cache[r][c] = cache[r][c-1]
			else:
				key = str(r)+str(c)+str(colors[r][c])
				colors_dict[key] = 1
				cache[r][c] = (colors_dict[key], key)	
				
			print(colors_dict) if debug else None
			print(r,c,max_size,colors_dict[cache[r][c][1]]) if debug else None
			if max_size < colors_dict[cache[r][c][1]]:
				max_size = colors_dict[cache[r][c][1]]
				max_color = colors[r][c]
			
	print(colors_dict) if debug else None
	
	#k = list(colors_dict.keys())
	#v = list(colors_dict.values())
	#return k[v.index(max(v))][-1:],max(v)
	return max_size, max_color
		

debug = True
debug = False
	
print("#################################")
print("###### Dynamic Programming ######")
print("#################################")
colors = [['R','B','B','B','G'],['R','B','G','G','R'],['R','B','R','R','G']]
print(find_longest_cont_color(colors))
colors = [['R','B','B','B','G'],['R','B','B','G','R'],['R','B','R','R','G']]
print(find_longest_cont_color(colors))


# (base) D:\>python dynamic_longest_strip_color.py
# #################################
# ###### Dynamic Programming ######
# #################################
# (5, 'B')
# (6, 'B')
