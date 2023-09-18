import copy
import math

day_num = 12

file_load = open("input/day12.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prune = file_prep.replace("<x=", "")
file_prune = file_prune.replace(", y=", " ")
file_prune = file_prune.replace(", z=", " ")
file_prune = file_prune.replace(">", "")
file_prune = file_prune.split("\n")
file_in = [[list(map(int, temp_line.split(" "))), [0, 0, 0]] for temp_line in file_prune]

def run():

	def timestep(input_list):
		for temp_moon in input_list:
			list_other = input_list.copy()
			list_other.remove(temp_moon)
			for temp_pull in list_other:
				for temp_index in range(3):
					if temp_moon[0][temp_index] < temp_pull[0][temp_index]:
						temp_moon[1][temp_index] += 1
					elif temp_moon[0][temp_index] > temp_pull[0][temp_index]:
						temp_moon[1][temp_index] -= 1
		for temp_moon in input_list:
			for temp_index in range(3):
				temp_moon[0][temp_index] += temp_moon[1][temp_index]
		return input_list

	def energy(input_list):
		energy_final = 0
		for temp_moon in input_list:
			energy_potential = 0
			energy_kinetic = 0
			for temp_index in range(3):
				energy_potential += abs(temp_moon[0][temp_index])
				energy_kinetic += abs(temp_moon[1][temp_index])
			energy_final += (energy_potential * energy_kinetic)
		return energy_final

	def simulate(input_in):
		list_moons = copy.deepcopy(input_in)
		for temp_step in range(1000):
			list_moons = timestep(list_moons)
		return energy(list_moons)

	def smallstep(input_list):
		list_moons = copy.deepcopy(input_list)
		for temp_moon in list_moons:
			list_other = list_moons.copy()
			list_other.remove(temp_moon)
			for temp_pull in list_other:
				if temp_moon[0] < temp_pull[0]:
					temp_moon[1] += 1
				elif temp_moon[0] > temp_pull[0]:
					temp_moon[1] -= 1
		for temp_moon in list_moons:
			temp_moon[0] += temp_moon[1]
		return list_moons

	def history(input_in):
		list_moons = copy.deepcopy(input_in)
		x_slice = [[temp_moon[0][0], 0] for temp_moon in list_moons]
		y_slice = [[temp_moon[0][1], 0] for temp_moon in list_moons]
		z_slice = [[temp_moon[0][2], 0] for temp_moon in list_moons]
		x_list, x_toggle, x_final = [], True, 0
		y_list, y_toggle, y_final = [], True, 0
		z_list, z_toggle, z_final = [], True, 0
		while x_toggle:
			if x_toggle:
				x_slice = smallstep(x_slice)
				if x_slice in x_list:
					x_toggle = False
					x_final = len(x_list)
					x_list.clear()
				x_list.append(x_slice)
		while y_toggle:
			if y_toggle:
				y_slice = smallstep(y_slice)
				if y_slice in y_list:
					y_toggle = False
					y_final = len(y_list)
					y_list.clear()
				y_list.append(y_slice)
		while z_toggle:
			if z_toggle:
				z_slice = smallstep(z_slice)
				if z_slice in z_list:
					z_toggle = False
					z_final = len(z_list)
					z_list.clear()
				z_list.append(z_slice)
		return math.lcm(x_final, y_final, z_final)

	return simulate(file_in), history(file_in)

if __name__ == "__main__":
	print(run())