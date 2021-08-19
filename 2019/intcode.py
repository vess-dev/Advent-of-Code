class Comp:

	mem_tape = []
	mem_pos = 0

	op_skip = {
		"01": 4,
		"02": 4,
		"03": 2,
		"04": 2,
	}

	def load(self, input_tape):
		self.mem_tape = input_tape
		self.mem_pos = 0
		return

	def get(self, input_pos, input_mode):
		if input_mode == "0":
			return self.mem_tape[self.mem_tape[self.mem_pos + input_pos]]
		elif input_mode == "1":
			return self.mem_tape[self.mem_pos + input_pos]
			
	def next(self):
		op_next = str(self.mem_tape[self.mem_pos]).rjust(5, "0")
		op_next = [op_next[-2:], list(op_next[:3][::-1])]
		if op_next[0] == "01":
			self.mem_tape[self.mem_tape[self.mem_pos + 3]] = self.get(1, op_next[1][1]) + self.get(2, op_next[1][2])
		elif op_next[0] == "02":
			self.mem_tape[self.mem_tape[self.mem_pos + 3]] = self.get(1, op_next[1][1]) * self.get(2, op_next[1][2])
		elif op_next[0] == "99":
			return "Break"
		self.mem_pos += self.op_skip[op_next[0]]
		return