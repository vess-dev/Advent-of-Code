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
			for temp_pull in input_list:
				if temp_moon != temp_pull:
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
		for temp_moon in input_list:
			for temp_pull in input_list:
				if temp_moon != temp_pull:
					if temp_moon[0] < temp_pull[0]:
						temp_moon[1] += 1
					elif temp_moon[0] > temp_pull[0]:
						temp_moon[1] -= 1
		for temp_moon in input_list:
			temp_moon[0] += temp_moon[1]
		return input_list

	def history(input_in):
		list_moons = copy.deepcopy(input_in)
		x_slice = [[temp_moon[0][0], 0] for temp_moon in list_moons]
		y_slice = [[temp_moon[0][1], 0] for temp_moon in list_moons]
		z_slice = [[temp_moon[0][2], 0] for temp_moon in list_moons]
		x_final, y_final, z_final = 0, 0, 0
		list_history = {}
		while True:
			x_slice = smallstep(x_slice)
			if str(x_slice) in list_history:
				x_final = len(list_history)
				list_history.clear()
				break
			list_history[str(x_slice)] = True
		while True:
			y_slice = smallstep(y_slice)
			if str(y_slice) in list_history:
				y_final = len(list_history)
				list_history.clear()
				break
			list_history[str(y_slice)] = True
		while True:
			z_slice = smallstep(z_slice)
			if str(z_slice) in list_history:
				z_final = len(list_history)
				list_history.clear()
				break
			list_history[str(z_slice)] = True
		return math.lcm(x_final, y_final, z_final)

	return simulate(file_in), history(file_in)

if __name__ == "__main__":
	print(run())