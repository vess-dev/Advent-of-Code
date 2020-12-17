day_num = 16

from collections import OrderedDict
import math

file_load = open("input/day16.txt", "r")
file_in = file_load.read()
file_load.close()

file_prep = [temp_itr.split("\n") for temp_itr in file_in.split("\n\n")]
file_prep[0] = [temp_itr.split(": ")[1] for temp_itr in file_prep[0]]
file_prep[0] = [temp_itr.split(" or ") for temp_itr in file_prep[0]]
file_prep[0] = [list(map(int, temp_sub.split("-"))) for temp_itr in file_prep[0] for temp_sub in temp_itr]
file_prep[0] = [list(range(temp_itr[0], temp_itr[1] + 1)) for temp_itr in file_prep[0]]
temp_new = []
temp_pos = 0
while temp_pos < len(file_prep[0]):
	temp_new.append([file_prep[0][temp_pos], file_prep[0][temp_pos + 1]])
	temp_pos += 2
file_prep[0] = temp_new
file_prep[1].pop(0)
file_prep[1] = [list(map(int, temp_itr.split(","))) for temp_itr in file_prep[1]]
file_prep[1] = [temp_sub for temp_itr in file_prep[1] for temp_sub in temp_itr]
file_prep[2].pop(0)
file_prep[2] = [list(map(int, temp_itr.split(","))) for temp_itr in file_prep[2]]
file_fields = [temp_itr.split("\n") for temp_itr in file_in.split("\n\n")]
file_fields = [temp_itr.split(": ")[0] for temp_itr in file_fields[0]]
file_prep.insert(0, file_fields)
file_in = file_prep

def run():

	def rate(input_in):
		error_total = 0
		num_range = set([temp_num for temp_item in [temp_range for temp_bracket in input_in[1] for temp_range in temp_bracket] for temp_num in temp_item])
		for temp_ticket in input_in[3]:
			for temp_value in temp_ticket:
				if temp_value not in num_range:
					error_total += temp_value
		return error_total

	def prune(input_in, input_range):
		input_new = []
		num_range = set([temp_num for temp_item in [temp_range for temp_bracket in input_range for temp_range in temp_bracket] for temp_num in temp_item])
		for temp_ticket in input_in:
			flag_keep = True
			for temp_value in temp_ticket:
				if temp_value not in num_range:
					flag_keep = False
			if flag_keep:
				input_new.append(temp_ticket)
		return input_new

	def depart(input_in):
		input_new = input_in.copy()
		input_new[3] = prune(input_in[3], input_in[1])
		field_count = OrderedDict()
		for temp_itr in range(0, len(input_new[0])):
			field_count[temp_itr] = []
		for temp_ticket in input_new[3]:
			for temp_valpos, temp_value in enumerate(temp_ticket):
				for temp_brapos, temp_bracket in enumerate(input_new[1]):
					if temp_value in (temp_bracket[0] + temp_bracket[1]):
						if temp_valpos not in field_count[temp_brapos]:
							field_count[temp_brapos].append(temp_valpos)
					else:
						if ("!" + str(temp_valpos)) not in field_count[temp_brapos]:
							field_count[temp_brapos].append("!" + str(temp_valpos))
		for temp_field in field_count:
			new_field = []
			for temp_test in field_count[temp_field]:
				if (("!" + str(temp_test)) not in field_count[temp_field]) and isinstance(temp_test, int):
					new_field.append(temp_test)
			field_count[temp_field] = new_field
		field_done = []
		while len(field_done) != 20:
			for temp_field in field_count:
				if len(field_count[temp_field]) == 1 and temp_field not in field_done:
					for temp_change in field_count:
						if field_count[temp_change] != field_count[temp_field]:
							if field_count[temp_field][0] in field_count[temp_change]:
								field_count[temp_change].remove(field_count[temp_field][0])
					field_done.append(temp_field)
		field_math = list(field_count.values())[0:6]
		field_math = [temp_sub for temp_itr in field_math for temp_sub in temp_itr]
		field_total = 1
		for temp_pos in field_math:
			field_total *= input_in[2][temp_pos]
		return field_total

	return rate(file_in), depart(file_in)