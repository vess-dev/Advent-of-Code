day_num = 19

import copy
import re

file_load = open("input/day19.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = [temp_itr.strip('\n') for temp_itr in file_in.split("\n\n")]
file_in[0] = dict([temp_itr.split(': ', 1) for temp_itr in file_in[0].split("\n")])
file_in[1] = file_in[1].split("\n")

def run():

	def build(input_in, input_num, input_fix):
		if input_fix:
			if input_num == "8":
				return build(input_in, "42", input_fix) + "+"
			elif input_num == "11":
				rule_a = build(input_in, "42", input_fix)
				rule_b = build(input_in, "31", input_fix)
				return "(?:" + "|".join(f"{rule_a}{{{temp_itr}}}{rule_b}{{{temp_itr}}}" for temp_itr in range(1, 10)) + ")"
		rule_test = input_in[0][input_num]
		if re.fullmatch("\".\"", rule_test):
			return rule_test[1]
		else:
			rule_split = rule_test.split(" | ")
			rule_final = []
			for temp_rule in rule_split:
				rule_nums = temp_rule.split(" ")
				rule_final.append("".join(build(input_in, rule_num, input_fix) for rule_num in rule_nums))
			return "(?:" + "|".join(rule_final) + ")"

	def regi(input_in, input_fix):
		input_new = copy.deepcopy(input_in)
		regex_str = build(input_new, "0", input_fix)
		if input_fix:
			print(regex_str)
		regex_total = 0
		for temp_test in input_new[1]:
			regex_total += bool(re.fullmatch(regex_str, temp_test))
		return regex_total

	return regi(file_in, False), regi(file_in, True)