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
		"05": [3, "jump !zero"],
		"06": [3, "jump zero"],
		"07": [4, "less than"],
		"08": [4, "equal to"],
		"09": [2, "offset"],
		"99": [0, "halt"],
	}

	def dbg(self, input_next):
		parm_string = ""
		temp_pos = self.mem_pos
		temp_end = (self.mem_pos + self.op_ref[input_next[0]][0])
		if self.op_ref[input_next[0]][0] != 0:
			temp_end -= 1
		while temp_pos < temp_end:
			temp_pos += 1
			parm_string += str(self.mem_tape[temp_pos]) + " "
		print(self.op_ref[input_next[0]][1], input_next, parm_string)
		return

	def load(self, input_tape):
		self.mem_tape = input_tape
		self.mem_pos = 0
		self.mem_out = []
		self.mem_base = 0
		self.flag_halt = False
		return

	def get(self, input_pos, input_mode):
		# Position mode.
		if input_mode == "0":
			mem_target = (self.mem_pos + input_pos)
			if self.mem_tape.get(mem_target, None) == None:
				self.mem_tape[mem_target] = 0
			mem_target = self.mem_tape[self.mem_pos + input_pos]
			if self.mem_tape.get(mem_target, None) == None:
				self.mem_tape[mem_target] = 0
			return self.mem_tape[self.mem_tape[self.mem_pos + input_pos]]
		# Immediate value mode.
		elif input_mode == "1":
			mem_target = (self.mem_pos + input_pos)
			if self.mem_tape.get(mem_target, None) == None:
				self.mem_tape[mem_target] = 0
			return self.mem_tape[self.mem_pos + input_pos]
		# Relative base mode.
		elif input_mode == "2":
			mem_target = (self.mem_base + input_pos)
			if self.mem_tape.get(mem_target, None) == None:
				self.mem_tape[mem_target] = 0
			return self.mem_tape[self.mem_base + self.mem_tape[self.mem_pos + input_pos]]

	def take(self, input_op, input_target):
		self.mem_tape[input_target] = input_op
		self.mem_pos += self.op_ref["03"][0]
		return
			
	def next(self, input_dbg=False):
		op_next = str(self.mem_tape[self.mem_pos]).rjust(5, "0")
		op_next = [op_next[-2:], list(op_next[:3][::-1])]
		if input_dbg:
			self.dbg(op_next)
		if op_next[0] in ["01", "02", "07", "08"]:
			if op_next[1][2] == "0":
				mem_target = self.mem_tape[self.mem_pos + 3]
			elif op_next[1][2] == "2":
				mem_target = self.mem_base + self.mem_tape[self.mem_pos + 3]
		# "01": [4, "add"]
		if op_next[0] == "01":
			self.mem_tape[mem_target] = self.get(1, op_next[1][0]) + self.get(2, op_next[1][1])
		# "02": [4, "mult"]
		elif op_next[0] == "02":
			self.mem_tape[mem_target] = self.get(1, op_next[1][0]) * self.get(2, op_next[1][1])
		# "03": [2, "input"]
		elif op_next[0] == "03":
			if op_next[1][0] == "0":
				mem_target = self.mem_tape[self.mem_pos + 1]
			elif op_next[1][0] == "2":
				mem_target = self.mem_base + self.mem_tape[self.mem_pos + 1]
			return ("Input", mem_target)
		# "04": [2, "output"]
		elif op_next[0] == "04":
			self.mem_out.append(self.get(1, op_next[1][0]))
		# "05": [3, "jump !zero"]
		elif op_next[0] == "05":
			if self.get(1, op_next[1][0]) != 0:
				self.mem_pos = self.get(2, op_next[1][1])
				return (None, None)
		# "06": [3, "jump zero"]
		elif op_next[0] == "06":
			if self.get(1, op_next[1][0]) == 0:
				self.mem_pos = self.get(2, op_next[1][1])
				return (None, None)
		# "07": [4, "less than"]
		elif op_next[0] == "07":
			if self.get(1, op_next[1][0]) < self.get(2, op_next[1][1]):
				self.mem_tape[mem_target] = 1
			else:
				self.mem_tape[mem_target] = 0
		# "08": [4, "equal to"]
		elif op_next[0] == "08":
			if self.get(1, op_next[1][0]) == self.get(2, op_next[1][1]):
				self.mem_tape[mem_target] = 1
			else:
				self.mem_tape[mem_target] = 0
		# "09": [2, "offset"]
		elif op_next[0] == "09":
			self.mem_base += self.get(1, op_next[1][0])
		# "99": [0, "halt"]
		elif op_next[0] == "99":
			self.flag_halt = True
			return ("Halt", None)
		self.mem_pos += self.op_ref[op_next[0]][0]
		return (None, None)

	def last(self):
		if self.mem_out:
			return self.mem_out[-1]
		else:
			return

	def run(self, input_sim=[], input_dbg=False):
		input_pos = 0
		while not self.flag_halt:
			comp_ret = self.next(input_dbg)
			if comp_ret[0] == "Input":
				if (input_pos + 1) <= len(input_sim):
					self.take(input_sim[input_pos], comp_ret[1])
					input_pos += 1
				else:
					return self.last()
		return self.last()