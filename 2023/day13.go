package main

import (
	"strings"
)

type d13Island struct {
	sizew int
	sizeh int
	data []string
}

func (self *d13Island) get(in_x int, in_y int) string {
	return self.data[in_x + (in_y * self.sizew)]
}

func (self *d13Island) row(in_idy int) []string {
	out_row := make([]string, self.sizew)
	for temp_idx := 0; temp_idx < self.sizew; temp_idx++ {
		out_row[temp_idx] = self.get(temp_idx, in_idy)
	}
	return out_row
}

func (self *d13Island) col(in_idx int) []string {
	out_col := make([]string, self.sizeh)
	for temp_idy := 0; temp_idy < self.sizeh; temp_idy++ {
		out_col[temp_idy] = self.get(in_idx, temp_idy)
	}
	return out_col
}

func d13debug(in_island *d13Island) {
	tline(in_island.sizew, in_island.sizeh)
	for temp_idy := 0; temp_idy < in_island.sizeh; temp_idy++ {
		tline(strings.Join(in_island.row(temp_idy)[:], ""))
	}
}

func d13clean(in_raw string) []d13Island {
	string_list := strings.Split(in_raw, "\n\n")
	island_list := make([]d13Island, len(string_list))
	for temp_idx, temp_island := range string_list {
		island_new := d13Island{}
		line_list := strings.Split(temp_island, "\n")
		island_new.sizeh = len(line_list)
		for _, temp_line := range line_list {
			char_list := strings.Split(temp_line, "")
			island_new.data = append(island_new.data, char_list...)
			if island_new.sizew == 0 {
				island_new.sizew = len(char_list)
			}
		}
		island_list[temp_idx] = island_new
	}
	return island_list
}

func d13ripple(in_island *d13Island, in_vertical bool, in_start int, in_cap int) bool {
	for int_left, int_right := in_start, in_start + 1; ((int_left >= 0) && (int_right < in_cap)); int_left, int_right = int_left-1, int_right+1 {
		tline(int_left + 1, int_right + 1, in_vertical)
		switch in_vertical {
			case false: if !tequal(in_island.row(int_left), in_island.row(int_right)) {return false}
			case true: if !tequal(in_island.col(int_left), in_island.col(int_right)) {return false}
		}
	}
	return true
}

func d13reflect(in_island *d13Island, in_vertical bool) int {
	var itr_cap int
	switch in_vertical {
		case false: itr_cap = in_island.sizeh
		case true: itr_cap = in_island.sizew
	}
	for ret_int := 0; ret_int < (itr_cap - 1); ret_int++ {
		if d13ripple(in_island, in_vertical, ret_int, itr_cap) {
			switch in_vertical {
				case false: return (ret_int + 1) * 100
				case true: return ret_int + 1
			}
		}
	}
	return 0
}

func d13part1(in_clean []d13Island) int {
	var int_total int
	for _, temp_island := range in_clean {
		d13debug(&temp_island)
		temp_one := d13reflect(&temp_island, false)
		temp_two := d13reflect(&temp_island, true)
		int_total += temp_one + temp_two
	}
	return int_total
}

func d13part2(in_clean []d13Island) int {
	return 5
}

func day13() (any, any) {
	file_string := tload("input/day13.txt")
	file_clean := d13clean(file_string)
	return d13part1(file_clean), d13part2(file_clean)
}