import copy
import math

day_num = 18

file_load = open("input/day18.txt", "r")
file_prep = file_load.read()
file_load.close()

MAP_CHECK = [(0, -1), (1, 0), (0, 1), (-1, 0)]

file_prep = list(file_prep)
pos_x = 0
pos_y = 0
file_in = Map()
for temp_char in file_prep:
	if temp_char == '\n':
		pos_x = 0
		pos_y += 1
	if temp_char.isalpha() or temp_char in [".", "@"]:
		pos_tuple = (pos_x, pos_y)
		file_in.add_char(temp_char, pos_tuple)
	pos_x += 1

class Map:
	def __init__(self):
		self.map_pos = {}
		self.map_char = {}
		self.map_keys = {}
	def __str__(self):
		return f"{self.map_pos}\n{self.map_char}"
	def add_char(self, input_in, input_pos):
		self.map_pos[input_in] = input_pos
		self.map_char[input_pos] = input_in
	def move_char(self, input_in, input_pos):
		old_char = self.get_pos(input_in)
		char_to = self.get_pos(input_pos)
		if char_to in self.map_keys:
			del self.map_char[char_to]
			del self.map_keys[char_to]
		self.map_pos[old_char] = "."
		self.map_char[input_in] = input_pos
		self.map_pos[input_pos] = input_in
	def get_pos(self, input_in):
		return self.map_char[input_in]
	def get_char(self, input_in):
		return self.map_pos[input_in]

class Agent:
	def __init__(self, input_in):
		self.cost_path = 0
		self.is_waiting = False
		self.map_full = copy.deepcopy(input_in)
		self.agent_pos = self.map_full.get_char("@")
	def move_pos(self, input_in, input_pos):
		self.map_full.set_char(input_in, input_pos)
	def get_keys():
		agent_list = []
		path_walked = {}
		for temp_check in MAP_CHECK:
			pos_target = (pos_at[0] + temp_check[0], pos_at[1] + temp_check[1])
			if (pos_target not in path_walked) and (pos_target in input_in.map_char):



def run():

	def close(input_in):

		walk(path_walked)
		print(pos_at)
		return

	def walk(input_in):
		print(input_in)
		print(close(input_in))
		return

	return walk(file_in)

if __name__ == "__main__":
	print(run())