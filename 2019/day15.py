import copy
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
		
	ROB_MOVES = {
		1: (0, -1),
		2: (0,  1),
		3: (-1, 0),
		4: (1,  0),
	}

	def test(input_in, input_move):
		rob_copy = copy.deepcopy(input_in)
		rob_copy.run([input_move])
		return rob_copy, rob_copy.status()

	def crawl(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		rob_pos = (0, 0)
		rob_tried = {}
		rob_alive = {}
		rob_tried[rob_pos] = True
		rob_alive[rob_pos] = [copy.deepcopy(comp_main), rob_pos, 0]
		while True:
			for (temp_robkey, temp_robdata) in list(rob_alive.items()):
				for (temp_key, temp_value) in ROB_MOVES.items():
					rob_new = (temp_robdata[1][0] + temp_value[0], temp_robdata[1][1] + temp_value[1])
					if rob_new not in rob_tried:
						rob_double, rob_status = test(temp_robdata[0], temp_key)
						if rob_status == 1:
							rob_alive[rob_new] = [rob_double, rob_new, temp_robdata[2] + 1]
						elif rob_status == 2:
							return rob_double, temp_robdata[2] + 1
						rob_tried[rob_new] = True		
				rob_alive.pop(temp_robkey, None)
		return None, None
	
	def control(input_in):
		rob_oxy, rob_dist = crawl(input_in)
		rob_pos = (0, 0)
		rob_tried = {}
		rob_alive = {}
		rob_tried[rob_pos] = True
		rob_alive[rob_pos] = [copy.deepcopy(rob_oxy), rob_pos, 0]
		rob_clock = 0
		while rob_alive:
			for (temp_robkey, temp_robdata) in list(rob_alive.items()):
				for (temp_key, temp_value) in ROB_MOVES.items():
					rob_new = (temp_robdata[1][0] + temp_value[0], temp_robdata[1][1] + temp_value[1])
					if rob_new not in rob_tried:
						rob_double, rob_status = test(temp_robdata[0], temp_key)
						if rob_status == 1:
							rob_alive[rob_new] = [rob_double, rob_new, temp_robdata[2] + 1]
						rob_tried[rob_new] = True		
				rob_alive.pop(temp_robkey, None)
			rob_clock += 1
		return rob_dist, rob_clock - 1

	return control(file_in)

if __name__ == "__main__":
	print(run())