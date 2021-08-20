class Comp:

	mem_tape = []
	mem_pos = 0
	mem_out = []
	flag_halt = False

	op_skip = {
		"01": 4,
		"02": 4,
		"03": 2,
		"04": 2,
		"05": 3,
		"06": 3,
		"07": 4,
		"08": 4,
		"99": 0,
	}

	op_ref = {
		"01": "add",
		"02": "mult",
		"03": "input",
		"04": "output",
		"05": "jump !zero",
		"06": "jump zero",
		"07": "less than",
		"08": "equal to",
		"99": "halt",
	}

	def dbg(self, input_next):
		print(self.op_ref[input_next[0]], input_next, self.mem_tape[self.mem_pos:self.mem_pos + self.op_skip[input_next[0]]])
		return

	def load(self, input_tape):
		self.mem_tape = input_tape
		self.mem_pos = 0
		self.mem_out = []
		self.flag_halt = False
		return

	def get(self, input_pos, input_mode):
		if input_mode == "0":
			return self.mem_tape[self.mem_tape[self.mem_pos + input_pos]]
		elif input_mode == "1":
			return self.mem_tape[self.mem_pos + input_pos]

	def take(self, input_op):
		self.mem_tape[self.mem_tape[self.mem_pos + 1]] = input_op
		self.mem_pos += self.op_skip["03"]
		return
			
	def next(self, input_dbg=False):
		op_next = str(self.mem_tape[self.mem_pos]).rjust(5, "0")
		op_next = [op_next[-2:], list(op_next[:3][::-1])]
		if input_dbg:
			self.dbg(op_next)
		if op_next[0] == "01":
			self.mem_tape[self.mem_tape[self.mem_pos + 3]] = self.get(1, op_next[1][0]) + self.get(2, op_next[1][1])
		elif op_next[0] == "02":
			self.mem_tape[self.mem_tape[self.mem_pos + 3]] = self.get(1, op_next[1][0]) * self.get(2, op_next[1][1])
		elif op_next[0] == "03":
			return "Input"
		elif op_next[0] == "04":
			self.mem_out.append(self.get(1, op_next[1][0]))
		elif op_next[0] == "05":
			if self.get(1, op_next[1][0]) != 0:
				self.mem_pos = self.get(2, op_next[1][1])
				return
		elif op_next[0] == "06":
			if self.get(1, op_next[1][0]) == 0:
				self.mem_pos = self.get(2, op_next[1][1])
				return
		elif op_next[0] == "07":
			if self.get(1, op_next[1][0]) < self.get(2, op_next[1][1]):
				self.mem_tape[self.mem_tape[self.mem_pos + 3]] = 1
			else:
				self.mem_tape[self.mem_tape[self.mem_pos + 3]] = 0
		elif op_next[0] == "08":
			if self.get(1, op_next[1][0]) == self.get(2, op_next[1][1]):
				self.mem_tape[self.mem_tape[self.mem_pos + 3]] = 1
			else:
				self.mem_tape[self.mem_tape[self.mem_pos + 3]] = 0
		elif op_next[0] == "99":
			self.flag_halt = True
			return "Halt"
		self.mem_pos += self.op_skip[op_next[0]]
		return

	def last(self):
		if self.mem_out:
			return self.mem_out[-1]
		else:
			return

	def run(self, input_sim=[]):
		input_pos = 0
		while not self.flag_halt:
			comp_ret = self.next()
			if comp_ret == "Input":
				self.take(input_sim[input_pos])
				input_pos += 1
		return self.last()