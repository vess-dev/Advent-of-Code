day_num = 19

import copy
from collections import defaultdict

file_load = open("input/day19.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = [defaultdict(list), []]
file_prep = [temp_itr.strip('\n') for temp_itr in file_prep.split("\n\n")]
for temp_rule in file_prep[0].replace("\"", "").split("\n"):
	rule_num, rule_parts = temp_rule.split(": ")
	for temp_part in rule_parts.split(" | "):
		if temp_part in ["a", "b"]:
			file_in[0][int(rule_num)] = temp_part
		else:
			file_in[0][int(rule_num)].append(list(eval(temp_itr) for temp_itr in temp_part.split()))
file_in[1] = file_prep[1].split("\n")

def run():

	def itr(input_in, input_rul, input_str):
		if not input_rul:
			return len(input_str) == 0
		rule_check = input_in[0][input_rul.pop(0)]
		if rule_check in ["a", "b"]:
			return input_str.startswith(rule_check) and itr(input_in, input_rul, input_str[1:])
		else:
			return any(itr(input_in, temp_rule + input_rul, input_str) for temp_rule in rule_check)

	def rule(input_in, input_adjust):
		if input_adjust:
			input_in[0][8] = [[42], [42, 8]]
			input_in[0][11] = [[42, 31], [42, 11, 31]]
		return sum(itr(input_in, [0], temp_line) for temp_line in input_in[1])

	return rule(file_in, False), rule(file_in, True)