day_num = 18

import copy

file_load = open("input/day18.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = [list(temp_itr.replace(" ", "")) for temp_itr in file_in.split("\n")]
for temp_pos, temp_line in enumerate(file_in):
	file_in[temp_pos] = [int(temp_itr) if temp_itr.isdigit() else temp_itr for temp_itr in temp_line]

def run():

	def opdo(input_in):
		if input_in[1] == "+": return input_in[0] + input_in[2]
		elif input_in[1] == "-": return input_in[0] - input_in[2]
		elif input_in[1] == "*": return input_in[0] * input_in[2]

	def comp(input_in, input_ord):
		while len(input_in) != 1:
			plus_pos = 1
			if input_ord and "+" in input_in:
				plus_pos = input_in.index("+")
			input_in[plus_pos - 1] = opdo(input_in[plus_pos - 1:plus_pos + 2])
			input_in.pop(plus_pos)
			input_in.pop(plus_pos)
		return input_in[0]

	def maff(input_in, input_ord):
		input_new, line_itr = copy.deepcopy(input_in), 0
		while line_itr != len(input_new):
			line_curr, line_pos = input_new[line_itr], 0
			while line_pos != len(line_curr):
				if "(" in line_curr:
					temp_stack = []
					if line_curr[line_pos] == ")":
						while line_curr[line_pos] != "(":
							line_pos -= 1
						line_curr.pop(line_pos)
						while line_curr[line_pos] != ")":
							temp_stack.append(line_curr[line_pos])
							line_curr.pop(line_pos)
						line_curr.pop(line_pos)
						line_curr.insert(line_pos, comp(temp_stack, input_ord))
						line_pos = 0
					else:
						line_pos += 1
				else:
					input_new[line_itr] = comp(line_curr, input_ord)
					break
			line_itr += 1
		return sum(input_new)

	return maff(file_in, False), maff(file_in, True)