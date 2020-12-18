day_num = 18

import copy

file_load = open("input/day18.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = [list(temp_itr.replace(" ", "")) for temp_itr in file_in.split("\n")]
for temp_pos, temp_line in enumerate(file_in):
	file_in[temp_pos] = [int(temp_itr) if temp_itr.isdigit() else temp_itr for temp_itr in temp_line]

def run():

	def opdo(input_one, input_op, input_two):
		if input_op == "+":
			return input_one + input_two
		elif input_op == "-":
			return input_one - input_two
		elif input_op == "*":
			return input_one * input_two

	def comp(input_in, input_ord):
		while len(input_in) != 1:
			if input_ord:
				if "+" in input_in:
					plus_pos = input_in.index("+")
					input_in[plus_pos - 1] = opdo(input_in[plus_pos - 1], input_in[plus_pos], input_in[plus_pos + 1])
					input_in.pop(plus_pos)
					input_in.pop(plus_pos)
				elif "+" not in input_in:
					input_ord = False
			elif not input_ord:
				input_in[0] = opdo(input_in[0], input_in[1], input_in[2])
				input_in.pop(1)
				input_in.pop(1)
		return input_in[0]

	def maff(input_in, input_ord):
		input_new = copy.deepcopy(input_in)
		line_itr = 0
		stack_maff = []
		while line_itr != len(input_new):
			line_curr = input_new[line_itr]
			line_pos = 0
			while line_pos != len(line_curr):
				if "(" in line_curr:
					temp_stack = []
					if line_curr[line_pos] == ")":
						line_par = line_pos
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
					stack_maff.append(comp(line_curr, input_ord))
					break
			line_itr += 1
		return sum(stack_maff)

	return maff(file_in, False), maff(file_in, True)

print(run())