day_num = 5

file_load = open("input/day5.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def op(input_in, input_mod, input_val):
		if input_mod == "0":
			return input_in[input_val]
		elif input_mod == "1":
			return input_val

	def comp(input_in, input_code):
		mem_tape = input_in.copy()
		mem_pos = 0
		mem_stdout = ""
		while True:
			com_full = str(mem_tape[mem_pos])
			while len(com_full) != 5:
				com_full = "0" + com_full
			com_mode = com_full[:-2][::-1]
			com_op = int(com_full[-2:])
			if com_op == 1:
				mem_tape[mem_tape[mem_pos + 3]] = op(mem_tape, com_mode[0], mem_tape[mem_pos + 1]) + op(mem_tape, com_mode[1], mem_tape[mem_pos + 2])
				mem_pos += 4
			elif com_op == 2:
				mem_tape[mem_tape[mem_pos + 3]] = op(mem_tape, com_mode[0], mem_tape[mem_pos + 1]) * op(mem_tape, com_mode[1], mem_tape[mem_pos + 2])
				mem_pos += 4
			elif com_op == 3:
				mem_tape[mem_tape[mem_pos + 1]] = input_code
				mem_pos += 2
			elif com_op == 4:
				mem_stdout = mem_stdout + str(op(mem_tape, com_mode[0], mem_tape[mem_pos + 1])) + " "
				mem_pos += 2
			elif com_op == 5:
				if op(mem_tape, com_mode[0], mem_tape[mem_pos + 1]) != 0:
					mem_pos = op(mem_tape, com_mode[1], mem_tape[mem_pos + 2])
				else:
					mem_pos += 3
			elif com_op == 6:
				if op(mem_tape, com_mode[0], mem_tape[mem_pos + 1]) == 0:
					mem_pos = op(mem_tape, com_mode[1], mem_tape[mem_pos + 2])
				else:
					mem_pos += 3
			elif com_op == 7:
				if op(mem_tape, com_mode[0], mem_tape[mem_pos + 1]) < op(mem_tape, com_mode[1], mem_tape[mem_pos + 2]):
					mem_tape[mem_tape[mem_pos + 3]] = 1
				else:
					mem_tape[mem_tape[mem_pos + 3]] = 0
				mem_pos += 4
			elif com_op == 8:
				if op(mem_tape, com_mode[0], mem_tape[mem_pos + 1]) == op(mem_tape, com_mode[1], mem_tape[mem_pos + 2]):
					mem_tape[mem_tape[mem_pos + 3]] = 1
				else:
					mem_tape[mem_tape[mem_pos + 3]] = 0
				mem_pos += 4
			elif com_op == 99:
				break
		return mem_stdout[:-1]

	def diag(input_in):
		comp_result = comp(input_in, 1)
		comp_result = comp_result.split(" ")
		return comp_result[-1]

	def test(input_in):
		comp_result = comp(input_in, 5)
		return comp_result

	return diag(file_in), test(file_in)

if __name__ == "__main__":
	print(run())