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
		print(str(self.mem_tape[self.mem_pos]))
		op_current = str(self.mem_tape[self.mem_pos]).rjust(2, "0")
		op_base = op_current[-2:]
		op_flags = []
		op_data = []
		if op_base != "99":
			op_offset = self.op_ref[op_base][0]
			op_pad = op_current.rjust(op_offset + 1, "0")
			op_flags = list(op_pad[:op_offset - 1][::-1])
			flag_count = range(1, len(op_flags))
			op_data = list(map(self.get, flag_count, op_flags))
			mem_read = (self.mem_pos + op_offset - 1)
			match op_flags[-1]:
				# Position mode.
				case "0":
					op_data.append(self.mem_tape[mem_read])
				case "1":
					op_data.append(self.mem_tape[mem_read])
				# Relative mode.
				case "2":
					op_data.append(self.mem_tape[mem_read] + self.mem_base)
		return (op_base, op_flags, op_data)

	def get(self, input_offset, input_mode):
		match input_mode:
			# Position mode.
			case "0":
				mem_read = (self.mem_pos + input_offset)
				return self.mem_tape[self.mem_tape[mem_read]]
			# Immediate mode.
			case "1":
				mem_read = (self.mem_pos + input_offset)
				return self.mem_tape[mem_read]
			# Relative mode.
			case "2":
				pass

	def debug(self, input_base, input_flags, input_data):
		print(f"| Position: {self.mem_pos} | Opcode: {input_base} | Flags: {input_flags} | Data: {input_data} |")
		print("| Pointer:", self.mem_pos, end=" ")
		print("| Offset:", self.mem_base, end=" ")
		print("| Output:", self.mem_output, end=" |\n")
		print("| Tape:", self.mem_tape, "|", end="\n\n")
		return

	def step(self, input_debug=False):
		op_base, op_flags, op_data = self.prepare()
		if input_debug:
			self.debug(op_base, op_flags, op_data)
		match op_base:
			case "01": # "01": [4, "add"]
				self.mem_tape[op_data[2]] = op_data[0] + op_data[1]
			case "02": # "02": [4, "mult"]
				self.mem_tape[op_data[2]] = op_data[0] * op_data[1]
			case "03": # "03": [2, "input"]
				if self.flag_input:
					self.flag_input = False
					self.mem_tape[op_data[0]] = self.flag_payload
					self.flag_payload = None
				else:
					self.flag_input = True
					return
			case "04": # "04": [2, "output"]
				if op_flags[0] == "1":
					self.mem_output.append(op_data[0])
				else:
					self.mem_output.append(self.mem_tape[op_data[0]])
			case "05": # "05": [3, "jump notzero"]
				if op_data[0] != 0:
					if op_flags[1] == "1":
						self.mem_pos = op_data[1]
					else:
						self.mem_pos = self.mem_tape[op_data[1]]
					return
			case "06": # "06": [3, "jump zero"]
				if op_data[0] == 0:
					if op_flags[1] == "1":
						self.mem_pos = op_data[1]
					else:
						self.mem_pos = self.mem_tape[op_data[1]]
					return
			case "07": # "07": [4, "less than"]
				if op_data[0] < op_data[1]:
					self.mem_tape[op_data[2]] = 1
				else:
					self.mem_tape[op_data[2]] = 0
			case "08": # "08": [4, "equal to"]
				if op_data[0] == op_data[1]:
					self.mem_tape[op_data[2]] = 1
				else:
					self.mem_tape[op_data[2]] = 0
			case "09": # "09": [2, "offset"]
				self.mem_base += op_data[0]
			case "99": # "99": [0, "halt"]
				self.flag_halt = True
		self.mem_pos += self.op_ref[op_base][0]
		return

	def status(self):
		if self.mem_output:
			return self.mem_output[-1]
		else:
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