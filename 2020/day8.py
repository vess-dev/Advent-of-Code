day_num = 8

file_load = open("input/input8.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = file_in.split("\n")

def run():

	def boy(input_in):
		state_acc = 0
		state_pos = 0
		state_visit = []
		while True:
			if state_pos in state_visit:
				return state_acc, False
			elif state_pos == len(input_in):
				return state_acc, True
			else:
				state_visit.append(state_pos)
			if input_in[state_pos].startswith("nop"):
				state_pos += 1
			elif input_in[state_pos].startswith("acc"):
				state_acc += int(input_in[state_pos].split(" ")[1])
				state_pos += 1
			elif input_in[state_pos].startswith("jmp"):
				state_pos += int(input_in[state_pos].split(" ")[1])

	def loop(input_in):
		state_acc, temp_truth = boy(input_in)
		return state_acc

	def halt(input_in):
		check_pos = 0
		while True:
			while not (input_in[check_pos][:3] in ["jmp", "nop"]):
				check_pos += 1
			if input_in[check_pos][:3] == "jmp":
				input_in[check_pos] = "nop " + input_in[check_pos].split(" ")[1]
			elif input_in[check_pos][:3] == "nop":
				input_in[check_pos] = "jmp " + input_in[check_pos].split(" ")[1]
			state_acc, state_truth = boy(input_in)
			if state_truth:
				return state_acc
			if input_in[check_pos][:3] == "jmp":
				input_in[check_pos] = "nop " + input_in[check_pos].split(" ")[1]
			elif input_in[check_pos][:3] == "nop":
				input_in[check_pos] = "jmp " + input_in[check_pos].split(" ")[1]
			check_pos += 1

	return loop(file_in), halt(file_in)