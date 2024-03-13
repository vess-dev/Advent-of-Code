package main

import (
	"strings"
)

type d16grid struct {
	sizew int
	sizeh int
	grid []string
	stats map[d16point]int
	beams []d16beam
}

type d16point struct {
	posx int
	posy int
}

type d16beam struct {
	posx int
	posy int
	velx int
	vely int
}

func (self *d16grid) get(in_x int, in_y int) string {
	return self.grid[in_x + (in_y * self.sizew)]
}

func d16clean(in_raw string) d16grid {
	grid_out := d16grid{}
	line_split := strings.Split(in_raw, "\n")
	grid_out.sizeh = len(line_split)
	for _, temp_line := range line_split {
		char_split := strings.Split(temp_line, "")
		grid_out.sizew = len(char_split)
		for _, temp_char := range char_split {
			grid_out.grid = append(grid_out.grid, temp_char)
		}
	}
	beam_start := d16beam{
		posx: -1,
		posy: 0,
		velx: 1,
		vely: 0,
	}
	grid_out.beams = append(grid_out.beams, beam_start)
	tline(grid_out)
	return grid_out
}

func d16part1(in_clean d16grid) int {
	return -1
}

func d16part2(in_clean d16grid) int {
	return -1
}

func day16() (any, any) {
	file_string := tload("input/day16.txt")
	file_clean := d16clean(file_string)
	return d16part1(file_clean), d16part2(file_clean)
}