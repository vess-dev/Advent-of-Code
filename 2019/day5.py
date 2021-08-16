day_num = 5


file_load = open("input/day5.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def comp(input_in):
		mem_tape = input_in.copy()
		mem_pos = 0
		while True:
			mem_split = list(map(int, list(str(mem_tape[mem_pos]))))
			mem_split[-2] = mem_split[-2] * 10 + mem_split[-1]
			mem_split.pop(-1)
			mem_com = []
			op_pad = {1:4, 2:4, 3:1, 4:1}
			while len(mem_split) != op_pad[mem_split[-1]]:
				mem_split.insert(0, 0)
			for mem_mode in mem_split[::-1][1:]:
				com_pos = 1
				if mem_mode == 0:
					mem_com.append("mem_tape[mem_tape + ]")
			quit()
			"""
			if mem_split[-1] ==  1:
				mem_tape[mem_tape[mem_pos + 3]] = mem_tape[mem_tape[mem_pos + 1]] + mem_tape[mem_tape[mem_pos + 2]]
				mem_pos += 4
			elif mem_split[-1] ==  2:
				mem_tape[mem_tape[mem_pos + 3]] = mem_tape[mem_tape[mem_pos + 1]] * mem_tape[mem_tape[mem_pos + 2]]
				mem_pos += 4
			elif mem_split[-1] ==  3:
				mem_input = int(input("1#: "))
				mem_tape[mem_tape[mem_pos + 1]] = mem_input
				mem_pos += 2
			elif mem_split[-1] ==  4:
				print("> " + str(mem_tape[mem_tape[mem_pos + 1]]))
				mem_pos += 2
			elif mem_split[-1] ==  99:
				break"""
		return mem_tape

	def diag(input_in):
		return comp(input_in)

	return diag(file_in)

print(run())