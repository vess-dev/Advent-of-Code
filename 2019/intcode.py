class Comp:

	mem_tape = []
	mem_pos = 0
	mem_out = []
	mem_base = 0

	flag_halt = False

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
		self.mem_out = []
		self.mem_base = 0
		return

	def prepare(self):
		op_current = str(self.mem_tape[self.mem_pos]).rjust(2, "0")
		op_base = op_current[-2:]
		op_flags = []
		op_data = []
		if op_base != "99":
			op_offset = self.op_ref[op_base][0]
			op_pad = op_current.rjust(op_offset + 1, "0")
			op_flags = list(op_pad[:3][::-1])
			flag_count = range(1, len(op_flags))
			op_data = list(map(self.get, flag_count, op_flags))
			mem_read = (self.mem_pos + op_offset - 1)
			# Position mode.
			if op_flags[-1] == "0":
				op_data.append(self.mem_tape[mem_read])
			# Relative mode.
			elif op_flags[-1] == "2":
				pass
		return (op_base, op_flags, op_data)

	def get(self, input_offset, input_mode):
		match input_mode:
			# Position mode.
			case "0":
				mem_read = (self.mem_pos + input_offset)
				if input_offset != -1:
					return self.mem_tape[self.mem_tape[mem_read]]
				else:
					return self.mem_tape[mem_read]
			# Immediate mode.
			case "1":
				pass
			# Relative mode.
			case "2":
				pass

	def step(self, input_debug=False):
		op_base, op_flags, op_data = self.prepare()
		if input_debug:
			print(self.mem_pos, op_base, op_flags, op_data)
		match op_base:
			case "01": # "01": [4, "add"]
				self.mem_tape[op_data[2]] = op_data[0] + op_data[1]
			case "02": # "02": [4, "mult"]
				self.mem_tape[op_data[2]] = op_data[0] * op_data[1]
			# "03": [2, "input"]
			# "04": [2, "output"]
			# "05": [3, "jump notzero"]
			# "06": [3, "jump zero"]
			# "07": [4, "less than"]
			# "08": [4, "equal to"]
			# "09": [2, "offset"]
			case "99": # "99": [0, "halt"]
				self.flag_halt = True
		self.mem_pos += self.op_ref[op_base][0]
		return

	def run(self, input_debug=False):
		while not self.flag_halt:
			self.step(input_debug)
		return