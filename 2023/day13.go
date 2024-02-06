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

func d13debug(in_island *d13Island) {
	tline(in_island)
	for temp_idy := 0; temp_idy < in_island.sizeh; temp_idy++ {
		var temp_line []string
		for temp_idx := 0; temp_idx < in_island.sizew; temp_idx++ {
			temp_char := in_island.get(temp_idx, temp_idy)
			temp_line = append(temp_line, temp_char)
		}
		tline(temp_line)
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
			island_new.sizew = len(char_list)
		}
		island_list[temp_idx] = island_new
	}
	return island_list
}

func d13part1(in_clean []d13Island) int {
	d13debug(&in_clean[0])
	return 5
}

func d13part2(in_clean []d13Island) int {
	return 5
}

func day13() (any, any) {
	file_string := tload("input/day13.txt")
	file_clean := d13clean(file_string)
	return d13part1(file_clean), d13part2(file_clean)
}