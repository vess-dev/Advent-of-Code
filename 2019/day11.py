import intcode

day_num = 11

file_load = open("input/day11.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = {}
file_prep = list(map(int, file_prep.split(",")))
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def painter(input_in, input_grid):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		paint_grid = input_grid.copy()
		paint_x, paint_y = 0, 0
		paint_angle = 0
		comp_main.run()
		while not comp_main.flag_halt:
			paint_status = paint_grid.get((paint_x, paint_y), None)
			if paint_status == None:
				paint_grid[(paint_x, paint_y)] = 0
				paint_status = 0
			comp_main.run([paint_status])
			comp_paint = comp_main.mem_output.pop(0)
			comp_turn = comp_main.mem_output.pop(0)
			paint_grid[(paint_x, paint_y)] = comp_paint
			match comp_turn:
				case 0:
					paint_angle = (paint_angle - 90) % 360
				case 1:
					paint_angle = (paint_angle + 90) % 360
			match paint_angle:
				case 0: paint_y -= 1
				case 90: paint_x += 1
				case 180: paint_y += 1
				case 270: paint_x -= 1
		return paint_grid

	def paint(input_in):
		paint_grid = painter(input_in, {})
		return len(paint_grid)

	def picture(input_in):
		paint_grid = painter(input_in, {(0, 0):1})
		max_x, max_y, min_x, min_y = 0, 0, 0, 0
		for temp_pair in paint_grid.keys():
			if temp_pair[0] < min_x: min_x = temp_pair[0]
			elif temp_pair[0] > max_x: max_x = temp_pair[0]
			if temp_pair[1] < min_y: min_y = temp_pair[1]
			elif temp_pair[1] > max_y: max_y = temp_pair[1]
		pos_x, pos_y = min_x, min_y
		paint_final = []
		for temp_y in range(max_y - min_y + 1):
			paint_line = []
			for temp_x in range(max_x - min_x + 1):
				paint_color = paint_grid.get((temp_x, temp_y), 0)
				paint_line.append(paint_color)
			paint_final.append(paint_line)
		paint_picture = ""
		for temp_line in paint_final:
			line_string = list(map(str, temp_line))
			paint_picture += "".join(line_string) + "\n"
		paint_picture = paint_picture.replace("0", " ")
		print(paint_picture)
		return

	return paint(file_in), picture(file_in)

if __name__ == "__main__":
	print(run())