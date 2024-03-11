package main

import (
	"crypto/md5"
	"encoding/hex"
	"strings"
)

type d14Dish struct {
	size int
	data []string
}

func (self *d14Dish) get(in_x int, in_y int) string {
	if in_x < 0 || in_x >= self.size || in_y < 0 || in_y >= self.size {
		return "X"
	}
	return self.data[in_x + (in_y * self.size)]
}

func (self *d14Dish) set(in_x int, in_y int, in_char string) {
	self.data[in_x + (in_y * self.size)] = in_char
	return
}

func (self *d14Dish) row(in_idy int) []string {
	out_row := make([]string, self.size)
	for temp_idx := 0; temp_idx < self.size; temp_idx++ {
		out_row[temp_idx] = self.get(temp_idx, in_idy)
	}
	return out_row
}

func (self *d14Dish) debug() {
	for temp_idx := 0; temp_idx < self.size; temp_idx++ {
		tline(strings.Join(self.row(temp_idx), ""))
	}
	tline()
}

func (self *d14Dish) shift(in_x int, in_y int, in_shiftx int, in_shifty int ) {
	for temp_newx, temp_newy := in_x, in_y; self.get(temp_newx + in_shiftx, temp_newy + in_shifty) == "."; temp_newx, temp_newy = temp_newx + in_shiftx, temp_newy + in_shifty {
		self.set(temp_newx, temp_newy, ".")
		self.set(temp_newx + in_shiftx, temp_newy + in_shifty, "O")
	}
}

func (self *d14Dish) tilt(in_dir string) {
	switch in_dir {
		case "up", "left": {
			for temp_idy := 0; temp_idy < self.size; temp_idy++ {
				for temp_idx := 0; temp_idx < self.size; temp_idx++ {
					if self.get(temp_idx, temp_idy) == "O" {
						if in_dir == "up" {
							self.shift(temp_idx, temp_idy, 0, -1)
						} else {
							self.shift(temp_idx, temp_idy, -1, 0)
						}	
					}
				}
			}
		}
		case "down", "right": {
			for temp_idy := self.size; temp_idy >= 0; temp_idy-- {
				for temp_idx := self.size; temp_idx >= 0; temp_idx-- {
					if self.get(temp_idx, temp_idy) == "O" {
						if in_dir == "down" {
							self.shift(temp_idx, temp_idy, 0, 1)
						} else {
							self.shift(temp_idx, temp_idy, 1, 0)
						}
					}
				}
			}
		}
	}
	
	return
}

func d14clean(in_raw string) d14Dish {
	string_list := strings.Split(in_raw, "\n")
	dish_final := d14Dish{}
	dish_final.size = len(string_list)
	for _, temp_line := range string_list {
		char_list := strings.Split(temp_line, "")
		dish_final.data = append(dish_final.data, char_list...)
	}
	return dish_final
}

func d14copy(in_dish *d14Dish) d14Dish {
	var out_dish d14Dish
	out_dish.size = in_dish.size
	out_dish.data = tcopy(in_dish.data)
	return out_dish
}

func d14load(in_dish *d14Dish) int {
	var total_load int
	for temp_idy := 0; temp_idy < in_dish.size; temp_idy++ {
		row_data := in_dish.row(temp_idy)
		for _, temp_char := range row_data {
			if temp_char == "O" {
				total_load += (in_dish.size - temp_idy)
			}
		}
	}
	return total_load
}

func d14part1(in_clean d14Dish) int {
	dish_new := d14copy(&in_clean)
	dish_new.tilt("up")
	return d14load(&dish_new)
}

func d14hash(in_data []string) string {
	data_concat := strings.Join(in_data, "")
	data_hash := md5.Sum([]byte(data_concat))
	return hex.EncodeToString(data_hash[:])
}

func d14part2(in_clean d14Dish) int {
	dish_new := d14copy(&in_clean)
	map_hash := make(map[string]int)
	var list_scores []int
	var loop_target int
	for temp_itr := 0; temp_itr < 1000000000; temp_itr++ {
		dish_new.tilt("up")
		dish_new.tilt("left")
		dish_new.tilt("down")
		dish_new.tilt("right")
		new_hash := d14hash(dish_new.data)
		if _, temp_ok := map_hash[new_hash]; temp_ok {
			loop_start := map_hash[new_hash]
			loop_size := temp_itr - map_hash[new_hash]
			loop_target = ((1000000000 - temp_itr) % loop_size) + loop_start
			break
		} else {
			map_hash[new_hash] = temp_itr
			list_scores = append(list_scores, d14load(&dish_new))
		}
	}
	return list_scores[loop_target - 1]
}

func day14() (any, any) {
	file_string := tload("input/day14.txt")
	file_clean := d14clean(file_string)
	return d14part1(file_clean), d14part2(file_clean)
}