import pprint

class Comp:

	op_ref = {
		"01": [4, "add"],
		"02": [4, "mult"],
		"03": [2, "input"],
		"04": [2, "output"],
		"05": [3, "jump notzero"],
		"06": [3, "jump ifzero"],
		"07": [4, "less than"],
		"08": [4, "equal to"],
		"09": [2, "offset"],
		"99": [0, "halt"],
	}

	def load(self, input_tape):
		self.mem_tape = input_tape
		self.mem_pos = 0
		self.mem_output = []
		self.mem_base = 0
		self.flag_halt = False
		self.flag_input = False
		self.flag_payload = None
		return

	def prepare(self):
		op_current = str(self.mem_tape[self.mem_pos]).rjust(2, "0")
		op_base = op_current[-2:]
		op_flags = []
		op_data = []
		op_pairs = []
		if op_base != "99":
			op_offset = self.op_ref[op_base][0]
			op_pad = op_current.rjust(op_offset + 1, "0")
			op_flags = list(op_pad[:op_offset - 1][::-1])
			flag_count = list(range(1, len(op_flags) + 1))
			op_data = [self.mem_tape[self.mem_pos + temp_itr] for temp_itr in flag_count]
			op_pairs = list(zip(op_flags, op_data))
		return (op_base, op_pairs)

	def debug(self, input_base, input_pairs):
		print(f"| Position: {self.mem_pos} | Opcode: {input_base} | Pairs: {input_pairs} |")
		print(f"| Pointer: {self.mem_pos} | Offset: {self.mem_base} | Output: {self.mem_output} |")
		print("| Tape:", self.mem_tape, "|", end="\n\n")
		return

	def get(self, input_pair):
		match input_pair[0]:
			case "0": # Position mode.
				test_get = self.mem_tape.get(input_pair[1], None)
				if test_get == None:
					self.mem_tape[input_pair[1]] = 0
					return 0
				return test_get
			case "1": # Immediate mode.
				return input_pair[1]
			case "2": # Relative mode.
				return self.mem_tape[self.mem_base + input_pair[1]]
		return

	def set(self, input_pair, input_data):
		match input_pair[0]:
			case "0": # Position mode.
				self.mem_tape[input_pair[1]] = input_data
			case "2": # Relative mode.
				self.mem_tape[self.mem_base + input_pair[1]] = input_data
		return

	def step(self, input_debug=False):
		op_base, op_pairs = self.prepare()
		if input_debug:
			self.debug(op_base, op_pairs)
		match op_base:
			case "01": # "01": [4, "add"]
				self.set(op_pairs[2], self.get(op_pairs[0]) + self.get(op_pairs[1]))
			case "02": # "02": [4, "mult"]
				self.set(op_pairs[2], self.get(op_pairs[0]) * self.get(op_pairs[1]))
			case "03": # "03": [2, "input"]
				if self.flag_input:
					self.flag_input = False
					self.set(op_pairs[0], self.flag_payload)
					self.flag_payload = None
				else:
					self.flag_input = True
					return
			case "04": # "04": [2, "output"]
				self.mem_output.append(self.get(op_pairs[0]))
			case "05": # "05": [3, "jump notzero"]
				if self.get(op_pairs[0]) != 0:
					self.mem_pos = self.get(op_pairs[1])
					return
			case "06": # "06": [3, "jump zero"]
				if self.get(op_pairs[0]) == 0:
					self.mem_pos = self.get(op_pairs[1])
					return
			case "07": # "07": [4, "less than"]
				if self.get(op_pairs[0]) < self.get(op_pairs[1]):
					self.set(op_pairs[2], 1)
				else:
					self.set(op_pairs[2], 0)
			case "08": # "08": [4, "equal to"]
				if self.get(op_pairs[0]) == self.get(op_pairs[1]):
					self.set(op_pairs[2], 1)
				else:
					self.set(op_pairs[2], 0)
			case "09": # "09": [2, "offset"]
				self.mem_base += self.get(op_pairs[0])
			case "99": # "99": [0, "halt"]
				self.flag_halt = True
		self.mem_pos += self.op_ref[op_base][0]
		return

	def status(self):
		if self.mem_output:
			return self.mem_output[-1]
		return

	def run(self, input_sim=[], input_debug=False):
		while not self.flag_halt:
			if self.flag_input:
				if input_sim:
					self.flag_payload = input_sim.pop(0)
				else:
					break
			self.step(input_debug)
		return self.status()