day_num = 13

import copy
from functools import reduce

file_load = open("input/input13.txt", "r")
file_prep = file_load.read()
file_load.close()
file_prep = file_prep.split("\n")

file_in = []
file_in.append(int(file_prep[0]))
file_in.append(list(map(int, file_prep[1].replace("x,","").split(","))))

file_new = []
for temp_index, temp_num in enumerate(file_prep[1].split(",")):
	if temp_num == "x":
		continue
	temp_num = int(temp_num)
	file_new.append((temp_num - temp_index, temp_num))

def run():

	def catch(input_in):
		time_stop = input_in[0]
		bus_ids = input_in[1]
		bus_sched = []
		time_step = 1
		while (time_step * bus_ids[0]) < time_stop:
			for bus_id in bus_ids:
				bus_sched.append([bus_id, bus_id * time_step])
			time_step += 1
		bus_sched.sort(key=lambda temp_bus: temp_bus[1])
		for temp_bus in bus_sched:
			if temp_bus[1] > time_stop:
				return temp_bus[0] * (temp_bus[1] - time_stop)

	def crt(input_in):
		crt_mult = 1
		for temp_bus in input_in:
			crt_mult *= temp_bus[1]
		crt_total = 0
		for temp_bus in input_in:
			temp_num = crt_mult // temp_bus[1]
			crt_total += temp_bus[0] * temp_num * pow(temp_num, temp_bus[1] - 2, temp_bus[1])
			crt_total %= crt_mult
		return crt_total

	return catch(file_in), crt(file_new)