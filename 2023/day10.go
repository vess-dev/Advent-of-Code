package main

import (
	"fmt"
	"strings"
)

type d10Point struct {
	x int
	y int
}
var d10PIPE_REL = map[string]map[d10Point]map[string]bool {
	"S": {
		d10Point{1, 0}:{ "-":true, "J":true, "7":true },
		d10Point{0, 1}:{ "|":true, "L":true, "J":true },
		d10Point{-1, 0}:{ "-":true, "L":true, "F":true },
		d10Point{0, -1}:{ "|":true, "7":true, "F":true },
	},
	"|": {
		d10Point{0, 1}:{ "|":true, "L":true, "J":true, "S":true },
		d10Point{0, -1}:{ "|":true, "7":true, "F":true, "S":true },
	},
	"-": {
		d10Point{1, 0}:{ "-":true, "J":true, "7":true, "S":true },
		d10Point{-1, 0}:{ "-":true, "L":true, "F":true, "S":true },
	},
	"L": {
		d10Point{1, 0}:{ "-":true, "J":true, "7":true, "S":true },
		d10Point{0, -1}:{ "|":true, "7":true, "F":true, "S":true },
	},
	"J": {
		d10Point{-1, 0}:{ "-":true, "L":true, "F":true, "S":true },
		d10Point{0, -1}:{ "|":true, "7":true, "F":true, "S":true },
	},
	"7": {
		d10Point{0, 1}:{ "|":true, "L":true, "J":true, "S":true },
		d10Point{-1, 0}:{ "-":true, "L":true, "F":true, "S":true },
	},
	"F": {
		d10Point{1, 0}:{ "-":true, "J":true, "7":true, "S":true },
		d10Point{0, 1}:{ "|":true, "L":true, "J":true, "S":true },
	},
}
var d10MAP_REL = [4][2]int {
	{1, 0}, {0, 1}, {-1, 0}, {0, -1},
}
type d10Map = map[d10Point]string

func d10clean(in_raw string) (d10Map, d10Point, int, int) {
	string_list := strings.Split(in_raw, "\n")
	pipe_map := make(d10Map)
	var pipe_start d10Point
	var max_x int
	max_y := len(string_list)
	for temp_idy, temp_line := range string_list {
		line_list := strings.Split(temp_line, "")
		max_x = len(line_list)
		for temp_idx, temp_pipe := range line_list {
			if temp_pipe == "S" {
				pipe_start = d10Point{temp_idx, temp_idy}
			}
			pipe_map[d10Point{temp_idx, temp_idy}] = temp_pipe
		}
	}
	return pipe_map, pipe_start, max_x - 1, max_y - 1
}

func d10flow(in_map d10Map, in_current d10Point, in_next d10Point, in_diff d10Point) bool {
	current_type := in_map[in_current]
	next_type := in_map[in_next]
	if d10PIPE_REL[current_type][in_diff][next_type] {
		return true
	}
	return false
}

func d10walk(in_map d10Map, in_start d10Point) (int, d10Map) {
	var step_count int
	current_point := in_start
	last_point := in_start
	loop_map := tcopymap(in_map)
	for true {
		for _, temp_pair := range d10MAP_REL {
			check_point := d10Point{temp_pair[0], temp_pair[1]}
			next_point := d10Point{current_point.x + temp_pair[0], current_point.y + temp_pair[1]}
			if next_point != last_point {
				if d10flow(in_map, current_point, next_point, check_point) {
					//tline(in_map[current_point], current_point, next_point)
					loop_map[current_point] = "X"
					last_point = current_point
					current_point = next_point
					step_count += 1
					break
				}
			}
		}
		if in_map[current_point] == "S" {
			break
		}
	}
	farthest_dist := ((step_count + 1) / 2)
	return farthest_dist, loop_map
}

func d10part1(in_map d10Map, in_start d10Point) (int, d10Map) {
	return d10walk(in_map, in_start)
}

func d10debug(in_map d10Map, in_maxx int, in_maxy int) {
	for temp_y := 0; temp_y <= in_maxx; temp_y++ {
		for temp_x := 0; temp_x <= in_maxx; temp_x++ {
			fmt.Print(in_map[d10Point{temp_x, temp_y}])
		}
		fmt.Println()
	}
}

func d10count(in_map d10Map, in_x int, in_y int, in_maxx int, in_maxy int) (int, int, int, int) {
	var right_count int
	for temp_x := in_x; temp_x >= 0; temp_x-- {
		if in_map[d10Point{temp_x, in_y}] == "X" {
			right_count += 1
		}
	}
	var down_count int
	for temp_y := in_y; temp_y <= in_maxy; temp_y++ {
		if in_map[d10Point{in_x, temp_y}] == "X" {
			down_count += 1
		}
	}
	var left_count int
	for temp_x := in_x; temp_x <= in_maxx; temp_x++ {
		if in_map[d10Point{temp_x, in_y}] == "X" {
			left_count += 1
		}
	}
	var up_count int
	for temp_y := in_y; temp_y >= 0; temp_y-- {
		if in_map[d10Point{in_x, temp_y}] == "X" {
			up_count += 1
		}
	}
	return right_count, down_count, left_count, up_count
}

func d10part2(in_map d10Map, in_start d10Point, in_maxx int, in_maxy int) int {
	var inside_seen int
	for temp_y := 0; temp_y <= in_maxy; temp_y++ {
		for temp_x := 0; temp_x <= in_maxx; temp_x++ {
			if in_map[d10Point{temp_x, temp_y}] != "X" {
				x_right, x_down, x_left, x_up := d10count(in_map, temp_x, temp_y, in_maxx, in_maxy)
				if (x_right > 0) && (x_down > 0) && (x_left > 0) && (x_up > 0) {
					if (x_right % 2 == 1) || (x_down % 2 == 1) || (x_left % 2 == 1) || (x_up % 2 == 1) {
						tline(in_map[d10Point{temp_x, temp_y}], temp_x, temp_y, x_right, x_down, x_left, x_up)
						inside_seen += 1
					}
				}
			}
		}
	}
	return inside_seen
}

func day10() (any, any) {
	file_string := tload("input/day10.txt")
	file_map, file_start, max_x, max_y := d10clean(file_string)
	dist_far, loop_map := d10part1(file_map, file_start)
	tuse(max_x, max_y, loop_map)
	return dist_far, d10part2(loop_map, file_start, max_x, max_y)
}