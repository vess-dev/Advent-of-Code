package main

import (
	"strings"

	goraph "gopkg.in/gyuho/goraph.v2"
)

type d17Grid struct {
	sizew int
	sizeh int
	grid []int
}
type d17Point struct {
	posx int
	posy int
}
type d17Cost struct {
	costx int
	costy int
}

func (self *d17Grid) get(in_x int, in_y int) int {
	return self.grid[in_x + (in_y * self.sizew)]
}

func d17clean(in_raw string) d17Grid {
	grid_out := d17Grid{}
	line_split := strings.Split(in_raw, "\n")
	grid_out.sizeh = len(line_split)
	for _, temp_line := range line_split {
		char_split := strings.Split(temp_line, "")
		grid_out.sizew = len(char_split)
		for _, temp_char := range char_split {
			char_cast := tnum(temp_char)
			grid_out.grid = append(grid_out.grid, char_cast)
		}
	}
	return grid_out
}

func d17name(in_x int, in_y int) string {
	return tstring("(", in_x, ",", in_y, ")")
}

func d17cost(in_grid d17Grid, in_x1 int, in_y1 int, in_x2 int, in_y2 int) int {
	diff_x := tsign(in_x2 - in_x1)
	diff_y := tsign(in_y2 - in_y1)
	tuse(diff_x, diff_y)
	total_cost := in_grid.get(in_x1, in_y1)
	return total_cost
}

func d17local(in_x int, in_y int, in_range int, in_maxx int, in_maxy int) []d17Point {
	point_out := []d17Point{}
	for temp_idx := (in_x - in_range); temp_idx <= (in_x + in_range); temp_idx++ {
		if (temp_idx >= 0) && (temp_idx < in_maxx) {
			for temp_idy := (in_y - in_range); temp_idy <= (in_y + in_range); temp_idy++ {
				if (temp_idy >= 0) && (temp_idy < in_maxy) {
					if ((temp_idx != in_x) && (temp_idy != in_y)) {
						if (tabs(temp_idx - in_x) == 1) || (tabs(temp_idy - in_y) == 1) {
							point_new := d17Point{temp_idx, temp_idy}
							point_out = append(point_out, point_new)
						}
					}
				}
			}
		}
	}
	return point_out
}

func d17build(in_clean d17Grid, in_range int) goraph.Graph {
	graph_out := goraph.NewGraph()
	for temp_idy := 0; temp_idy < in_clean.sizew; temp_idy++ {
		for temp_idx := 0; temp_idx < in_clean.sizew; temp_idx++ {
			node_name := d17name(temp_idx, temp_idy)
			node_new := goraph.NewNode(node_name)
			graph_out.AddNode(node_new)
		}
	}
	return graph_out
}

func d17part1(in_clean d17Grid) int {
	//graph_build := d17build(in_clean, 3)
	//tline(d17local(in_clean.sizew, in_clean.sizeh, 0, 0, 3))
	//tline(graph_build.GetNodes())
	tline(d17local(3, 3, 3, in_clean.sizew, in_clean.sizeh))
	tline(d17cost(in_clean, 1, 1, 0, 0))
	tuse(in_clean)
	return -1
}

func d17part2(in_clean d17Grid) int {
	tuse(in_clean)
	return -1
}

func day17() (any, any) {
	file_string := tload("input/day17.txt")
	file_clean := d17clean(file_string)
	return d17part1(file_clean), d17part2(file_clean)
}