import intcode
import random

day_num = 13

file_load = open("input/day13.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def score(input_in):
		index_score = input_in.index(-1)
		return input_in[index_score + 2]

	def blocks(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()
		block_count = 0
		for temp_itr in range(2, len(comp_main.mem_output), 3):
			if comp_main.mem_output[temp_itr] == 2:
				block_count += 1
		return block_count

	def play(input_in):
		tape_mem = input_in.copy()
		tape_mem[0] = 2
		comp_main = intcode.Comp()
		score_current = 0
		joystick_list = [-1, 0, 1]
		while score_current == 0:
			comp_main.load(tape_mem.copy())
			while not comp_main.flag_halt:
				comp_main.mem_output.clear()
				joystick_choice = random.choice(joystick_list)
				comp_main.run([joystick_choice])
			score_current = score(comp_main.mem_output)
			print(score_current)
		return score_current

	return blocks(file_in), play(file_in)

if __name__ == "__main__":
	print(run())