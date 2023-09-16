from collections import deque
import intcode

day_num = 15

file_load = open("input/day15.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def crawl(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		map_grid = {}
		map_x, map_y = 0, 0
		map_grid[(map_x, map_y)] = 1
		wall_hand = [
			(1, 4, [1, 0]),
			(4, 2, [0, 1]),
			(2, 3, [-1, 0]),
			(3, 1, [0, -1])
		]
		wall_cycle = deque(wall_hand)
		map_oxy = False
		while True:
			comp_main.run([1])
			comp_status = comp_main.mem_output.pop(0)
			if comp_status == 0:
				break
		while not map_oxy:
			wall_dir = wall_cycle[0]
			while True:
				comp_main.run([wall_dir[0]])
				comp_status = comp_main.mem_output.pop(0)
				if comp_status == 1:
					wall_cycle.rotate(-1)
					break
				elif comp_status == 2:
					map_oxy = True
					break
				comp_main.run([wall_dir[1]])
				comp_status = comp_main.mem_output.pop(0)
				if comp_status == 0:
					wall_cycle.rotate(1)
					break
				elif comp_status == 2:
					map_oxy = True
					break
				map_x += wall_dir[2][0]
				map_y += wall_dir[2][1]
				map_grid[(map_x, map_y)] = "1"
		print(len(map_grid))
		return

	return crawl(file_in)

if __name__ == "__main__":
	print(run())