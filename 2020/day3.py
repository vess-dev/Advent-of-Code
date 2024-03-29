day_num = 3

file_load = open("input/day3.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = file_in.split("\n")

def run():

	def slide(map_curr, slide_right, slide_down):
		pos_x, pos_y = 0, 0
		tree_count = 0
		map_length = len(map_curr)
		map_width = len(map_curr[0])
		while(pos_y <= map_length):
			if map_curr[pos_y][pos_x] == "#":
				tree_count += 1
			pos_x += slide_right
			pos_y += slide_down
			if pos_y >= map_length:
				return tree_count
			pos_x %= map_width
		return tree_count

	def hills():
		slope_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
		slope_total = 1
		for slope_right, slope_down in slope_list:
			slope_total *= slide(file_in, slope_right, slope_down)
		return slope_total

	return slide(file_in, 3, 1), hills()

if __name__ == "__main__":
	print(run())