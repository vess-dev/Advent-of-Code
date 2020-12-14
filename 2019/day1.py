day_num = 1

import math

file_load = open("input/day1.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("\n")))

def run():

	def fuel(input_mass):
		return math.floor(input_mass / 3) - 2

	def launch(input_in):
		fuel_total = 0
		for temp_mass in input_in:
			fuel_total += fuel(temp_mass)
		return fuel_total

	def stonk(input_in):
		fuel_total = 0
		for temp_mass in input_in:
			while temp_mass >= 0:
				fuel_calc = fuel(temp_mass)
				if fuel_calc > 0:
					fuel_total += fuel_calc
					temp_mass = fuel_calc
				else:
					temp_mass = -1
		return fuel_total

	return launch(file_in), stonk(file_in)